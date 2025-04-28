# Simple Flask App CI/CD Pipeline with GitHub Actions & Docker

## Objective

This repository demonstrates a basic Continuous Integration and Continuous Deployment (CI/CD) pipeline for a Python Flask application using GitHub Actions and Docker. The pipeline automatically builds a Docker image, pushes it to Docker Hub upon changes to the `main` branch, and provides instructions for deploying the application locally using Docker or Minikube.

## Features

* **Simple Flask Application:** A basic web server (`app.py`).
* **Dockerization:** `Dockerfile` to containerize the application.
* **Local Development:** `docker-compose.yml` for easy local testing.
* **CI/CD Automation:** GitHub Actions workflow (`.github/workflows/main.yml`) for:
    * Checking out code.
    * Setting up Docker Buildx.
    * Logging into Docker Hub (using secrets).
    * Building the Docker image.
    * Pushing the image to Docker Hub (tagged with `latest` and Git SHA).
* **Local Deployment:** Instructions for running the containerized application using Docker directly or via Minikube.

## Prerequisites

* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/get-started)
* [Docker Hub](https://hub.docker.com/) account
* [GitHub](https://github.com/) account
* (Optional) [Minikube](https://minikube.sigs.k8s.io/docs/start/) for Kubernetes deployment

## Project Structure

.

├── .github/

│   └── workflows/

│       └── main.yml      # GitHub Actions CI/CD workflow

├── app.py                # Simple Flask application

├── Dockerfile            # Docker image build instructions

├── docker-compose.yml    # Local development setup

├── requirements.txt      # Python dependencies

└── README.md 

## Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd <repository-directory>
    ```
2.  **Configure GitHub Secrets:**
    * Go to your repository's `Settings` -> `Secrets and variables` -> `Actions`.
    * Add the following repository secrets:
        * `DOCKERHUB_USERNAME`: Your Docker Hub username.
        * `DOCKERHUB_TOKEN`: Your Docker Hub Access Token (create one in Docker Hub settings).
3.  **Update Workflow:**
    * Edit `.github/workflows/main.yml`.
    * Replace `your-dockerhub-username` in the `tags:` line with your actual Docker Hub username.
4.  **Commit and Push:**
    * Commit any changes and push to the `main` branch on GitHub.
    ```bash
    git add .
    git commit -m "Configure CI/CD pipeline"
    git push origin main
    ```
    * This will trigger the GitHub Actions workflow.

## Running the Application Locally

Ensure Docker Desktop or Docker Engine is running.

**Option A: Using Docker Run**

1.  **Pull the image** (replace `your-dockerhub-username`):
    ```bash
    docker pull your-dockerhub-username/my-flask-app:latest
    ```
2.  **Run the container:**
    ```bash
    docker run -d -p 8080:5000 --name my-running-app your-dockerhub-username/my-flask-app:latest
    ```
3.  Access the app at `http://localhost:8080`.
4.  **Stop and remove:**
    ```bash
    docker stop my-running-app
    docker rm my-running-app
    ```

**Option B: Using Minikube**

1.  **Start Minikube:**
    ```bash
    minikube start
    ```
2.  **Create Kubernetes Resources:** Create `deployment.yaml` and `service.yaml` files as described in the [CI/CD Pipeline Guide](link-to-guide-or-keep-inline-if-preferred). **Remember to replace `your-dockerhub-username` in `deployment.yaml`**.
    * Example `deployment.yaml` (condensed):
        ```yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: my-flask-app-deployment
        spec:
          replicas: 1
          selector: { matchLabels: { app: my-flask-app } }
          template:
            metadata: { labels: { app: my-flask-app } }
            spec:
              containers:
              - name: my-flask-container
                image: your-dockerhub-username/my-flask-app:latest # <-- UPDATE THIS
                ports: [{ containerPort: 5000 }]
        ```
    * Example `service.yaml` (condensed):
        ```yaml
        apiVersion: v1
        kind: Service
        metadata:
          name: my-flask-app-service
        spec:
          type: NodePort
          selector: { app: my-flask-app }
          ports: [{ port: 5000, targetPort: 5000 }]
        ```
3.  **Apply the configurations:**
    ```bash
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    ```
4.  **Get the service URL:**
    ```bash
    minikube service my-flask-app-service --url
    ```
    Open the provided URL in your browser.
5.  **Clean up:**
    ```bash
    kubectl delete service my-flask-app-service
    kubectl delete deployment my-flask-app-deployment
    minikube stop
    ```

## Workflow Details

* The CI/CD pipeline is defined in `.github/workflows/main.yml`.
* It triggers on pushes to the `main` branch.
* You can monitor workflow runs in the "Actions" tab of your GitHub repository.
* The built Docker image is pushed to `https://hub.docker.com/r/your-dockerhub-username/my-flask-app`.

## Deliverables Checklist

* [ ] GitHub repository setup complete.
* [ ] Docker image successfully pushed to Docker Hub (`your-dockerhub-username/my-flask-app`).
* [ ] GitHub Actions workflow runs successfully.
* [ ] Application deployed and accessible locally (via Docker or Minikube).
* [ ] Screenshots of the running application included or linked.

