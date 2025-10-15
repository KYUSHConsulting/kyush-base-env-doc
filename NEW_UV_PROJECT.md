# Complete Guide: Creating a New UV Project with GitHub Repository

This guide walks you through creating a new Python project with `uv` and setting up a GitHub repository from scratch.

This is the **kyush-base-env-doc** reference project - your complete template for Python development with Docker and data science libraries.

## Prerequisites

- [ ] `uv` installed (`pip install uv` or `curl -LsSf https://astral.sh/uv/install.sh | sh`)
- [ ] `git` installed
- [ ] `gh` (GitHub CLI) installed and authenticated
- [ ] GitHub account

## Method 1: Create Local Project First (Recommended)

### Step 1: Create New UV Project
```powershell
# Navigate to your projects directory
cd C:\Users\kjusz\!Projects

# Create new project with uv (includes git initialization)
uv init kyush-base-env-doc --git

# Navigate into the project
cd kyush-base-env-doc
```

### Step 2: Set Up Project Structure
```powershell
# Check what uv created
ls

# You should see:
# - README.md
# - pyproject.toml
# - .gitignore
# - .git/ (hidden folder)
# - src/my_new_project/ (source code directory)
```

### Step 3: Customize Your Project
```powershell
# Edit README.md with project description
code README.md

# Add dependencies if needed
uv add requests pandas  # Example dependencies

# Create your main application code
code src/my_new_project/__init__.py
code src/my_new_project/main.py
```

### Step 4: Make Initial Commit
```powershell
# Check git status
git status

# Add all files
git add .

# Make initial commit
git commit -m "Initial commit: Set up project with uv"
```

### Step 5: Create GitHub Repository and Push
```powershell
# Create GitHub repo and push in one command
gh repo create kyush-base-env-doc --public --source=. --remote=origin --push

# Alternative: Create private repo
# gh repo create kyush-base-env-doc --private --source=. --remote=origin --push
```

### Step 6: Verify Setup
```powershell
# Check remote connection
git remote -v

# Check GitHub repo (opens in browser)
gh repo view --web
```

## Method 2: Create GitHub Repository First

### Step 1: Create GitHub Repository
```powershell
# Create and clone GitHub repo
gh repo create kyush-base-env-doc --public --clone

# Navigate into cloned directory
cd kyush-base-env-doc
```

### Step 2: Initialize UV Project
```powershell
# Initialize uv in existing directory
uv init .

# This creates pyproject.toml and basic structure
```

### Step 3: Set Up Project
```powershell
# Add dependencies
uv add requests pandas

# Create source code
mkdir src/my_new_project
code src/my_new_project/__init__.py
code src/my_new_project/main.py

# Edit README
code README.md
```

### Step 4: Commit and Push
```powershell
# Add and commit
git add .
git commit -m "Initialize uv project structure"

# Push to GitHub
git push
```

## Method 3: Quick One-Liner Setup

For experienced users, combine everything:

```powershell
# Create project, initialize git, commit, and create GitHub repo
uv init kyush-base-env-doc --git && cd kyush-base-env-doc && git add . && git commit -m "Initial commit" && gh repo create kyush-base-env-doc --public --source=. --remote=origin --push
```

## Method 4: Docker-Based Development Environment

This method creates a containerized development environment using Docker, which ensures consistency across different systems and isolates your project dependencies.

### Prerequisites for Docker Method
- [ ] Docker Desktop installed and running
- [ ] Basic understanding of Docker concepts
- [ ] All previous prerequisites (uv, git, gh)

### Step 1: Create Project Structure
```powershell
# Navigate to your projects directory
cd C:\Users\kjusz\!Projects

# Create new project with uv
uv init kyush-base-env-doc --git
cd kyush-base-env-doc
```

### Step 2: Create Docker Configuration Files

#### Create Dockerfile
```powershell
# Create Dockerfile
code Dockerfile
```

