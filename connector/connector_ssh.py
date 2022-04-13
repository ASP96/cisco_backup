import paramiko
import time
from connector.connector import Connector


class ConnectorSSH(Connector):
    connect = False

    def __init__(self, ip, port, username, password):
        port = 22
        if port:
            port = port

        client = None
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # create client
        client.connect(ip,
                            port=port,
                            username=username,
                            password=password,
                            look_for_keys=False,
                            allow_agent=False)

        # init interactive shell
        self.connect = client.invoke_shell()
        output = self.connect.recv(65535)

        return

    def execute(self, command, delay=1):
        return self.command(command, delay)

    def command(self, command, delay=1, buffer=65535):
        self.connect.send(command + "\n")
        time.sleep(delay)
        output = self.connect.recv(buffer)
        return output
