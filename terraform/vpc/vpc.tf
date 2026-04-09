#VPC
resource "aws_vpc" "vpc-block" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "haha-test-vpc"
  }
}

## output
output "vpc_id" {
  value = aws_vpc.vpc-block.tags["Name"]
}