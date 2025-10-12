# ecs task definition -> will use 1 template.
#  ecs cluser
# ecs service -> will map this to load balancer 

# ECS cluster
resource "aws_ecs_cluster" "ecs" {
  name = "${var.environment}-${var.app_name}-cluster"
}

# Task defnition
resource "aws_ecs_task_definition" "ecs" {
  #checkov:skip=CKV_AWS_336: The ECS task needs write access to system
  family = "aug-task-def"
  container_definitions = jsonencode(
    [
      {
        "name" : "aug-container",
        "image" : "059941826920.dkr.ecr.ap-south-1.amazonaws.com/ecs-studentportal-1.0:latest",
        "portMappings" = [
          {
            "containerPort" = 8000
            "hostPort"      = 8000
            
          }
        ],
        "essential" : true,
        "logConfiguration" : {
          "logDriver" : "awslogs",
          "options" : {
            "awslogs-group" : aws_cloudwatch_log_group.ecs.name,
            "awslogs-region" : data.aws_region.current.id,
            "awslogs-stream-prefix" : "ecs"
          },
        },
        "environment" : [
          {
            "name" : "DB_LINK",
            "value" : "postgresql://${aws_db_instance.postgres.username}:${random_password.dbs_random_string.result}@${aws_db_instance.postgres.address}:${aws_db_instance.postgres.port}/${aws_db_instance.postgres.db_name}"
          },

        ]
      }
  ])

  cpu = 256
  # role for task to pull the ecr image
  execution_role_arn = aws_iam_role.ecs_task_execution_role.arn
  memory             = 512
  network_mode       = "awsvpc"
  requires_compatibilities = [
    "FARGATE",
  ]

}

# ECS service

resource "aws_ecs_service" "ecs" {
  name                       = "aug-service"
  cluster                    = aws_ecs_cluster.ecs.id
  task_definition            = aws_ecs_task_definition.ecs.arn
  desired_count              = 2
  deployment_maximum_percent = 250 # 
  launch_type                = "FARGATE"
  force_new_deployment       = true

  network_configuration {
    security_groups  = [aws_security_group.ecs_service_sg.id]
    subnets          = [aws_subnet.private_sub1.id, aws_subnet.private_sub2.id]
    assign_public_ip = false
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.alb.arn
    container_name   = "aug-container"
    container_port   = 8000
  }

  depends_on = [
    aws_iam_role.ecs_task_execution_role,
  ]

}