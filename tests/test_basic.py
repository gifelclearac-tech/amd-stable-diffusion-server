"""
Basic tests for amd-stable-diffusion-server
"""

import pytest

def test_import():
    import src
    assert hasattr(src, "__version__")

def test_version():
    import src
    assert src.__version__ == "0.1.0"
