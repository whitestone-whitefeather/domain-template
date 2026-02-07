
# Domain Template

Standard project scaffold for domain repos (communities, internal departments, clients, programs).

## Structure

```
src/
tests/
notebooks/
pipelines/
config/
  dev/
  test/
  prod/
docs/
.vscode/
.devcontainer/
.github/workflows/
```

## Getting Started
1. Create a virtual environment: `python -m venv .venv && source .venv/bin/activate`
2. Install deps: `pip install -r requirements.txt`
3. Run tests: `pytest -q`
4. Open in VS Code: `code .`
