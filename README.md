### Setup (Linux)
- Install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`

- Create virtualenv:
```
uv venv --python 3.11 --python-preference only-managed

#If an error has occurred, it is necessary to take the following step: 
export PATH="/home/<yourfolder>/.cargo/bin:${PATH}"
```

- Activate: 
```
source .venv/bin/activate
uv pip install -r pyproject.toml
```
