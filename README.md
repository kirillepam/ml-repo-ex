# Get started
```bash
conda deactivate
conda env remove -n dev-ml-repo-ex
conda env create -f envs/environment-local-dev.yml
conda activate dev-ml-repo-ex
pre-commit install
dvc init
dvc add data/data-v1.txt
dvc status
dvc checkout
python -m ml_repo_ex.train
```

# Testing
1. pytest
    ```bash
    pytest -v .
    coverage run -m pytest -v
    coverage report
    coverage html
    ```
2. [safety](https://github.com/pyupio/safety)
    ```bash
    safety check
    ```
