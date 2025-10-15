"""
Main module for KYUSH Base Environment Documentation.

This module demonstrates a simple Python application that can be used
as a starting point for UV-based projects. It showcases basic functionality
and serves as an example of how to structure a Python package.
"""

import sys
import platform
from typing import Dict, Any


def get_system_info() -> Dict[str, Any]:
    """Get basic system information."""
    return {
        "python_version": sys.version,
        "python_executable": sys.executable,
        "platform": platform.platform(),
        "architecture": platform.architecture(),
        "processor": platform.processor(),
    }


def get_package_info() -> Dict[str, Any]:
    """Get package information."""
    try:
        import pandas as pd
        pandas_version = pd.__version__
    except ImportError:
        pandas_version = "Not installed"
    
    try:
        import numpy as np
        numpy_version = np.__version__
    except ImportError:
        numpy_version = "Not installed"
    
    try:
        import matplotlib
        matplotlib_version = matplotlib.__version__
    except ImportError:
        matplotlib_version = "Not installed"
    
    try:
        import seaborn
        seaborn_version = seaborn.__version__
    except ImportError:
        seaborn_version = "Not installed"
    
    return {
        "pandas": pandas_version,
        "numpy": numpy_version,
        "matplotlib": matplotlib_version,
        "seaborn": seaborn_version,
    }


def main() -> None:
    """Main entry point for the application."""
    print("🚀 KYUSH Base Environment Documentation")
    print("=" * 50)
    print()
    
    print("📋 System Information:")
    system_info = get_system_info()
    for key, value in system_info.items():
        print(f"  {key}: {value}")
    print()
    
    print("📦 Package Information:")
    package_info = get_package_info()
    for package, version in package_info.items():
        status = "✅" if version != "Not installed" else "❌"
        print(f"  {status} {package}: {version}")
    print()
    
    print("🎯 This is your UV-based Python project template!")
    print("   Edit this file to build your application.")
    print()
    print("📚 Next steps:")
    print("   - Check out NEW_UV_PROJECT.md for setup guides")
    print("   - Try the Docker development environment")
    print("   - Add your own dependencies with 'uv add <package>'")
    print("   - Run tests with 'uv run pytest'")


if __name__ == "__main__":
    main()