variable "region" {
  description = "The region in which the resources will be created"
  default     = "ap-south-1"
}

variable "vpc_cidr" {
  type    = string
  default = "10.0.0.0/16"
}

variable "environment" {
  description = "The environment in which the resources will be created"
  default     = "dev"
}

variable "prefix" {
  description = "main"
  default = "main"
}

variable "app_name" {
  description = "The name of the application"
  default     = "studentportal"
}

variable "subnet_cidrs" {
  description = "A list of CIDR blocks for the subnets"
  type        = list(string)
  default = [
    "10.0.1.0/24",
    "10.0.2.0/24",
    "10.0.3.0/24",
    "10.0.4.0/24",
    "10.0.5.0/24",
    "10.0.6.0/24"
  ]

}

variable "db_default_settings" {
  type = any
  default = {
    allocated_storage       = 30
    max_allocated_storage   = 50
    engine_version          = 14.15
    instance_class          = "db.t3.micro"
    backup_retention_period = 2
    db_name                 = "postgres"
    ca_cert_name            = "rds-ca-rsa2048-g1"
    db_admin_username       = "postgres"
  }
}

variable "public_hosted_zone_id" {
  description = "The hosted zone id for the public domain"
  default     = "hemantapps.site"
}

variable "domain_name" {
  description = "hemantdesale.tech"
  default = "hemantdesale.tech"
}
