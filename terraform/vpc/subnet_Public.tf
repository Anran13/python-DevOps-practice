#2 Public Subnets
resource "aws_subnet" "public-subnet1" {
  tags = {
    Name = "haha-test-PublicSubnet-A" # 子網的名稱
  }
  vpc_id            = aws_vpc.vpc-block.id
  cidr_block        = var.public-subnet1
  availability_zone = "us-west-1a"
}

resource "aws_subnet" "public-subnet2" {
  tags = {
    Name = "haha-test-PublicSubnet-B" # 子網的名稱
  }
  vpc_id            = aws_vpc.vpc-block.id
  cidr_block        = var.public-subnet2
  availability_zone = "us-west-1b"
}

## Output
output "public-subnet1_name" {
  value = aws_subnet.public-subnet1.tags["Name"]
}

output "public-subnet2_name" {
  value = aws_subnet.public-subnet2.tags["Name"]
}