# This file is used to output the DNS name of the load balancer created by the Kubernetes service.
output "nginx_service_dns" {
    value = kubernetes_service.nginx_service.status.0.load_balancer.0.ingress.0.hostname
}