**Option A: Ubuntu 22.04 LTS (Recommended for Ubuntu preference)**
Add this content to `Dockerfile`:
```dockerfile
# Use Ubuntu 22.04 LTS as base image
FROM ubuntu:22.04

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV UV_CACHE_DIR=/tmp/uv-cache
ENV DEBIAN_FRONTEND=noninteractive

# Set work directory
WORKDIR /app

# Install system dependencies including Python 3.12
RUN apt-get update && apt-get install -y \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update && apt-get install -y \
    python3.12 \
    python3.12-dev \
    python3.12-venv \
    python3-pip \
    git \
    curl \
    wget \
    build-essential \
    gcc \
    g++ \
    make \
    vim \
    nano \
    htop \
    tree \
    unzip \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create symlinks for python and pip
RUN ln -sf /usr/bin/python3.12 /usr/bin/python && \
    ln -sf /usr/bin/python3.12 /usr/bin/python3

# Install pip for Python 3.12
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12

# Install uv
RUN pip install uv

# Install common data science libraries globally
RUN pip install \
    pandas \
    numpy \
    scikit-learn \
    matplotlib \
    seaborn \
    jupyter \
    ipykernel \
    plotly \
    requests \
    python-dotenv

# Copy project files
COPY pyproject.toml ./
COPY uv.lock* ./

# Install Python dependencies
RUN uv sync --frozen

# Copy source code
COPY . .

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash appuser && \
    chown -R appuser:appuser /app
USER appuser

# Expose port (adjust as needed)
EXPOSE 8000

# Default command
CMD ["uv", "run", "python", "src/my_new_project/main.py"]
```

**Option B: Debian-based (Smaller size, faster builds)**
Alternative `Dockerfile` content:
```dockerfile
# Use official Python runtime as base image (Debian-based)
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV UV_CACHE_DIR=/tmp/uv-cache

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Copy project files
COPY pyproject.toml ./
COPY uv.lock* ./

# Install Python dependencies
RUN uv sync --frozen

# Copy source code
COPY . .

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash appuser && \
    chown -R appuser:appuser /app
USER appuser

# Expose port (adjust as needed)
EXPOSE 8000

# Default command
CMD ["uv", "run", "python", "src/my_new_project/main.py"]
```

**Linux Distribution Comparison:**

| Feature | Ubuntu 22.04 | Debian Slim |
|---------|--------------|-------------|
| **Base OS** | Ubuntu 22.04 LTS | Debian 12 (Bookworm) |
| **Image Size** | ~150MB | ~80MB |
| **Package Manager** | apt (same as Debian) | apt |
| **Python Installation** | Manual via deadsnakes PPA | Pre-installed |
| **Additional Tools** | More utilities included | Minimal installation |
| **Familiarity** | More familiar to most devs | Lighter, Docker-optimized |
| **Long-term Support** | Until 2027 | Rolling updates |

#### Create docker-compose.yml
```powershell
# Create docker-compose file
code docker-compose.yml
```

Add this content to `docker-compose.yml`:
```yaml
version: '3.8'

services:
  app:
    build: .
    container_name: kyush-base-env-doc-app
    volumes:
      # Mount source code for development
      - .:/app
      # Mount uv cache to speed up builds
      - uv-cache:/tmp/uv-cache
    ports:
      - "8000:8000"
    environment:
      - PYTHONPATH=/app/src
    # Override default command for development
    command: tail -f /dev/null
    stdin_open: true
    tty: true

  # Optional: Add database service
  db:
    image: postgres:15
    container_name: kyush-base-env-doc-db
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  uv-cache:
  postgres_data:
```

#### Create .dockerignore
```powershell
# Create .dockerignore
code .dockerignore
```

Add this content to `.dockerignore`:
```
.git
.gitignore
README.md
.venv
__pycache__
*.pyc
*.pyo
*.pyd
.pytest_cache
.coverage
.mypy_cache
node_modules
.DS_Store
Thumbs.db
```

#### Create Docker development script
```powershell
# Create development helper script
code docker-dev.ps1
```

