resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
    tags = {
        Name = "${var.environment}-vpc"
    }
}

resource "aws_subnet" "public" {
  vpc_id            = aws_vpc.main.id
  count             = 2
  cidr_block        = cidrsubnet(aws_vpc.main.cidr_block, 8, 2 + count.index)
  availability_zone = data.aws_availability_zones.available_zones.names[count.index]
  map_public_ip_on_launch = true
    tags = {
        Name = "${var.environment}-ecs-fargate-public-sub-${count.index}"
    }
}

resource aws_subnet "private" {
  vpc_id            = aws_vpc.main.id
  count             = 2
  cidr_block        = cidrsubnet(aws_vpc.main.cidr_block, 8, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]
    tags = {
        Name = "${var.environment}-ecs-fargate-private-sub-${count.index}"
    }
}

resource "aws_subnet" "rds" {
  vpc_id            = aws_vpc.main.id
  count             = 2
  cidr_block        = cidrsubnet(aws_vpc.main.cidr_block, 8, 4 + count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]
    tags = {
        Name = "${var.environment}-rds-private-sub-${count.index}"
    }
}

resource "aws_internet_gateway" "gateway" {
  vpc_id = aws_vpc.main.id
    tags = {
        Name = "${var.environment}-igw"
    }
}

resource "aws_route" "internet_access" {
  route_table_id         = aws_vpc.main.main_route_table_id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.gateway.id
}

# use with private subnet if ecs tasks need internet access
resource "aws_eip" "gateway" {
  count      = 2
  depends_on = [ aws_internet_gateway.gateway ]
}

resource "aws_nat_gateway" "gateway" {
  count         = 2
  allocation_id = element(aws_eip.gateway.*.id,count.index)
  subnet_id     = element(aws_subnet.public.*.id,count.index)
    tags = {
        Name = "${var.environment}-nat-gateway-${count.index}"
    }  
}

resource "aws_route_table" "private" {
  count                   = 2
  vpc_id                  = aws_vpc.main.id
  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = element(aws_nat_gateway.gateway.*.id, count.index)
  }
    tags = {
        Name = "${var.environment}-ecs-ec2-private-rt-${count.index}"
    }
}

resource "aws_route_table_association" "private" {
  count          = 2
  subnet_id      = element(aws_subnet.private.*.id, count.index)
  route_table_id = element(aws_route_table.private.*.id, count.index)
}

# Secutiry Groups

resource "aws_security_group" "lb" {
  name        = "${var.environment}-lb-sg"
  vpc_id      = aws_vpc.main.id
  description = "controls access to the Application Load Balancer (ALB)"

  ingress {
    protocol    = "tcp"
    from_port   = 80
    to_port     = 80
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    protocol    = "tcp"
    from_port   = 443
    to_port     = 443
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "ecs_tasks_flask" {
  name        = "${var.environment}-ecs-tasks-flask-sg"
  vpc_id      = aws_vpc.main.id
  description = "allow inbound access from the ALB only"

  ingress {
    protocol        = "tcp"
    from_port       = 8000
    to_port         = 8000
    security_groups = [aws_security_group.ecs_tasks_react.id]
  }

  egress {
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }

}

resource "aws_security_group" "ecs_tasks_react" {
  name        = "${var.environment}-ecs-tasks-react-sg"
  vpc_id      = aws_vpc.main.id
  description = "allow inbound access from the ALB only"

  ingress {
    protocol        = "tcp"
    from_port       = 80
    to_port         = 80
    security_groups = [aws_security_group.lb.id]

  }

  egress {
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }

}

resource "aws_security_group" "rds" {
  name        = "${var.environment}-rds-sg"
  vpc_id      = aws_vpc.main.id
  description = "allow inbound access from the ECS only"

  ingress {
    protocol        = "tcp"
    from_port       = 5432
    to_port         = 5432
    cidr_blocks     = ["0.0.0.0/0"]
    security_groups = [aws_security_group.ecs_tasks_flask.id]
  }

  egress {
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}