# ipfs-demo

This project installs IPFS service in a AWS managed EKS cluster provisioned using using python flask API with IAC tool Terraform and Helm chart.

**Prerequisites to be installed in local:**
- Terraform >= v1.5.6
- Helm3
- Python3 flask

**Steps to deploy IPFS Service:**
- Clone the ipfs-demo git repo
  
  ` git clone https://github.com/raghu1306/ipfs-demo.git `
- Start the Python flask server using command
  
  ` cd ipfs-demo/src `
  
  ` python.exe app.py `

- To provision insfrastructure and to deploy IPFS Helm chart run the curl command with following API calls

    ` curl -X POST http://127.0.0.1:5000/terraform/init `

    ` curl -X POST http://127.0.0.1:5000/terraform/apply `

- To scale up or down the nodeGroup (no. of instances)

    ` curl -X POST http://127.0.0.1:5000/terraform/scale -H "Content-Type: application/json" -d '{"count": 5}' `

- To show the status of the insfrastructure
 
    ` curl http://127.0.0.1:5000/terraform/status `

- To delete the infrastucture resources

    ` curl -X POST http://127.0.0.1:5000/terraform/destroy `

    

    
    

    
    
  
  
