terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "~> 4.16"
    }
  }
  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "us-west-2"
}

# 引用 vpc 子模塊
module "vpc" {
  source = "./vpc" # 指定 vpc 子模塊的路徑。
}