## 2 kinds of dependencies in terraform
# implicit dependencies ->  aws_vpc.main.id
# explicit dependencies -> depends_on = [aws_internet_gateway.main]

# VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name = "${var.prefix}-${var.environment}-vpc"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "igw" { 
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "${var.environment}-igw"
  }
}

# Public Subnet 1
resource "aws_subnet" "public_sub1" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "${var.subnet_cidrs[0]}"
  map_public_ip_on_launch = true
  availability_zone       = "ap-south-1a"
  tags = {
    Name = "ECS Fargate Public Subnet 1"
  }
}

# Public Subnet 2
resource "aws_subnet" "public_sub2" { 
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "${var.subnet_cidrs[1]}"
  map_public_ip_on_launch = true
  availability_zone       = "ap-south-1b"
  tags = {
    Name = "ECS Fargate Public Subnet 2"
  }
}

# To ensure proper ordering, it is recommended to add an explicit dependency
# on the Internet Gateway for the VPC.
# Public Route Table
resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "${var.environment}-public-rt"
  }
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
    depends_on = [aws_internet_gateway.igw]
}

# Associate Public Subnet 1 with Public Route Table
resource "aws_route_table_association" "public_sub1_association" {  
  subnet_id      = aws_subnet.public_sub1.id
  route_table_id = aws_route_table.public_rt.id
}
# Associate Public Subnet 2 with Public Route Table
resource "aws_route_table_association" "public_sub2_association" {  
  subnet_id      = aws_subnet.public_sub2.id
  route_table_id = aws_route_table.public_rt.id
}

# Elastic IP 1 for NAT Gateway 1
resource "aws_eip" "nat_eip1" {
  tags = {
    Name = "${var.environment}-nat-eip1"
  }
}

# Elastic IP 2 for NAT Gateway 2
resource "aws_eip" "nat_eip2" {
  tags = {
    Name = "${var.environment}-nat-eip2"
  }
}

#NAT Gateway in Public Subnet 1 
resource "aws_nat_gateway" "nat_gw1" {
  allocation_id = aws_eip.nat_eip1.id
  subnet_id     = aws_subnet.public_sub1.id
  tags = {
    Name = "${var.environment}-nat-gw1"
  }
  depends_on = [aws_internet_gateway.igw, aws_route_table.public_rt]
}

#NAT Gateway in Public Subnet 2
resource "aws_nat_gateway" "nat_gw2" {
  allocation_id = aws_eip.nat_eip2.id
  subnet_id     = aws_subnet.public_sub2.id
  tags = {
    Name = "${var.environment}-nat-gw2"
  }
  depends_on = [aws_internet_gateway.igw, aws_route_table.public_rt]
}

# Private Subnet 1
resource "aws_subnet" "private_sub1" {  
  vpc_id            = aws_vpc.main.id
  cidr_block        = "${var.subnet_cidrs[2]}"
  availability_zone = "ap-south-1a"
  tags = {
    Name = "${var.environment}-private-sub1"
  }
}

# Private Subnet 2
resource "aws_subnet" "private_sub2" {  
  vpc_id            = aws_vpc.main.id
  cidr_block        = "${var.subnet_cidrs[3]}"
  availability_zone = "ap-south-1b"
  tags = {
    Name = "${var.environment}-private-sub2"
  }
} 

# Private Route Table for private subnet 1
resource "aws_route_table" "private_rt1" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "${var.environment}-private-rt1"
  }
  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_gw1.id
  }
    depends_on = [aws_nat_gateway.nat_gw1]
}

# Private Route Table for private subnet 2
resource "aws_route_table" "private_rt2" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "${var.environment}-private-rt2"
  }
  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_gw2.id
  }
    depends_on = [aws_nat_gateway.nat_gw2]
}

# Associate Private Subnet 1 with Private Route Table
resource "aws_route_table_association" "private_sub1_association" {  
  subnet_id      = aws_subnet.private_sub1.id
  route_table_id = aws_route_table.private_rt1.id
}

# Associate Private Subnet 2 with Private Route Table
resource "aws_route_table_association" "private_sub2_association" {  
  subnet_id      = aws_subnet.private_sub2.id
  route_table_id = aws_route_table.private_rt2.id
}

# 2 private subnet for database
# RDS(DB) Subnet 1
resource "aws_subnet" "rds_sub1" {  
  vpc_id            = aws_vpc.main.id
  cidr_block        = "${var.subnet_cidrs[4]}"
  availability_zone = "ap-south-1a"
  tags = {
    Name = "${var.environment}-rds-sub1"
  }
} 

# RDS(DB) Subnet 2
resource "aws_subnet" "rds_sub2" {  
  vpc_id            = aws_vpc.main.id
  cidr_block        = "${var.subnet_cidrs[5]}"
  availability_zone = "ap-south-1b"
  tags = {
    Name = "${var.environment}-rds-sub2"
  }
}

# ALB security group for load balancer -> inbound on port 80(http) and 443(for https) from internet(everywhere)
resource "aws_security_group" "alb_sg" {  
  name        = "${var.environment}-alb-sg"
  description = "Security group for ALB - allows inbound traffic on port 80 and 443 from the world"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
        from_port   = 443
        to_port     = 443
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
    tags = {
        Name = "${var.environment}-alb-sg"
    }
}

# ECS security group --> inbound on port 8000 from load balancer(alb) only
resource "aws_security_group" "ecs_service_sg" {  
  name        = "${var.environment}-ecs-sg"
  description = "Security group for ECS - allows inbound traffic from ALB SG on port 8000"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port       = 8000
    to_port         = 8000
    protocol        = "tcp"
    security_groups = [aws_security_group.alb_sg.id]  # allow from alb sg only
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
    tags = {
        Name = "${var.environment}-ecs-sg"
    }
}

# RDS security group -> inbound on port 5432 from ecs only
resource "aws_security_group" "rds_sg" {  
  name        = "${var.environment}-${var.app_name}-rds-sg"
  description = "Security group for RDS - allows MySQL access from ecs tasks"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    security_groups = [aws_security_group.ecs_service_sg.id]  # allow from ecs service sg only
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
    tags = {
        Name = "${var.environment}-${var.app_name}-rdsdb-sg"
    }
}