# Python
__pycache__/
*.py[cod]
.venv/
venv/

# Jupyter
.ipynb_checkpoints/

# Local environment variables and secrets
.env
.env.*

# Data files (keep original and processed datasets off GitHub)
data/raw/*
data/processed/*
!data/raw/.gitkeep
!data/processed/.gitkeep

# Generated reports
reports/*
!reports/.gitkeep

# macOS
.DS_Store

# RetailLens

RetailLens is a retail sales analytics project built with Python,
pandas, SQL, and data visualization.

## Goals

- Inspect and validate retail transaction data.
- Identify missing values, duplicates, and invalid records.
- Analyze sales trends, products, and customer purchasing patterns.
- Communicate findings through charts and business recommendations.

## Project Status

Phase 1: Repository setup and project structure.