Add this content to `docker-dev.ps1`:
```powershell
# Docker Development Helper Script

param(
    [Parameter(Position=0)]
    [string]$Command = "help"
)

switch ($Command) {
    "build" {
        Write-Host "Building Docker image..." -ForegroundColor Green
        docker-compose build
    }
    "up" {
        Write-Host "Starting development environment..." -ForegroundColor Green
        docker-compose up -d
        Write-Host "Environment started. Use 'docker-dev shell' to access container." -ForegroundColor Yellow
    }
    "down" {
        Write-Host "Stopping development environment..." -ForegroundColor Red
        docker-compose down
    }
    "shell" {
        Write-Host "Entering container shell..." -ForegroundColor Blue
        docker-compose exec app bash
    }
    "ubuntu" {
        Write-Host "Checking Ubuntu system information..." -ForegroundColor Cyan
        docker-compose exec app bash -c "lsb_release -a && uname -a"
    }
    "system" {
        Write-Host "System information and installed packages..." -ForegroundColor Cyan
        docker-compose exec app bash -c "
            echo '=== Ubuntu Version ==='
            lsb_release -a
            echo '=== Python Version ==='
            python --version
            echo '=== Data Science Libraries ==='
            python -c 'import pandas as pd; print(f\"pandas: {pd.__version__}\")'
            python -c 'import numpy as np; print(f\"numpy: {np.__version__}\")'
            python -c 'import sklearn; print(f\"scikit-learn: {sklearn.__version__}\")'
            python -c 'import matplotlib; print(f\"matplotlib: {matplotlib.__version__}\")'
            python -c 'import seaborn as sns; print(f\"seaborn: {sns.__version__}\")'
            echo '=== UV Status ==='
            uv --version
            echo '=== Python packages ==='
            uv pip list
        "
    }
    "datascience" {
        Write-Host "Testing data science libraries..." -ForegroundColor Green
        docker-compose exec app python -c "
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification

print('✅ All data science libraries imported successfully!')
print(f'📊 pandas: {pd.__version__}')
print(f'🔢 numpy: {np.__version__}')
print(f'📈 matplotlib: {plt.matplotlib.__version__}')
print(f'🎨 seaborn: {sns.__version__}')
print('🤖 scikit-learn: imported successfully')

# Quick test
df = pd.DataFrame({'x': np.random.randn(10), 'y': np.random.randn(10)})
print(f'📋 Sample DataFrame shape: {df.shape}')
print('🎉 Data science environment ready!')
        "
    }
    "logs" {
        docker-compose logs -f app
    }
    "test" {
        Write-Host "Running tests in container..." -ForegroundColor Cyan
        docker-compose exec app uv run pytest
    }
    "install" {
        Write-Host "Installing dependencies in container..." -ForegroundColor Magenta
        docker-compose exec app uv sync
    }
    "add" {
        if ($args.Count -eq 0) {
            Write-Host "Usage: docker-dev add <package-name>" -ForegroundColor Red
            exit 1
        }
        Write-Host "Adding package: $($args[0])" -ForegroundColor Magenta
        docker-compose exec app uv add $args[0]
    }
    "clean" {
        Write-Host "Cleaning up Docker resources..." -ForegroundColor Red
        docker-compose down -v
        docker system prune -f
    }
    "rebuild" {
        Write-Host "Rebuilding containers..." -ForegroundColor Yellow
        docker-compose down
        docker-compose build --no-cache
        docker-compose up -d
    }
    default {
        Write-Host @"
Docker Development Commands:

  build       - Build Docker image
  up          - Start development environment
  down        - Stop development environment
  shell       - Enter container shell
  ubuntu      - Check Ubuntu version and system info
  system      - Show detailed system information
  datascience - Test data science libraries installation
  logs        - View container logs
  test        - Run tests in container
  install     - Install dependencies
  add         - Add new package (e.g., docker-dev add requests)
  clean       - Clean up Docker resources
  rebuild     - Rebuild containers from scratch

Usage: .\docker-dev.ps1 <command>
"@ -ForegroundColor White
    }
}
```

### Step 3: Set Up Project Code

#### Update main.py for Docker
```powershell
# Create or update main application
code src/my_new_project/main.py
```

