[
  {
    "name": "${container_name}",
    "image": "${aws_ecr_repository}:${tag}",
    "essential": true,
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-region": "ap-south-1",
        "awslogs-stream-prefix": "${aws_cloudwatch_log_group_name}-service",
        "awslogs-group": "${aws_cloudwatch_log_group_name}"
      }
    },
    "portMappings": [
      {
        "containerPort": 8000,
        "hostPort": 8000,
        "protocol": "tcp",
        "name": "app",
        "appProtocol": "http"
      }
    ],
    "command": [
    "bash",
    "-c",
    "sleep 10 && ./migrate.sh && gunicorn --bind 0.0.0.0:8000 run:app"
    ],
    "environment": [
      {
        "name": "ENV",
        "value": "${environment}"
      },
      {
        "name": "FLASK_APP",
        "value": "${flask_app_py}"
      },
      {
        "name": "FLASK_DEBUG",
        "value": "1"
      },
      {
        "name": "DATABASE_URL",
        "value": "${database_url}"
      },
      {
        "name": "SECRET_KEY",
        "value": "${secret_key}"
      },
      {
        "name": "DB_HOST",
        "value": "${database_address}"
      },
      {
        "name": "DB_PORT",
        "value": "${database_port}"
      },
      {
        "name": "DB_NAME",
        "value": "${database_name}"
      },
      {
        "name": "DB_USERNAME",
        "value": "${postgres_username}"
      },
      {
        "name": "DB_PASSWORD",
        "value": "${postgres_password}"
      },
      {
        "name": "ALLOWED_ORIGINS",
        "value": "*"
      }
   ]
  }
]
