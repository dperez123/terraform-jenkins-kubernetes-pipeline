# Jenkins Pipeline for Docker Image Creation and ECR Upload with Terraform

This Jenkins pipeline automates the process of creating a Docker image and uploading it to Amazon Elastic Container Registry (ECR) using a deployment script and Terraform. This pipeline is designed to be used in a Continuous Integration/Continuous Deployment (CI/CD) workflow.

## Prerequisites

Before you can use this pipeline, make sure you have the following prerequisites in place:

1. Jenkins: You need to have Jenkins set up and configured on your build server.

2. Jenkins Credentials: Ensure that you have configured SSH credentials for your deployment server, and they are accessible to Jenkins.

3. Git Repositories: You should have the following Git repositories set up:
   - The Terraform code repository (referred to as `projectworkspace` in the pipeline).
   - The web app code repository (referred to as `appworkspace` in the pipeline).

4. Remote Deployment Server: You need a remote server where the deployment will occur. The server should have the required tools and permissions for Terraform and Docker.

## Pipeline Overview

This Jenkins pipeline consists of the following stages:

1. **Get code**: Clone the Terraform code from the specified Git repository.

2. **Get app code**: Clone the web app code from the specified Git repository to a different workspace folder.

3. **Copy terraform code**: Copy the Terraform code from the Jenkins workspace to the remote workspace on the deployment server using `rsync`.

4. **Copy app code**: Copy the web app code from the Jenkins workspace to the remote workspace on the deployment server using `rsync`.

5. **Create docker image and upload to ECR**: Execute a Python script on the deployment server to create a Docker image and upload it to ECR.

6. **Fmt terraform code**: Format the Terraform code on the deployment server using `terraform fmt`.

7. **Init terraform code**: Initialize the Terraform code on the deployment server using `terraform init`.

8. **Validate terraform code**: Validate the Terraform code on the deployment server using `terraform validate`.

9. **Plan terraform code**: Generate a Terraform plan on the deployment server using `terraform plan`.

10. **Apply terraform code**: Apply the Terraform plan on the deployment server using `terraform apply -auto-approve`.

## Pipeline Configuration

Before using the pipeline, you need to configure the following environment variables:

- `projectworkspace`: Path to the Terraform workspace on Jenkins.
- `appworkspace`: Path to the web app workspace on Jenkins.
- `remoteworkspace`: Path to the remote workspace on the deployment server.
- `remoteserver`: SSH connection information for the deployment server (e.g., `user@ip`).

## Usage

1. Create a new Jenkins Pipeline job and configure it with this pipeline script.

2. Configure the necessary Jenkins credentials for SSH access to the deployment server.

3. Trigger the pipeline manually or set up webhooks or triggers based on your CI/CD workflow.

4. Monitor the pipeline execution in Jenkins and check the logs for any errors.

This pipeline automates the process of building and deploying your application using Terraform and Docker, making it easier to manage your infrastructure and application deployments.