Add this sample content:
```python
"""
Main application module.
Data science enabled FastAPI application running in Ubuntu Docker container.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse
import json
import base64
from io import BytesIO

app = FastAPI(
    title="KYUSH Base Environment Documentation",
    description="A FastAPI application with data science libraries running in Ubuntu Docker",
    version="1.0.0"
)

@app.get("/")
async def root():
    """Root endpoint with library versions."""
    return {
        "message": "Hello from Ubuntu Docker with Data Science!",
        "environment": os.environ.get("ENVIRONMENT", "development"),
        "python_version": os.environ.get("PYTHON_VERSION", "unknown"),
        "libraries": {
            "pandas": pd.__version__,
            "numpy": np.__version__,
            "matplotlib": plt.matplotlib.__version__,
            "seaborn": sns.__version__,
            "scikit-learn": "installed"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return JSONResponse(
        status_code=200,
        content={"status": "healthy", "service": "kyush-base-env-doc"}
    )

@app.get("/demo/data")
async def create_sample_data():
    """Create and return sample dataset."""
    # Generate sample data
    X, y = make_classification(
        n_samples=1000, 
        n_features=20, 
        n_informative=10, 
        n_redundant=10, 
        random_state=42
    )
    
    # Create DataFrame
    df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])
    df['target'] = y
    
    # Basic statistics
    stats = {
        "shape": df.shape,
        "columns": list(df.columns),
        "target_distribution": df['target'].value_counts().to_dict(),
        "feature_stats": df.describe().to_dict()
    }
    
    return JSONResponse(content=stats)

@app.get("/demo/model")
async def train_model():
    """Train a simple model and return results."""
    # Generate data
    X, y = make_classification(
        n_samples=1000, 
        n_features=20, 
        n_informative=10, 
        n_redundant=10, 
        random_state=42
    )
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    return {
        "model": "Random Forest Classifier",
        "training_samples": len(X_train),
        "test_samples": len(X_test),
        "accuracy": float(accuracy),
        "feature_importance": model.feature_importances_.tolist()[:10]  # Top 10
    }

@app.get("/demo/plot", response_class=HTMLResponse)
async def create_plot():
    """Create a sample plot and return as HTML."""
    # Set style for better plots
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    
    # Generate sample data
    np.random.seed(42)
    data = {
        'x': np.random.randn(100),
        'y': np.random.randn(100),
        'category': np.random.choice(['A', 'B', 'C'], 100)
    }
    df = pd.DataFrame(data)
    
    # Create plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Scatter plot
    sns.scatterplot(data=df, x='x', y='y', hue='category', ax=ax1)
    ax1.set_title('Sample Scatter Plot')
    
    # Distribution plot
    sns.histplot(data=df, x='x', hue='category', ax=ax2, alpha=0.7)
    ax2.set_title('Sample Distribution')
    
    plt.tight_layout()
    
    # Convert plot to base64 string
    buffer = BytesIO()
    plt.savefig(buffer, format='png', dpi=150, bbox_inches='tight')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    
    # Return HTML with embedded plot
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Data Science Demo Plot</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .container {{ text-align: center; }}
            img {{ max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Data Science Demo - Ubuntu Docker Container</h1>
            <p>Generated using matplotlib and seaborn in Ubuntu Linux container</p>
            <img src="data:image/png;base64,{plot_data}" alt="Sample Plot">
            <p><a href="/demo/data">View Sample Data</a> | <a href="/demo/model">Train Model</a></p>
        </div>
    </body>
    </html>
    """
    
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_dirs=["src"]
    )
```

#### Update pyproject.toml for Docker
```powershell
# Add web dependencies
uv add fastapi uvicorn[standard]

# Add data science dependencies
uv add pandas numpy scikit-learn matplotlib seaborn jupyter plotly

# Add development dependencies
uv add --dev pytest httpx black mypy ruff
```

### Step 4: Build and Start Docker Environment

#### Build the Docker image
```powershell
# Make the PowerShell script executable
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Build Docker image
.\docker-dev.ps1 build
```

#### Start the development environment
```powershell
# Start containers
.\docker-dev.ps1 up

# Check if containers are running
docker-compose ps
```

### Step 5: Develop Inside Docker Container

#### Access the container shell
```powershell
# Enter container for development
.\docker-dev.ps1 shell

# Inside container, you can run:
# uv run python src/my_new_project/main.py
# uv run pytest
# uv add new-package
```

