# TableLLM Repository

Official implementation of the paper "Rethinking Tabular Data Understanding with Large Language Models" ([https://arxiv.org/abs/2312.16702](https://arxiv.org/abs/2312.16702)).

## 🚀 Installation

### 🛠 Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/Leolty/tablellm.git
cd tablellm
```

### 📦 Install Dependencies

Create and activate a new environment, and install the required packages:

```bash
conda create -n tablellm python=3.10
conda activate tablellm
pip install -r requirements.txt
```

## 🗂 Data

Unzip the dataset provided in the repository:

```bash
unzip assets/data.zip
```

After unzipping, you should have the following files:

```bash
data
├── wtq.json
├── tabfact.json
```

## 🔬 Experimentation

### 🔄 Reproducing the Results

For replicating our study's findings, navigate to the [scripts](scripts) folder:

- [scripts/all_dp.sh](scripts/all_dp.sh): Runs direct prompting on all wtq datasets.
- [scripts/all_pyagent.sh](scripts/all_pyagent.sh): Runs python shell agent on all wtq datasets.
- [scripts/vicuna_example.sh](scripts/vicuna_example.sh): An example of changing base model to `vicuna` on the subsampled wtq dataset.
  > Ensure [vllm](https://github.com/vllm-project/vllm) is installed beforehand.
- [scripts/perturbed_example.sh](scripts/perturbed_example.sh): An example of running experiments on perturbed wtq dataset.

Detailed explanations of parameters can be found in [run_cot.py](run_cot.py) and [run_agent.py](run_agent.py).

### 🤖 Using the Table Agent

For hands-on experience with the table agent, refer to the following notebook:

- [examples/pyagent.ipynb](examples/pyagent.ipynb)

## 📚 Citation

If you find this research useful in your work, please consider citing:

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