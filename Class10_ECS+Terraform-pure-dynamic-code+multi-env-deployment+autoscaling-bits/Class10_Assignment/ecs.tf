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
  family = "${var.environment}-${var.app_name}-task-def"
  container_definitions = jsonencode(
    [
      {
        "name" : "${var.ecs_app_values["container_name"]}",
        "image" : "${data.aws_caller_identity.current.account_id}.dkr.ecr.${data.aws_region.current.id}.amazonaws.com/${var.ecs_app_values["image_name"]}",
        "portMappings" = [
          {
            "containerPort" = tonumber("${var.ecs_app_values["container_port"]}"),
            "hostPort"      = tonumber("${var.ecs_app_values["container_port"]}")
            
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
  memory             = var.ecs_app_values["memory"]
  network_mode       = "awsvpc"
  requires_compatibilities = [
    var.ecs_app_values["launch_type"],
  ]

}

# ECS service

resource "aws_ecs_service" "ecs" {
  name                       = "${var.environment}-${var.app_name}-service"
  cluster                    = aws_ecs_cluster.ecs.id
  task_definition            = aws_ecs_task_definition.ecs.arn
  desired_count              = var.ecs_app_values["desired_count"]
  deployment_maximum_percent = 250 # 
  launch_type                = var.ecs_app_values["launch_type"]
  force_new_deployment       = true

  network_configuration {
    security_groups  = [aws_security_group.ecs_service_sg.id]
    subnets          = [aws_subnet.private_sub1.id, aws_subnet.private_sub2.id]
    assign_public_ip = false
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.alb.arn
    container_name   = var.ecs_app_values["container_name"]
    container_port   = var.ecs_app_values["container_port"]
  }

  depends_on = [
    aws_iam_role.ecs_task_execution_role,
  ]

}

# scaling policy

resource "aws_appautoscaling_target" "ecs" {
  max_capacity       = 5
  min_capacity       = 2
  resource_id        = "service/${aws_ecs_cluster.ecs.name}/${aws_ecs_service.ecs.name}"
  scalable_dimension = "ecs:service:DesiredCount"
  service_namespace  = "ecs"
}

resource "aws_appautoscaling_policy" "cpu_scaling_policy" {
  name               = "${var.environment}-${var.app_name}-cpu-scaling-policy"
  policy_type        = "TargetTrackingScaling"
  resource_id        = aws_appautoscaling_target.ecs.resource_id
  scalable_dimension = aws_appautoscaling_target.ecs.scalable_dimension
  service_namespace  = aws_appautoscaling_target.ecs.service_namespace

  target_tracking_scaling_policy_configuration {
    predefined_metric_specification {
      predefined_metric_type = "ECSServiceAverageCPUUtilization"
    }
    target_value       = 60.0
    scale_in_cooldown  = 30
    scale_out_cooldown = 30
  }
}