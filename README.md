# TableLLM Repository

Official implementation of "Rethinking Tabular Data Understanding with Large Language Models" ([Paper](https://arxiv.org/abs/2312.16702)). Dive into the world of advanced tabular data analysis with our Large Language Models!

## 🚀 Installation

### 🛠 Clone the Repository

```bash
git clone https://github.com/Leolty/tablellm.git
cd tablellm
```

### 📦 Install Requirements

```bash
conda create -n tablellm python=3.10
conda activate tablellm
pip install -r requirements.txt
```

## 🗂 Data

Extract the provided data with the following command:

```bash
unzip assets/data.zip
```

Your data directory will include:

```bash
data
├── wtq.json
├── tabfact.json
```

## 🧪 Experimentation

### 🔬 Reproducing the Results

For replicating our study's findings, navigate to the [scripts](scripts) folder:

- [scripts/all_dp.sh](scripts/all_dp.sh): Runs direct prompting on all wtq datasets.
- [scripts/all_pyagent.sh](scripts/all_pyagent.sh): Runs python shell agent on all wtq datasets.
- [scripts/vicuna_example.sh](scripts/vicuna_example.sh): An example of changing base model to `vicuna` on the subsampled wtq dataset.
  > Ensure [vllm](https://github.com/vllm-project/vllm) is installed beforehand.
- [scripts/perturbed_example.sh](scripts/perturbed_example.sh): An example of running experiments on perturbed wtq dataset.

Parameters are detailed in [run_cot.py](run_cot.py) and [run_agent.py](run_agent.py).

### 🤖 Using the Table Agent

Explore the table agent through:

- [examples/pyagent.ipynb](examples/pyagent.ipynb)

## 📚 Citation

To cite our work in your research, use the following bibtex entry:

```bibtex
@misc{liu2023rethinking,
      title={Rethinking Tabular Data Understanding with Large Language Models}, 
      author={Tianyang Liu and Fei Wang and Muhao Chen},
      year={2023},
      eprint={2312.16702},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```