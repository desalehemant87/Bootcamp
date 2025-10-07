# output.tf
output "ec2_public_ip" {
  description = "public ip for ec2"
  value       = aws_instance.public.public_ip
}

output "vpc_id" {
  description = "The ID of the VPC"
  value       = aws_vpc.main.id
}

output "private_subnet1_id" {
  description = "The IDs of the private subnets"
  value       = aws_subnet.private1.id
}

output "private_subnet2_id" {
  description = "The IDs of the private subnets"
  value       = aws_subnet.private2.id
}

output "rds_endpoint" {
  description = "The endpoint of the RDS instance"
  value       = aws_db_instance.postgresdb.endpoint
}

output "ec2_instance_public_id" {
  description = "The ID of the EC2 public instance"
  value       = aws_instance.public.id
}

output "ec2_instance_private_id" {
  description = "The ID of the EC2 public instance"
  value       = aws_instance.private.id
}