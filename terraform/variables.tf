variable "region" {
  description = "AWS region"
 type = string
 default = "us-east-1"
}

variable "clusterName" {
  description = "my EKS cluster"
 type = string
 default = "raghu-eks-2"
}

variable "desired_count" {
 type = number
 default = 5
}

