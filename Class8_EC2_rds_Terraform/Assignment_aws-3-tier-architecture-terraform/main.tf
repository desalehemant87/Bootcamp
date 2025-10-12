resource "aws_security_group" "public_ssh_sg" {

  description = "allow ssh to public ec2"
  name        = "${local.prefix}-public-ssh-access"
  vpc_id      = aws_vpc.main.id

  ingress {
    protocol    = "tcp"
    from_port   = 22
    to_port     = 22
    cidr_blocks = ["0.0.0.0/0"]
    #We can limit the ip here
  }
  tags = local.common_tags

}

# Security Group for SSH Access to Private EC2 Instances
resource "aws_security_group" "private_ssh_sg" {

  description = "allow ssh to private ec2"
  name        = "${local.prefix}-private-ssh-access"
  vpc_id      = aws_vpc.main.id

  ingress {
    protocol    = "tcp"
    from_port   = 22
    to_port     = 22
    cidr_blocks = [var.vpc_cidr]
    #We can limit the ip here
  }
  tags = local.common_tags

}

// Create a security group for the RDS instance
resource "aws_security_group" "rds_sg" {
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = [aws_subnet.private1.cidr_block, aws_subnet.private2.cidr_block]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(
    local.common_tags,
    tomap({ "Name" = "${local.prefix}-rds-sg" })
  )
}