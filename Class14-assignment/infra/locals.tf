locals {
  db_data = {
    allocated_storage       = "30"
    max_allocated_storage   = 100
    engine_version          = "14.15"
    engine                  = "postgres"
    instance_class          = "db.t3.small"
    ca_cert_name            = "rds-ca-rsa2048-g1"
    backup_retention_period = 7
    db_name                 = "mydb"
    cloudwatch_logs         = ["postgresql", "upgrade"]
  }

  ecs_services = [
    {
      name          = "flask"
      cpu           = var.flask_app_cpu
      memory        = var.flask_app_memory
      template_file = var.flask_app_template_file
      vars = {
        # aws_ecr_repository            = aws_ecr_repository.python_app.repository_url
        aws_ecr_repository            = aws_ecr_repository.python_app["flask"].repository_url
        tag                           = var.flask_app_tag
        container_name                = var.flask_app_container_name
        aws_cloudwatch_log_group_name = "/aws/ecs/${var.environment}-flask"
        database_address              = var.environment == "dev" ? aws_db_instance.postgres[0].address : aws_rds_cluster.postgres[0].endpoint
        database_name                 = var.environment == "dev" ? aws_db_instance.postgres[0].db_name : aws_rds_cluster.postgres[0].database_name
        postgres_username             = var.environment == "dev" ? aws_db_instance.postgres[0].username : aws_rds_cluster.postgres[0].master_username
        postgres_password             = random_password.dbs_random_string.result
        database_url                  = var.environment == "dev" ? "postgresql://${aws_db_instance.postgres[0].username}:${random_password.dbs_random_string.result}@${aws_db_instance.postgres[0].address}:${aws_db_instance.postgres[0].port}/${aws_db_instance.postgres[0].db_name}" : "postgres://${aws_rds_cluster.postgres[0].master_username}:${random_password.dbs_random_string.result}@${aws_rds_cluster.postgres[0].endpoint}:${aws_rds_cluster.postgres[0].port}/${aws_rds_cluster.postgres[0].database_name}"
        database_port                 = var.environment == "dev" ? aws_db_instance.postgres[0].port : aws_rds_cluster.postgres[0].port
        flask_app_py                  = var.flask_app_py
        allowed_origins               = var.flask_allowed_origins
        secret_key                    = var.flask_secret_key
        environment                   = var.environment
      }
    },
    {
      name          = "react"
      cpu           = var.react_cpu
      memory        = var.react_memory
      template_file = var.react_template_file
      vars = {
        # aws_ecr_repository            = aws_ecr_repository.react.repository_url
        aws_ecr_repository            = aws_ecr_repository.python_app["react"].repository_url
        tag                           = var.react_tag
        container_name                = var.react_container_name
        aws_cloudwatch_log_group_name = "/aws/ecs/${var.environment}-react"
        backend_url                   = var.react_backend_url
        environment                   = var.environment
      }
    }
   
  ]
  ecs_service_map = {for service in local.ecs_services : service.name => service}


  # flask = 


  flask_deploy_data = {
    IMAGE_NAME : "${var.app_name}-image"
    ECR_REGISTRY : "${data.aws_caller_identity.current.account_id}.dkr.ecr.${data.aws_region.current.id}.amazonaws.com"
    ECR_REPOSITORY : "${var.environment}-${var.app_name}-flask"
    ACCOUNT_ID : data.aws_caller_identity.current.account_id
    ECS_CLUSTER : "${var.environment}-${var.app_name}-cluster"
    ECS_REGION : data.aws_region.current.id
    ECS_SERVICE : "${var.environment}-${var.app_name}-flask-service"
    ECS_TASK_DEFINITION : "${var.environment}-${var.app_name}-flask"
    ECS_APP_CONTAINER_NAME : var.flask_app_container_name

  }
}

resource "random_string" "secret_suffix" {
  length  = 4
  upper   = false
  special = false
}

resource "aws_secretsmanager_secret" "app_deploy_data" {
  name        = "flask/${var.environment}-${var.app_name}-${random_string.secret_suffix.result}"
  description = "Deployment data for the Flask app"
  depends_on = [random_string.secret_suffix]
}

resource "aws_secretsmanager_secret_version" "app_deploy_data_version" {
  secret_id     = aws_secretsmanager_secret.app_deploy_data.id
  secret_string = jsonencode(local.flask_deploy_data)
}


# output "ecs_services" {
#   value = local.ecs_services
# }

# output "ecs_services_map" {
#   value = local.ecs_service_map
# }

# output the database address
output "database_address" {
  value = aws_db_instance.postgres[0].address
} 

# output the database name
output "database_name" {
  value = aws_db_instance.postgres[0].db_name
} 