#### Alternative: Use VS Code with Docker
```powershell
# Install VS Code Docker extension
code --install-extension ms-vscode-remote.remote-containers

# Open project in VS Code
code .

# Use Command Palette (Ctrl+Shift+P): 
# "Dev Containers: Reopen in Container"
```

### Step 6: Test Your Docker Setup

#### Run the application
```powershell
# Start the web server in container
docker-compose exec app uv run python src/my_new_project/main.py

# Or use the helper script
.\docker-dev.ps1 shell
# Then inside container: uv run uvicorn src.my_new_project.main:app --host 0.0.0.0 --port 8000 --reload
```

#### Test the endpoints
```powershell
# In another terminal, test the API
curl http://localhost:8000
curl http://localhost:8000/health

# Test data science endpoints
curl http://localhost:8000/demo/data
curl http://localhost:8000/demo/model

# Or open in browser to see the plot
Start-Process "http://localhost:8000"
Start-Process "http://localhost:8000/demo/plot"
```

### Step 7: Add Docker Files to Git

#### Update .gitignore for Docker
```powershell
# Edit .gitignore to include Docker-specific ignores
code .gitignore
```

Add these Docker-related entries:
```gitignore
# Docker
.dockerignore
docker-compose.override.yml

# Database
*.db
*.sqlite
*.sqlite3

# Logs
logs/
*.log
```

#### Commit Docker configuration
```powershell
# Add all new files
git add .

# Commit Docker setup
git commit -m "Add Docker development environment

- Add Dockerfile with Python 3.12
- Add docker-compose.yml with app and database services
- Add docker-dev.ps1 helper script
- Add sample FastAPI application
- Update dependencies for web development"
```

### Step 8: Create GitHub Repository
```powershell
# Create GitHub repo and push (same as other methods)
gh repo create my-new-project --public --source=. --remote=origin --push
```

### Step 9: Document Docker Usage

#### Update README.md
```powershell
code README.md
```

Add Docker section to your README:
```markdown
## Docker Development

This project includes Docker configuration for consistent development environments.

### Quick Start with Docker

1. **Build and start the environment:**
   ```bash
   .\docker-dev.ps1 build
   .\docker-dev.ps1 up
   ```

2. **Access the application:**
   - Web interface: http://localhost:8000
   - API docs: http://localhost:8000/docs

3. **Development workflow:**
   ```bash
   # Enter container shell
   .\docker-dev.ps1 shell
   
   # Add new packages
   .\docker-dev.ps1 add requests
   
   # Run tests
   .\docker-dev.ps1 test
   
   # View logs
   .\docker-dev.ps1 logs
   ```

4. **Stop the environment:**
   ```bash
   .\docker-dev.ps1 down
   ```

### Docker Commands Reference

See `.\docker-dev.ps1 help` for all available commands.
```

### Docker Development Workflow

#### Daily Development Commands
```powershell
# Start your development day
.\docker-dev.ps1 up

# Develop in container
.\docker-dev.ps1 shell

# Add new dependencies
.\docker-dev.ps1 add pandas numpy

# Run tests
.\docker-dev.ps1 test

# Check logs
.\docker-dev.ps1 logs

# End your development day
.\docker-dev.ps1 down
```

#### Production Deployment
```powershell
# Build production image
docker build -t my-new-project:latest .

# Run production container
docker run -d \
  --name my-new-project-prod \
  -p 8000:8000 \
  -e ENVIRONMENT=production \
  my-new-project:latest
```

### Benefits of Docker Method

✅ **Consistent Environment**: Same Python version and dependencies everywhere  
✅ **Isolation**: No conflicts with system Python or other projects  
✅ **Easy Onboarding**: New team members just need Docker  
✅ **Production Parity**: Development environment matches production  
✅ **Database Integration**: Easy to add databases and other services  
✅ **VS Code Integration**: Full IDE support with Dev Containers  
✅ **CI/CD Ready**: Docker images work great in deployment pipelines  

### Troubleshooting Docker Setup

1. **Docker not running**:
   ```powershell
   # Start Docker Desktop
   Start-Process "Docker Desktop"
   ```

