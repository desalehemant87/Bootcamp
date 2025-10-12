
// Generate a random password for the RDS instance
resource "random_password" "rdspwd2" {
  length  = 16
  special = false
}

// Store the RDS password in AWS Secrets Manager
resource "aws_secretsmanager_secret" "rdspwd2" {
  name_prefix = "${var.prefix}-rdspwd2-"
}

resource "aws_secretsmanager_secret_version" "rdspwd2" {
  secret_id     = aws_secretsmanager_secret.rdspwd2.id
  secret_string = jsonencode({ password = random_password.rdspwd2.result })
}

// Create the RDS PostgreSQL instance
resource "aws_db_instance" "postgresdb" {
  identifier              = "${var.db_name}-postgres"
  engine                 = "postgres"
  engine_version         = "14.12"
  instance_class          = "db.t3.micro"
  allocated_storage       = 30
  username                = var.db_username
  password                = random_password.rdspwd2.result
  vpc_security_group_ids  = [aws_security_group.rds_sg.id]
  db_subnet_group_name    = aws_db_subnet_group.main.name
  skip_final_snapshot     = true

  tags = merge(
    local.common_tags,
    tomap({ "Name" = "${local.prefix}-postgres" })
  )
}

// Create a DB subnet group for the RDS instance
resource "aws_db_subnet_group" "main" {
  name       = "${var.prefix}-db-subnet-group"
  subnet_ids = [aws_subnet.private1.id, aws_subnet.private2.id]

  tags = merge(
    local.common_tags,
    tomap({ "Name" = "${local.prefix}-db-subnet-group" })
  )
}

// Create a security group for the EC2 instance
resource "aws_security_group" "ec2-sg" {
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(
    local.common_tags,
    tomap({ "Name" = "${local.prefix}-ec2-sg" })
  )
}
