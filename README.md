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

## Driver Installation (Ubuntu)

A prebuilt `.deb` package for the Sinus measurement hardware is provided in the `drivers/` directory.
Install it with:

```bash
sudo dpkg -i drivers/sinus-driver-6.2.22-a237b85-noble-amd64.deb
sudo apt-get install -f
```

The first command installs the package; the second resolves and installs any missing dependencies automatically.

> **Note:** This package targets Ubuntu 24.04 (Noble). On other Ubuntu versions, compatibility is not guaranteed.
