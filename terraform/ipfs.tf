provider "local" {}

resource "null_resource" "wait_for_node_group" {
  depends_on = [module.eks]


  provisioner "local-exec" {
    command = "cd .. ; helm install ipfs-release helm-chart ; aws eks update-kubeconfig --region ${var.region} --name ${var.clusterName}" 
}
}

