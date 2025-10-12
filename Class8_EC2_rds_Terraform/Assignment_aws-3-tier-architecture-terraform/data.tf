data "aws_ami" "ubuntu_24_04" {
  most_recent = true
  filter {

    name   = "image-id"
    values = ["ami-02d26659fd82cf299"]
  }
  owners = ["099720109477"] # Canonical's AWS account ID
}

data "aws_region" "current" {

}