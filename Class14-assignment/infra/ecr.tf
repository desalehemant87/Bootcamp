locals {
  ecr_repo= {
    flask = "flask"
    react = "react"
  }
}

# for_each works with maps {} and set [] list of unique value

resource "aws_ecr_repository" "python_app" {
  # for_each = toset((local.ecr_repo))
  for_each = local.ecr_repo
  name = "${var.environment}-${var.app_name}-${each.value}"
}