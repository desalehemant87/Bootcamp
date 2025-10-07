# Private ec2
resource "aws_instance" "private" {
  ami                    = data.aws_ami.ubuntu_24_04.id
  instance_type          = var.instance_type
  subnet_id              = aws_subnet.private1.id
  availability_zone      = aws_subnet.private1.availability_zone
  vpc_security_group_ids = [aws_security_group.private_ssh_sg.id,]
  key_name               = "ssh-key"
  tags = merge(
    local.common_tags,
    tomap({ "Name" = "${local.prefix}-private-ec2" })
  )
}

# Public ec2
resource "aws_instance" "public" {
  ami                    = data.aws_ami.ubuntu_24_04.id
  instance_type          = var.instance_type
  subnet_id              = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.public_ssh_sg.id, ]
  key_name               = "ssh-key"
  availability_zone      = "${data.aws_region.current.name}a"

  tags = merge(
    local.common_tags,
    tomap({ "Name" = "${local.prefix}-public-ec2" })
  )
}
