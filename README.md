# CI/CD Final Project — Counter REST API

**Owner:** Shreyaslad99  
**Course:** IBM Continuous Integration and Continuous Delivery (CI/CD) Final Project

This repository contains a small Flask REST API and example Continuous Integration / Continuous Delivery configuration. The CI workflow installs dependencies, runs `flake8`, and runs unit tests with `nose`. The Tekton task definitions cover cleanup, source checkout, linting, unit tests, image build, and OpenShift deployment.

> Adapted as a learning implementation using the publicly available project structure at [christian-schw/ci-cd-final-project](https://github.com/christian-schw/ci-cd-final-project) and the IBM developer-skills-network CI/CD project template. See upstream license/attribution before redistributing copied files. Do not represent sample logs or screenshots as evidence from a real run.

## Project details

- **Project name:** CI/CD Final Project — Counter REST API
- **Goal:** automate linting and tests, build a container image, and deploy to OpenShift using Tekton
- **Application:** Python 3.9, Flask, Gunicorn
- **Continuous integration:** GitHub Actions
- **Continuous delivery:** Tekton / OpenShift Pipelines
- **Unit testing:** nose
- **Linting:** flake8

## API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API information |
| GET | `/health` | Health status |
| GET | `/counters` | List counters |
| POST | `/counters/{name}` | Create a counter |
| GET | `/counters/{name}` | Read a counter |
| PUT | `/counters/{name}` | Increment a counter |
| DELETE | `/counters/{name}` | Delete a counter |

## Run locally

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
nosetests -v
```

Run the service on port 8000:

```bash
gunicorn service:app --bind 0.0.0.0:8000
```

Check `http://127.0.0.1:8000/health`.

## CI workflow

The workflow is `.github/workflows/workflow.yml`. On pushes and pull requests to `main`, it checks out the code, installs Python and Node runtimes, installs dependencies, runs flake8, and runs nose tests. View real run output from the repository's **Actions** tab after you push this project to your own public repository.

## Tekton / OpenShift

- `.tekton/tasks.yml` defines `cleanup`, `flake8`, and `nose` tasks.
- `.tekton/pipeline.yml` wires together `cleanup`, `git-clone`, lint, tests, `buildah`, and `openshift-client` deployment tasks.
- Cluster tasks such as `git-clone`, `buildah`, and `openshift-client` must already be installed and supported by the target OpenShift Pipelines cluster. Update image registry, repository URL, namespace, and deployment settings for your environment before running it.

The pipeline is a configuration template; it does not prove that your OpenShift deployment has run. Capture your own screenshots and logs from the actual cluster.

## Evidence checklist

See [`submission/EVIDENCE_CHECKLIST.md`](submission/EVIDENCE_CHECKLIST.md). Store only genuine logs/screenshots from your own GitHub Actions and OpenShift executions.
