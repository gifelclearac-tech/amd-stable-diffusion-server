"""
amd-stable-diffusion-server - Training Pipeline
Optimized for AMD Instinct GPUs via ROCm/HIP
"""

import argparse
import yaml
import torch
from pathlib import Path


def load_config(config_path: str) -> dict:
    with open(config_path) as f:
        return yaml.safe_load(f)


def train(config: dict):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Training on: {device}")
    if torch.cuda.is_available():
        print(f"GPU: {torch.cuda.get_device_name(0)}")
        print(f"ROCm: {getattr(torch.version, 'hip', 'N/A')}")
    
    # TODO: Implement training loop
    print("Training pipeline initialized.")
    print(f"Config: {config}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True)
    args = parser.parse_args()
    config = load_config(args.config)
    train(config)
