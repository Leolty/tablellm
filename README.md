# TableLLM

This repository is the official implementation of the paper "Rethinking Tabular Data Understanding with Large Language Models" (https://arxiv.org/abs/2312.16702)

## Installation

### Clone the repository

```bash
git clone https://github.com/Leolty/tablellm.git
cd tablellm
```

### Install the requirements

```bash
conda create -n tablellm python=3.10
conda activate tablellm
pip install -r requirements.txt
```

## Data

Unzip the [assets/data.zip](assets/data.zip) file to get the data.

```bash
unzip assets/data.zip
```

You will get the following files:

```bash
data
├── wtq.json
├── tabfact.json
```

## Experiment

### To reproduce the results

To reproduce the results in the paper, check the following files:

- [run_cot.py](run_cot.py): Run Direct Prompting (DP)
- [run_agent.py](run_agent.py): Run PyAgent

We give detailed running instructions and specific running commands in the comments of the files.

### To use the table agent

To use the table agent, check the notebook:

- [examples/pyagent.ipynb](examples/pyagent.ipynb)

## Citation

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







