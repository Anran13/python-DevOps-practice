##########################
##### VPC CIDR Block #####
##########################
variable "vpc_cidr" {
  default     = "10.0.0.0/16"
  description = "VPC_cidr block"
  type        = string
}

##################
##### Subnet #####
##################
variable "public-subnet1" {
  default     = "10.0.1.0/24"
  description = "public-subnet-A"
  type        = string
}

variable "public-subnet2" {
  default     = "10.0.2.0/24"
  description = "public-subnet-B"
  type        = string
}

variable "private-subnet1" {
  default     = "10.0.3.0/24"
  description = "private-subnet-A"
  type        = string
}

variable "private-subnet2" {
  default     = "10.0.4.0/24"
  description = "private-subnet-B"
  type        = string
}