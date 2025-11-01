terraform {
  required_version = ">= 1.5.7"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0.0" # >= 6.0.0 and < 7.0.0
    }
    random = {
      source  = "hashicorp/random"
      version = ">= 3.0.0" # >= 3.0.0 and < 4.0.0
    }
    template = {
      source  = "hashicorp/template"
      version = ">= 2.2.0" # Update this to a compatible version
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

# Using S3 backend
terraform {
  backend "s3" {
  }
}