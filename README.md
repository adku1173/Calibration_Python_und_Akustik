# Calibration_Python_und_Akustik

## Setup with uv

Install `uv` if it is not already available:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Create the virtual environment and install the dependencies:

```bash
uv venv
uv sync
```

Run the notebook:

```bash
uv run jupyter notebook calibration.ipynb
```

As an alternative, the environment can also be created with `conda`, `mamba`,
or `micromamba`, but dependency resolution is usually slower than with `uv`.
