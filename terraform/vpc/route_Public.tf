# route_Public.tf

#######################
##### Route Table #####
#######################

# 創建公共路由表
resource "aws_route_table" "public-subnet-route-table" {
  vpc_id = aws_vpc.vpc-block.id

  tags = {
    Name = "haha-test-Route-Public"
  }
}

# 添加路由規則
resource "aws_route" "public-subnet-default-route" {
  route_table_id         = aws_route_table.public-subnet-route-table.id
  destination_cidr_block = "0.0.0.0/0"                 # 所有流量
  gateway_id             = aws_internet_gateway.igw.id # 通過 Internet Gateway 出去
}


###################################
##### Route table association #####
###################################

# 將子網與路由表關聯
resource "aws_route_table_association" "public-subnet1-route-table-association" {
  subnet_id      = aws_subnet.public-subnet1.id
  route_table_id = aws_route_table.public-subnet-route-table.id
}

resource "aws_route_table_association" "public-subnet2-route-table-association" {
  subnet_id      = aws_subnet.public-subnet2.id
  route_table_id = aws_route_table.public-subnet-route-table.id
}