2. **Port already in use**:
   ```powershell
   # Check what's using the port
   netstat -ano | findstr :8000
   # Kill the process or change port in docker-compose.yml
   ```

3. **Permission issues**:
   ```powershell
   # Run PowerShell as Administrator
   # Or adjust ExecutionPolicy
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

4. **Container won't start**:
   ```powershell
   # Check container logs
   docker-compose logs app
   
   # Rebuild without cache
   .\docker-dev.ps1 rebuild
   ```

5. **Dependencies not updating**:
   ```powershell
   # Force rebuild
   .\docker-dev.ps1 rebuild
   
   # Or manually sync
   .\docker-dev.ps1 install
   ```

## Common UV Commands for Your Project

### Development Workflow
```powershell
# Add new dependencies
uv add package-name

# Add development dependencies
uv add --dev pytest black mypy

# Install dependencies (when cloning existing project)
uv sync

# Run your application
uv run python src/my_new_project/main.py

# Run with specific Python version
uv run --python 3.12 python src/my_new_project/main.py

# Run tests
uv run pytest

# Format code
uv run black .

# Type checking
uv run mypy src/
```

### Virtual Environment Management
```powershell
# Activate virtual environment
uv venv
.venv\Scripts\activate  # Windows PowerShell

# Or use uv directly (recommended)
uv run python --version
uv run pip list
```

## GitHub Workflow Commands

### Daily Development
```powershell
# Check status
git status

# Add changes
git add .
# or add specific files
git add src/my_new_project/main.py

# Commit changes
git commit -m "Add new feature: description"

# Push to GitHub
git push
```

### Branch Management
```powershell
# Create new branch
git checkout -b feature/new-feature

# Push new branch to GitHub
git push -u origin feature/new-feature

# Create pull request
gh pr create --title "New Feature" --body "Description of changes"

# Switch back to main
git checkout main

# Pull latest changes
git pull
```

### Repository Management
```powershell
# View repository info
gh repo view

# Open repository in browser
gh repo view --web

# Clone existing repository
gh repo clone username/repository-name

# List your repositories
gh repo list
```

## Project Structure Template

After running the commands, your project should look like this:

```
kyush-base-env-doc/
├── .git/                 # Git repository data
├── .gitignore           # Git ignore rules
├── README.md            # Project documentation
├── pyproject.toml       # UV/Python project configuration
├── .venv/               # Virtual environment (created by uv)
└── src/
    └── kyush_base_env_doc/
        ├── __init__.py  # Package initialization
        └── main.py      # Main application code
```

## Troubleshooting

### Common Issues and Solutions

1. **uv not found**:
   ```powershell
   # Install uv
   pip install uv
   ```

2. **gh not found**:
   ```powershell
   # Install GitHub CLI
   winget install GitHub.cli
   # Refresh PATH
   $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
   ```

3. **Not authenticated with GitHub**:
   ```powershell
   gh auth login
   ```

4. **Permission denied (publickey)**:
   ```powershell
   # Use HTTPS instead of SSH
   git remote set-url origin https://github.com/username/repository-name.git
   ```

5. **Repository already exists**:
   ```powershell
   # Add existing repo as remote
   git remote add origin https://github.com/username/repository-name.git
   git push -u origin main
   ```

## Best Practices

1. **Always use meaningful commit messages**
2. **Create `.gitignore` appropriate for Python projects** (uv does this automatically)
3. **Use semantic versioning** in your `pyproject.toml`
4. **Write good README.md** with installation and usage instructions
5. **Add tests** from the beginning with `uv add --dev pytest`
6. **Use branches** for features and bug fixes
7. **Create pull requests** for code review

## Next Steps

After setting up your project:

1. **Add project description** to README.md
2. **Set up continuous integration** with GitHub Actions
3. **Add tests** and set up test automation
4. **Configure code formatting** with Black and linting with Ruff
5. **Set up documentation** with Sphinx or MkDocs
6. **Add badges** to README for build status, coverage, etc.

---

**Happy coding!** 🚀

This guide should get you from zero to a fully functional Python project with GitHub integration in just a few minutes.