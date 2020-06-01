import json
import paramiko
import sys

def lambda_handler(event, context):
    
    
    ### Declare vars 
    host_ip='3.231.203.45'
    host_port=22
    username='ec2-user'
    pkey_path="lambda_kp.pem"
    
    
    ### creating RSAKey object
    key=paramiko.RSAKey.from_private_key_file(pkey_path)
    
    ### Create ssh client 
    ssh=paramiko.SSHClient()

    ### Automatically add the host to varified host file
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    ### Make a connection
    ssh.connect(hostname=host_ip, username=username, pkey=key)
    
    ### Run commands
    stdin, stdout, stderr = ssh.exec_command('ls -al')
    
    ### Print the stdout
    for line in stdout.read().splitlines():
        print(line.decode("utf-8"))
    
    ### Close the client
    ssh.close()
