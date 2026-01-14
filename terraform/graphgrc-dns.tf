# Route 53 DNS record for graphgrc.engseclabs.com
# Run with: terraform init && terraform apply

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  profile = "alex-admin"
  region  = "us-east-1"
}

# Get the existing hosted zone for engseclabs.com
data "aws_route53_zone" "engseclabs" {
  name         = "engseclabs.com."
  private_zone = false
}

# CNAME record pointing to GitHub Pages
resource "aws_route53_record" "graphgrc" {
  zone_id = data.aws_route53_zone.engseclabs.zone_id
  name    = "graphgrc.engseclabs.com"
  type    = "CNAME"
  ttl     = 300
  records = ["engseclabs.github.io"]
}

output "dns_record" {
  value = {
    name  = aws_route53_record.graphgrc.name
    type  = aws_route53_record.graphgrc.type
    value = aws_route53_record.graphgrc.records
  }
  description = "Created DNS record for GraphGRC"
}
