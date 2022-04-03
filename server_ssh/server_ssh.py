import paramiko
import argparse

def create_connection(host,special_account,key_path,server):
    # host = "192.0.2.0"
    # special_account = "user1"
    pkey = paramiko.RSAKey.from_private_key_file(key_path)
    client = paramiko.SSHClient()
    policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(policy)
    client.connect(host,username=special_account,pkey=pkey)

    return client