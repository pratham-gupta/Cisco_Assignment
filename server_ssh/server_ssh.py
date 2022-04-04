import paramiko
import argparse
import os

def create_connection(host,username,key_path):
    # host = "192.0.2.0"
    # special_account = "user1"
    pkey = paramiko.RSAKey.from_private_key_file(key_path)
    client = paramiko.SSHClient()
    policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(policy)
    client.connect(host,username=username,pkey=pkey)

    return client

def transfer_file(client,remote_path='/',file_local_path=None):

        sftp = client.open_sftp()
        file_remote = os.path.join(remote_path,file_name)
    

        sftp.get(file_remote,file_local_path)
        print(file_local_path,">>>>",file_remote)

        sftp.close()



def execute_command(client, command,output_path):
    stdin,stdout,stderr = client.execute_command(command)

    cmd_output = stdout.read()
    print("log printing",command)
    with open(output_path,"w+") as f:
        f.write(str(cmd_output))



parser = argparse.ArgumentParser(description="SSH into a server using paramiko.")
parser.add_argument("-c","--command",type=str,help='Command to run on a sever.')
parser.add_argument("-f","--file_transfer",type=str,default="no",help="yes if want to file transfer.")
parser.add_argument("-fp","--file_path",type=str,help="Path of the file to send.")
parser.add_argument("-rp","--remote_path",type=str,default="/",help="Location on remote where the file needs to be stored.")




if __name__ == "__main__":

    host = '192.0.0.1'
    username = 'root'
    output_file = "./command.txt"
    keypath = ''
    # client = create_connection(host,username,keypath)
    args = vars(parser.parse_args())


    if args['command']:
        try:
            execute_command(client, parser['command'],output_file)

        except Exception as e:
            raise Exception("Error while executing command",parser['command'],e)

    if args['file_transfer'].lower() =='yes':

        if os.isfile(args['file_path']):

            transfer_file(client,args['remote_path'],args['file_path'])

        else:
            raise Exception("Invalid File path",args['file_path'])


    client.close()
