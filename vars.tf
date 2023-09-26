# Description: Variables for the Terraform Jenkins Kubernetes Pipeline

# Aws ecr url
variable "ecr_url" {
    description = "ECR URL"
    default = "635182717371.dkr.ecr.us-east-2.amazonaws.com/example"
}

# Nginx version
variable "nginx_version" {
    description = "nginx version"
    default = "nginx-20230923080941"
}