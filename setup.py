from setuptools import setup, find_packages

setup(
    name="amd-stable-diffusion-server",
    version="0.1.0",
    description="High-throughput Stable Diffusion image generation server optimized for AMD GPUs with ROCm, supporting SDXL, SD3, and ControlNet.",
    author="Developer",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "torch>=2.1.0",
        "numpy>=1.24.0",
        "pyyaml>=6.0",
    ],
)
