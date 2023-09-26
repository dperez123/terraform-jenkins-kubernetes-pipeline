# This file contains the terraform code to create the kubernetes deployment and service
terraform {
    required_providers {
        kubernetes = {
        source  = "hashicorp/kubernetes"
        version = "2.0.2"
        }
    }
}

# Configure the Kubernetes Provider
provider "kubernetes" {
    config_path = "~/.kube/config"
}

# Create the Kubernetes Deployment and Service
resource "kubernetes_deployment" "nginx" {
    metadata {
        name = "nginx"
        labels = {
        app = "nginx"
        }
    }
    spec {
        replicas = 2
        selector {
        match_labels = {
            app = "nginx"
        }
        }
        template {
        metadata {
            labels = {
            app = "nginx"
            }
        }
        spec {
            container {
            image = "${var.ecr_url}:${var.nginx_version}"
            name  = "nginx"
            port {
                container_port = 80
            }
            }
        }
        }
    }
    lifecycle {
      create_before_destroy = true
    }
  
}

# Create the Kubernetes Service
resource "kubernetes_service" "nginx_service" {
    metadata {
        name = "nginx"
    }
    spec {
        selector = {
        app = "nginx"
        }
        port {
        port        = 80
        target_port = 80
        }
        type = "LoadBalancer"
    }   
}