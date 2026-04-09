# Private Subnets
resource "aws_subnet" "private-subnet1" {
  tags = {
    Name = "haha-test-PrivateSubnet-A" # 子網的名稱
  }
  vpc_id            = aws_vpc.vpc-block.id
  cidr_block        = var.private-subnet1
  availability_zone = "us-west-1a"
}

resource "aws_subnet" "private-subnet2" {
  tags = {
    Name = "haha-test-PrivateSubnet-B" # 子網的名稱
  }
  vpc_id            = aws_vpc.vpc-block.id
  cidr_block        = var.private-subnet2
  availability_zone = "us-west-1b"
}

## Output
output "private-subnet1_name" {
  value = aws_subnet.private-subnet1.tags["Name"]
}

output "private-subnet2_name" {
  value = aws_subnet.private-subnet2.tags["Name"]
}