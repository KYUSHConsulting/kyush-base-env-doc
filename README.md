# KYUSH Base Environment Documentation

🚀 **Complete reference project for Python development with UV, Docker, and Data Science libraries**

This repository serves as a comprehensive template and reference guide for setting up modern Python development environments using UV package manager, Docker containerization, and GitHub integration.

## 📋 What's Included

### Development Methods
- **Method 1**: Local UV project with GitHub integration
- **Method 2**: GitHub-first approach with UV initialization  
- **Method 3**: Quick one-liner setup for experienced users
- **Method 4**: Complete Docker-based development environment with Ubuntu 22.04

### Pre-configured Environment
- **🐧 Ubuntu 22.04 LTS** Docker container
- **🐍 Python 3.12** with UV package manager
- **📊 Data Science Stack**: pandas, numpy, scikit-learn, matplotlib, seaborn
- **🌐 Web Framework**: FastAPI with sample endpoints
- **🔧 Development Tools**: pytest, black, mypy, ruff
- **📓 Jupyter Support**: jupyter, ipykernel for notebook development

### Sample Applications
- **REST API** with health checks and system info
- **Data Science Demos**: dataset generation, model training, visualization
- **Interactive Plots**: matplotlib/seaborn charts served via web interface

## 🚀 Quick Start

### Option 1: Use This Template
```bash
# Clone this repository as your starting point
gh repo clone KYUSHConsulting/kyush-base-env-doc my-new-project
cd my-new-project

# Build and start Docker environment
.\docker-dev.ps1 build
.\docker-dev.ps1 up

# Test the environment
.\docker-dev.ps1 datascience
```

### Option 2: Follow the Complete Guide
See [`NEW_UV_PROJECT.md`](./NEW_UV_PROJECT.md) for detailed step-by-step instructions.

## 🐳 Docker Development

This project includes a complete Docker development environment:

```bash
# Build and start
.\docker-dev.ps1 build
.\docker-dev.ps1 up

# Access container shell
.\docker-dev.ps1 shell

# Test data science libraries
.\docker-dev.ps1 datascience

# View web interface
# Open http://localhost:8000/demo/plot
```

## 📚 Documentation Structure

- **`NEW_UV_PROJECT.md`** - Complete setup guide (main documentation)
- **`README.md`** - This file (project overview)
- **`Dockerfile`** - Ubuntu 22.04 with Python 3.12 and data science stack
- **`docker-compose.yml`** - Multi-service development environment
- **`docker-dev.ps1`** - PowerShell helper script for Docker commands

## 🎯 Use Cases

This template is perfect for:
- **Data Science Projects** - Pre-installed ML/analytics libraries
- **Web API Development** - FastAPI with sample endpoints
- **Educational Projects** - Complete learning environment
- **Team Development** - Consistent Docker-based setup
- **Reference Documentation** - Step-by-step guides for future projects

## 🔧 Technologies

- **UV** - Fast Python package manager
- **Docker** - Containerized development environment  
- **GitHub CLI** - Repository management and authentication
- **FastAPI** - Modern web framework for APIs
- **Ubuntu 22.04** - Long-term support Linux distribution
- **Data Science Stack** - pandas, numpy, scikit-learn, matplotlib, seaborn

## 📖 Getting Started

1. **Read the guide**: Start with [`NEW_UV_PROJECT.md`](./NEW_UV_PROJECT.md)
2. **Choose your method**: Local development, Docker, or GitHub-first approach
3. **Follow the steps**: Detailed instructions for each approach
4. **Customize**: Adapt the template for your specific needs

## 🤝 Contributing

This is a reference project. Feel free to:
- Fork it for your own use
- Suggest improvements via issues
- Share your customizations

## 📝 License

This project is intended as a reference and template. Use it freely for your projects.

---

**Created by KYUSH Consulting** - Your complete Python development environment template! 🚀