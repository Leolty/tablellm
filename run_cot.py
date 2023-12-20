import os
import json

from typing import Optional
from tqdm import tqdm
from fire import Fire
from agent.model import Model

from utils.data import construct_markdown_table
from utils.execute import markdown_to_df, remove_merged_suffixes
from utils.table import transpose, sort_dataframe

from run_helper import load_dataset, get_cot_prompt, query, check_transpose, check_sort, read_json_file

"""
- Run COT on wikitablequestion dataset using openai API (GPT-3.5-turbo-0613)

CUDA_VISIBLE_DEVICES=0 python run_cot.py \
    --model gpt-3.5-turbo-0613 --long_model gpt-3.5-turbo-16k-0613 \
    --provider openai --dataset wtq \
    --perturbation none --norm True --disable_resort True --norm_cache True \
    --resume 0 --stop_at 1e6 --self_consistency 10 --temperature 0.8 \
    --log_dir output/wtq_cot_wo_norm --cache_dir cache/wtq_cot_wo_norm

- Run COT on wikitablequestion dataset using vllm (vicuna-13b-v1.5-16k)

CUDA_VISIBLE_DEVICES=0 python run_cot.py \
    --model None --long_model lmsys/vicuna-13b-v1.5-16k \
    --provider vllm --dataset wtq \
    --perturbation none --norm True --disable_resort True --norm_cache True \
    --resume 0 --stop_at 1e6 --self_consistency 10 --temperature 0.8 \
    --log_dir output/wtq_cot_vicuna_wo_norm --cache_dir cache/wtq_cot_vicuna_wo_norm

"""

def main(
        model:Optional[str] = "gpt-3.5-turbo-0613", 
        long_model:Optional[str] = "gpt-3.5-turbo-16k-0613",
        provider: str = "openai",
        dataset:str = "wtq", # wtq
        perturbation: str = "none", # none, transpose, shuffle, transpose_shuffle
        norm: bool = True,
        disable_resort: bool = True,
        norm_cache: bool = True,
        sub_sample: bool = True,
        resume:int = 0,
        stop_at:int = 1e6,
        self_consistency:int = 10,
        temperature:float=0.8,
        log_dir: str = "output/tabfact_cot",
        cache_dir: str = "cache",
):
    
    #### create log & cache dir and save config ####
    os.makedirs(log_dir, exist_ok=True)
    os.makedirs(cache_dir, exist_ok=True)
    
    # store the config
    config_path = os.path.join(log_dir, "config.json")
    with open(config_path, "w") as f:
        json.dump({key: value for key, value in locals().items() if key != 'f'}, f, indent=4)
    
    #### load dataset and cot prompt ####
    data = load_dataset(dataset)
    cot_prompt = get_cot_prompt(dataset)

    #### load the model ####
    if model:
        model = Model(model, provider=provider)
    if long_model:
        long_model = Model(long_model, provider=provider)
    
    #### load the cache ####
    transpose_cache = read_json_file(os.path.join(cache_dir, "transpose.json"))
    resort_cache = read_json_file(os.path.join(cache_dir, "resort.json"))
    
    #### prepare the iterator ####
    global_i = 0
    break_flag = False
    total = sum([len(d['sampled_indices']) for d in data]) if sub_sample else sum([len(d['questions']) for d in data])
    pbar = tqdm(total=stop_at if stop_at < total else total)
    
    #### start the loop ####
    for table_idx, d in enumerate(data):
        if break_flag:
            break
        
        index_list = d['sampled_indices'] if sub_sample else range(len(d["questions"]))
        
        # if the table is empty, skip
        if len(index_list) == 0:
            continue
            
        # load table infos
        table_id = d["table_id"]
        title = d["title"]

        if perturbation == "none":
            table = construct_markdown_table(**d["table"])
        elif perturbation == "transpose":
            table = construct_markdown_table(**d["transposed_table"])
        elif perturbation == "shuffle":
            table = construct_markdown_table(**d["row_shuffled_table"])
        elif perturbation == "transpose_shuffle":
            table = construct_markdown_table(**d["row_shuffled_transposed_table"])
            
        df = markdown_to_df(table)

        # transpose and sort if necessary
        transpose_flag = False
        resort_list = []
        
        if norm:
            transpose_flag = check_transpose(model, long_model, table, title, table_id, perturbation, transpose_cache, norm_cache, cache_dir)
            
            if transpose_flag:
                transposed_df = transpose(df)
                df = remove_merged_suffixes(transposed_df)
            
            if not disable_resort:
                resort_list = check_sort(model, long_model, df, title, table_id, perturbation, resort_cache, norm_cache, cache_dir)
                df = sort_dataframe(df, resort_list)
            
        # reset the table
        table = df.to_markdown()

        for idx in index_list:
            if global_i < resume:
                global_i += 1
                pbar.update(1)
                continue
            elif global_i >= stop_at:
                break_flag = True
                break

            question = d["questions"][idx]
            answer = d["answers"][idx]
            question_id = d["ids"][idx]

            prompt = cot_prompt.replace("[TABLE]", table)\
                .replace("[QUESTION]", question)\
                .replace("[TITLE]", title)\
                .strip()

            text, response = query(model, long_model, prompt, temperature, self_consistency)
        
            log_path = os.path.join(log_dir, "log", f"{global_i}.txt")
            os.makedirs(os.path.dirname(log_path), exist_ok=True)
            with open(log_path, "w") as f:
                f.write("===================Title===================\n")
                f.write(title + "\n")
                f.write("===================Table===================\n")
                f.write(table + "\n")
                f.write("===================Question===================\n")
                f.write(question + "\n")
                f.write("===================Text===================\n")
                f.write(text if isinstance(text, str) else "\n".join(text))
                f.write("\n")
                f.write("===================Answer===================\n")
                f.write(",".join(answer) if isinstance(answer, list) else str(answer))
                f.write("\n")

            res = {
                "idx": global_i,
                "answer": answer,
                "text": text,
                "transpose": transpose_flag,
                "resort": resort_list,
                "question_id": question_id,
                "table_id": table_id,
                "title": title,
                "table": table,
                "question": question,
            }

            with open(os.path.join(log_dir, "result.jsonl"), "a") as f:
                json.dump(res, f)
                f.write("\n")

            global_i += 1
            pbar.update(1)

if __name__ == "__main__":
    Fire(main)