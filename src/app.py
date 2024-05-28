from flask import Flask, jsonify, request
import subprocess
#import requests

app = Flask(__name__)

new_directory = '../terraform/'

@app.route('/terraform/init', methods=['POST'])
def init_terraform():
    try:
        # Run Terraform init command
        result = subprocess.run(['terraform', 'init',], cwd=new_directory, capture_output=True, text=True)
        if result.returncode == 0:
            return jsonify({"message": "Terraform initialization successful", "output": result.stdout}), 200
        else:
            return jsonify({"message": "Terraform initilalization failed", "error": result.stderr}), 500
    except Exception as e:
        return jsonify({"message": "Error occurred", "error": str(e)}), 500

@app.route('/terraform/apply', methods=['POST'])
def apply_terraform():
    try:
        # Run Terraform apply command
        result = subprocess.run(['terraform', 'apply', '-auto-approve'], cwd=new_directory, capture_output=True, text=True)
        if result.returncode == 0:
            return jsonify({"message": "Terraform apply successful", "output": result.stdout}), 200
        else:
            return jsonify({"message": "Terraform apply failed", "error": result.stderr}), 500
    except Exception as e:
        return jsonify({"message": "Error occurred", "error": str(e)}), 500

@app.route('/terraform/scale', methods=['POST'])
def scale_terraform():
    data = request.get_json()
    desired_count = data.get('count')
    
    if desired_count is None:
        return jsonify({'error': 'Count is required'}), 400

    # Run Terraform command to scale nodes
    result = subprocess.run(['terraform', 'apply', '-var', f'desired_count={desired_count}', '-auto-approve'], cwd=new_directory, capture_output=True, text=True)

    if result.returncode != 0:
        return jsonify({'error': result.stderr}), 500

    return jsonify({'message': 'Scaling operation completed', 'output': result.stdout})


@app.route('/terraform/destroy', methods=['POST'])
def destroy_terraform():
    try:
        # Run Terraform destroy command
        result = subprocess.run(['terraform', 'destroy', '-auto-approve'], cwd=new_directory, capture_output=True, text=True)
        if result.returncode == 0:
            return jsonify({"message": "Terraform destroy successful", "output": result.stdout}), 200
        else:
            return jsonify({"message": "Terraform destroy failed", "error": result.stderr}), 500
    except Exception as e:
        return jsonify({"message": "Error occurred", "error": str(e)}), 500

@app.route('/terraform/status', methods=['GET'])
def status_terraform():
    try:
        # Run Terraform status command
        result = subprocess.run(['terraform', 'show'], cwd=new_directory, capture_output=True, text=True)
        if result.returncode == 0:
            return jsonify({"message": "Terraform status successful", "output": result.stdout}), 200
        else:
            return jsonify({"message": "Terraform status failed", "error": result.stderr}), 500
    except Exception as e:
        return jsonify({"message": "Error occurred", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

