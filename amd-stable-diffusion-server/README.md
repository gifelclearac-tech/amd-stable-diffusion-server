# Amd Stable Diffusion Server

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![ROCm 6.x](https://img.shields.io/badge/ROCm-6.x-orange.svg)](https://rocm.docs.amd.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-ee4c2c.svg)](https://pytorch.org/)

High-throughput Stable Diffusion image generation server optimized for AMD GPUs with ROCm, supporting SDXL, SD3, and ControlNet.

---

## Features

- **SDXL, SD 3.0, and SDXL-Turbo support**
- **ControlNet and IP-Adapter integration**
- **ROCm-optimized attention kernels**
- **Dynamic batching for multiple requests**
- **INT8 quantization for faster inference**
- **FastAPI REST + WebSocket streaming**
- **Image-to-image, inpainting, img2img**
- **Prometheus metrics and health checks**

---

## Requirements

- **GPU**: AMD Instinct MI250X, MI300X, or compatible CDNA GPU
- **OS**: Ubuntu 22.04 / 24.04
- **ROCm**: 6.1+
- **Python**: 3.10+

---

## Installation

```bash
git clone https://github.com/user/amd-stable-diffusion-server.git
cd amd-stable-diffusion-server
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

---

## Quick Start

```bash
# Run training
python -m src.train --config configs/default.yaml

# Run inference
python -m src.inference --model checkpoints/best.pt --input data/sample
```

---

## Project Structure

```
amd-stable-diffusion-server/
├── README.md
├── LICENSE
├── requirements.txt
├── setup.py
├── configs/
│   └── default.yaml
├── src/
│   ├── __init__.py
│   ├── train.py
│   └── inference.py
├── tests/
│   └── test_basic.py
└── docs/
    └── architecture.md
```

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

*Built for the AMD GPU ecosystem. Not affiliated with or endorsed by AMD.*
