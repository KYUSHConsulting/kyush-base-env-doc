"""
KYUSH Base Environment Documentation

A comprehensive template and reference project for Python development
with UV package manager, Docker, and data science libraries.
"""

__version__ = "0.1.0"
__author__ = "KYUSH Consulting"
__email__ = "kyush.consulting@gmail.com"

# Make main function available at package level
from .main import main

__all__ = ["main"]