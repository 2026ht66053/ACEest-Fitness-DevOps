
# ACEest Fitness & Gym — DevOps Assignment 1

## Project Overview

This project demonstrates a Flask application with automated testing,
Docker containerization, GitHub version control, GitHub Actions CI,
and a Jenkins BUILD job.

## Technology Stack

- Python
- Flask
- Pytest
- Ruff
- Git and GitHub
- Docker
- GitHub Actions
- Jenkins

## Repository Contents

- `app.py` — Flask application and endpoints
- `test_app.py` — Automated unit tests
- `requirements.txt` — Python dependencies
- `Dockerfile` — Docker image build instructions
- `.dockerignore` — Files excluded from Docker build context
- `.github/workflows/main.yml` — GitHub Actions CI workflow

## Local Setup

Clone the repository:

```bash
git clone https://github.com/2026HT66053/ACEest-Fitness-DevOps.git
cd ACEest-Fitness-DevOps
```

Create and activate a virtual environment on Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

Use the address and port printed by the application.
For the Docker configuration, the application listens on port 5000.

## Run Tests Manually

```bash
python -m compileall -q app.py test_app.py
python -m ruff check app.py test_app.py
python -m pytest -v
```

## Docker

Build the image:

```bash
sudo docker build -t aceest-fitness:latest .
```

Run the tests inside the image:

```bash
sudo docker run --rm aceest-fitness:latest python -m pytest -v
```

Run the application:

```bash
sudo docker run -d --name aceest-fitness-container \
  -p 5000:5000 aceest-fitness:latest
```

Check the health endpoint:

```bash
curl http://127.0.0.1:5000/health
```

Stop and remove the container when finished:

```bash
sudo docker stop aceest-fitness-container
sudo docker rm aceest-fitness-container
```

## GitHub Actions Integration

The workflow is stored at `.github/workflows/main.yml`.
It runs on pushes and pull requests.

The pipeline checks out the repository, installs Python dependencies,
compiles the Python files, runs Ruff, executes the unit tests,
builds the Docker image, and runs tests inside the image.

## Jenkins Integration

The Jenkins Freestyle project retrieves the source code from GitHub.
Its build shell step creates a virtual environment, installs dependencies,
compiles the application, runs Ruff, and executes Pytest.

The Jenkins console output is used to verify whether the BUILD succeeds.

## Version Control

Changes are committed with descriptive Git commit messages and pushed
to the `main` branch.

## Conclusion

This project demonstrates source control, automated quality checks,
unit testing, containerization, and a Jenkins BUILD process.
