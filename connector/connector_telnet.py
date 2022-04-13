from telnetlib import Telnet
import time
from connector.connector import Connector


class ConnectorTelnet(Connector):
    connect = False

    def __init__(self, ip, port, username, password):
        port = 23
        if port:
            port = port

        try:
            client = Telnet(ip, port, timeout=15)
        except:
            print(f"Unable to connect to Telnet {ip}")
            return

        # client.set_debuglevel(100)
        # print(client.read_all())

        client.read_until(b"Username: ", 10)

        client.write(username.encode("ascii") + b"\n")
        client.read_until(b"Password: ", 10)
        client.write(password.encode("ascii") + b"\n")

        time.sleep(1)
        self.connect = client
        time.sleep(2)

    def execute(self, command, delay=1):
        return self.command(command, delay)

    def command(self, command, delay=1, buffer=65535):
        # print("Debug:   len=", len(self.connect.read_very_eager().decode('ascii')))
        # print(f"\t ++++++++++++++++++Command: {command}")

        self.connect.write(command.encode("ascii"))
        self.connect.write(b"\n")
        time.sleep(delay)

        result = self.connect.read_very_eager().decode('ascii')
        # print("+++++++++++++++Debug:   ", len(result))
        # print("+++++++++++++++Debug:   ", result)

        self.connect.write(b"\n")
        time.sleep(delay)

        return result
