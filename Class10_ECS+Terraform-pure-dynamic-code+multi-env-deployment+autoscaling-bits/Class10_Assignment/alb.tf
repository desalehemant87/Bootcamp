# ALB
resource "aws_lb" "alb" {
  name               = "${var.environment}-${var.app_name}-alb"
  internal           = false
  security_groups    = [aws_security_group.alb_sg.id]
  subnets            = [aws_subnet.public_sub1.id, aws_subnet.public_sub2.id]
  enable_deletion_protection = false
  tags = {
    Name = "${var.environment}-lb"
  }
  
}

# ALB Target Group
resource "aws_lb_target_group" "alb" {
  name        = "${var.environment}-${var.app_name}-alb-tg"
  port        = 8000
  protocol    = "HTTP"
  vpc_id      = aws_vpc.main.id
  target_type = "ip"

  health_check {
    healthy_threshold   = "3"
    interval            = "90"
    protocol            = "HTTP"
    matcher             = "200-399"
    timeout             = "20"
    path                = "/login"
    unhealthy_threshold = "2"
  }
}

# ALB Listener for http (port 80)
resource "aws_lb_listener" "http_forward" {
  load_balancer_arn = aws_lb.alb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.alb.arn
  }
}

# ALB listener for https (port 443) - optional
resource "aws_lb_listener" "https_forward" {
  load_balancer_arn = aws_lb.alb.arn
  port              = 443
  protocol          = "HTTPS"
  ssl_policy        = "ELBSecurityPolicy-TLS13-1-2-2021-06"
  certificate_arn   = aws_acm_certificate.cert.arn

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.alb.arn
  }
}

