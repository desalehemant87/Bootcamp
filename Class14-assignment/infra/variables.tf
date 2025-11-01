variable "app_name" {
  type    = string
  default = "app"
}

variable "environment" {
  type    = string
  default = "dev"
}

variable "domain_name" {
  type    = string
  default = "hemantdesale.tech"

}

##### RDS ############

variable "db_default_settings" {
  type = any
  default = {
    allocated_storage       = 30
    max_allocated_storage   = 50
    engine_version          = "14.15"
    engine                 = "postgres"
    instance_class          = "db.t2.micro"
    backup_retention_period = 2
    db_name                 = "postgres"
    ca_cert_name            = "rds-ca-rsa2048-g1"
    db_admin_username       = "postgres"
  }
}


########### microservices #################

#### flask app ####

variable "flask_app_cpu" {
  description = "CPU units for the flask-app service"
  type        = number
  default     = 1024
}

variable "flask_app_memory" {
  description = "Memory in MiB for the flask-app service"
  type        = number
  default     = 2048
}

variable "flask_app_template_file" {
  description = "Template file for the flask-app service"
  type        = string
  default     = "task-definitions/flask-service.json.tpl"
}

variable "flask_app_tag" {
  description = "Tag for the flask-app service"
  type        = string
  default     = "latest"
}

variable "flask_app_container_name" {
  description = "Container name for the flask-app service"
  type        = string
  default     = "flask-app"
}

variable "desired_flask_task_count" {
  description = "Desired count for the flask-app tasks"
  type        = number
  default     = 2

}

variable "flask_app_py" {
  type    = string
  default = "run.py"
}

variable "flask_allowed_origins" {
  type    = string
  default = "http://localhost:3000,http://localhost:80"
}

variable "flask_secret_key" {
  description = "Your secret key - a random string of 64 characters"
  type        = string
  default     = "f4a83d7e15e9f8b1c23b4b73f9b09b8827f501bbdce1a3dca7d23d8c991e3f45"
}

##### react ####

variable "react_cpu" {
  description = "CPU units for the react service"
  type        = number
  default     = 1024
}

variable "react_memory" {
  description = "Memory in MiB for the react service"
  type        = number
  default     = 2048
}

variable "react_template_file" {
  description = "Template file for the react service"
  type        = string
  default     = "task-definitions/react-service.json.tpl"
}

variable "react_aws_ecr_repository" {
  description = "ECR repository URL for the react service"
  type        = string
  default     = "059941826920.dkr.ecr.ap-south-1.amazonaws.com/react"
}

variable "react_tag" {
  description = "Tag for the react service"
  type        = string
  default     = "latest"
}

variable "react_container_name" {
  description = "Container name for the react service"
  type        = string
  default     = "react"
}

variable "desired_react_task_count" {
  description = "Desired count for the flask-app tasks"
  type        = number
  default     = 2

}

variable "react_backend_url" {
  description = "backend url from react app"
  type        = string
  default     = "http://app:8000"
}

