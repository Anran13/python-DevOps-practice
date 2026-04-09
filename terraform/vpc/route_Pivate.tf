#######################
##### Route Table #####
#######################

resource "aws_route_table" "private-route-table" {
  vpc_id = aws_vpc.vpc-block.id

  tags = {
    Name = "haha-test-Route-Private"
  }
}


###################################
##### Route table association #####
###################################

# 將子網與路由表關聯
resource "aws_route_table_association" "private-subnet1-route-table-association" {
  subnet_id      = aws_subnet.private-subnet1.id
  route_table_id = aws_route_table.private-route-table.id
}

resource "aws_route_table_association" "private-subnet2-route-table-association" {
  subnet_id      = aws_subnet.private-subnet2.id
  route_table_id = aws_route_table.private-route-table.id
}