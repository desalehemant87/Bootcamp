# have a registered domain in aws or outside in godaddy or any other domain provider
# create a public hosted zone in route53
# map dns servers to the domain provider
### 

# create a public hosted zone
data "aws_route53_zone" "primary" {
  name         = "hemantdesale.tech"
  private_zone = false
}

# Create the DNS record for the application
resource "aws_route53_record" "app" {
  zone_id = data.aws_route53_zone.primary.zone_id
  name    = "${var.environment}.${data.aws_route53_zone.primary.name}"
  type    = "A"
  alias {
    name                   = aws_lb.alb.dns_name
    zone_id                = aws_lb.alb.zone_id
    evaluate_target_health = true
  }
}

# Create an ACM certificate
resource "aws_acm_certificate" "cert" {
  # "august.akhileshmishra.tech"
  domain_name       = "${var.environment}.${data.aws_route53_zone.primary.name}"
  validation_method = "DNS"
  tags = {
    Name = "${var.environment}.${data.aws_route53_zone.primary.name}-cert"
  }
}

# Create a DNS validation record
resource "aws_route53_record" "cert_validation" {
  for_each = {
    for dvo in aws_acm_certificate.cert.domain_validation_options : dvo.domain_name => {
      name   = dvo.resource_record_name
      type   = dvo.resource_record_type
      record = dvo.resource_record_value
    }
  }
  zone_id = data.aws_route53_zone.primary.zone_id
  name    = each.value.name
  type    = each.value.type
  ttl     = 60
  records = [each.value.record]
}

# ACM cert validation using DNS
resource "aws_acm_certificate_validation" "cert_validation" {
  certificate_arn         = aws_acm_certificate.cert.arn
  validation_record_fqdns = [for record in aws_route53_record.cert_validation : record.fqdn]
}