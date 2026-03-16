# Project 1: CI/CD Pipeline for Web Application

## Description
CI/CD pipeline for a simple web application built with Node.js and Python, featuring automated testing and deployment.

## Quick Start

### Manual Testing - Node.js
```bash
cd nodejs-app
npm install
npm test
npm start
# Open http://localhost:3000
```

### Manual Testing - Python
```bash
cd python-app
pip install -r requirements.txt
pytest test_app.py
python app.py
# Open http://localhost:5000
```

## Structure
- `nodejs-app/` - Node.js web application
- `python-app/` - Python web application
- `.github/workflows/` - GitHub Actions workflows
- `jenkins/` - Jenkins pipeline files

## Technologies
- Node.js / Python
- GitHub Actions / Jenkins
- Docker
- Unit Testing

## Usage
1. Push code to the repository
2. GitHub Actions will automatically trigger the pipeline
3. Or use Jenkins for local execution
