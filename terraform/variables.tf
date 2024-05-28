variable "region" {
  description = "AWS region"
 type = string
 default = "us-east-1"
}

variable "clusterName" {
  description = "Raghu EKS cluster"
 type = string
 default = "raghu-eks"
}

variable "desired_count" {
 type = number
 default = 1
}

