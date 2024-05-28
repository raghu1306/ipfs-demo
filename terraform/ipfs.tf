provider "local" {}

resource "null_resource" "example" {
  provisioner "local-exec" {
    command = "git clone https://github.com/raghu1306/ipfs-demo.git ; cd ipfs-demo ; helm install ipfs-release helm-chart ;aws eks update-kubeconfig --region ${var.region} --name ${var.clusterName} ;  cd .. ; rm -rf ipfs-demo  }


}
