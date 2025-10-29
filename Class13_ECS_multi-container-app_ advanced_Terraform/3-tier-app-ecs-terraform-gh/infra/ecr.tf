# resource "aws_ecr_repository" "python_app" {
#   name = "${var.environment}-${var.app_name}-flask"
# }
# resource "aws_ecr_repository" "redis" {
#   name = "${var.environment}-${var.app_name}-redis"
# }

# resource "aws_ecr_repository" "nginx" {
#   name = "${var.environment}-${var.app_name}-nginx"
# }


locals {
  # ecr_repo= ["flask", "redis", "nginx"]

  ecr_repo= {
    flask = "flask"
    redis = "redis"
    nginx = "nginx"
  }
  

}

# for_each works with maps {} and set [] list of unique value

resource "aws_ecr_repository" "python_app" {
  # for_each = toset((local.ecr_repo))
  for_each = local.ecr_repo
  name = "${var.environment}-${var.app_name}-${each.value}"
}