provider "local" {}

resource "null_resource" "wait_for_node_group" {
  depends_on = [module.eks]


  provisioner "local-exec" {
    command = "aws eks update-kubeconfig --region ${var.region} --name ${var.clusterName} && cd ../ && cd helm-chart && helm install ipfs-new . " 
}
}

