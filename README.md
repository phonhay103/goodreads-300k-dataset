# goodreads-300k-dataset

## Pre-requisites
The project was developed using python 3.9 with the following packages.
- numpy
- pandas
- scikit-learn
- gensim
- jupyterlab
- pandas-profiling
- matplotlib
- seaborn
- joblib

Installation with pip:
```bash
pip install -r requirements.txt
```

Installation with [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html):
```bash
conda create -n IT4362 --file requirements.txt python=3.9
```

## Dataset
Download from kaggle: [Goodreads 300K dataset](https://www.kaggle.com/khushdassani/goodreads-300k-dataset)

Download from google drive: [Goodreads 300K dataset](https://drive.google.com/file/d/1GJLByvetYbNofD3kK-0iunYnAYX3MZR4/view?usp=share_link)

## Getting Started
If using conda, activate conda environment
```bash
conda activate IT4362
```

Inference
```bash
python main.py
```

## Using jupyter notebook
Add conda environment to jupyter notebook
```bash
python -m ipykernel install --user --name IT4362
```

Run jupyter notebook
```bash
jupyter-lab
```
