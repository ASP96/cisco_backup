from Bcolors import Bcolors
from command import Command
from connector.connector_ssh import ConnectorSSH
from connector.connector_telnet import ConnectorTelnet
import os


class Cisco:
    __connector = False
    _commands = []
    __logger = False
    auth = {}
    path_config = "./_output/config"
    path_info = "./_output/info"
    _configuration = ""
    _info = ""

    def __init__(self, ip, name, connect_type, personal_auth=False, port="", **kwargs):
        self.ip = ip
        self.name = name
        self.connect_type = connect_type
        self.personal_auth = bool(personal_auth)
        self.port = port

        self.cmd_settings = [
            Command("terminal len 0")
        ]

        self.cmd_info = [
            Command("show ip int brief"),
            Command("show int status"),
            Command("show mac address-table")
        ]
        self.cmd_config = [
            Command("show inventory"),
            Command("show run | exclude ntp clock-period")
        ]

    def __str__(self):
        return f"IP: {self.ip} | name: {self.name} | connection_type: {self.connect_type}"

    def connect(self):
        if self.__connector is False:
            if self.connect_type == "ssh":
                self.__connector = "ssh"
                self.__connector = ConnectorSSH(self.ip, self.port, self.auth["username"], self.auth["password"])

            if self.connect_type == "telnet":
                self.__connector = "telnet"
                self.__connector = ConnectorTelnet(self.ip, self.port, self.auth["username"], self.auth["password"])

        # configure hardware:
        for command_setting in self.cmd_settings:
            self.cmd(command_setting.value)

    """ Добавление команды для инициализации соединения"""
    def add_setting_command(self, command):
        self.cmd_settings.append(command)
        return self

    def cmd(self, cmd):
        if self.is_connected():
            return False
        delay = 2
        if self.connect_type == "telnet":
            delay = 3

        return self.__connector.execute(cmd, delay)

    def is_connected(self):
        return self.__connector is False

    def setAuthParam(self, username, password):
        self.auth["username"] = username
        self.auth["password"] = password

    def get_configuration(self):
        result = ""
        result_array = []
        for command_configuration in self.cmd_config:
            res = self.cmd(command_configuration.value)
            command_configuration.setResult(res)
            try:
                result = result + res.decode()
            except AttributeError:
                result = result + res

            result_array.append(res)

        try:
            result = b"\n".join(result_array)
        except TypeError:
            result = "\n".join(result_array)

        self._configuration = result

        return result

    def get_info(self):
        result = ""
        result_array = []
        for cmd in self.cmd_info:
            res = self.cmd(cmd.value)
            cmd.setResult(res)
            try:
                result = result + res.decode()
            except AttributeError:
                result = result + res

            result_array.append(res)

        try:
            result = b"\n".join(result_array)
        except TypeError:
            result = "\n".join(result_array)

        self._info = result

        return result

    def save_configuration(self, data=""):
        if not data:
            data = self._configuration
        self.__save_data(data, 'config')

    def save_info(self, data=""):
        if not data:
            data = self._info
        self.__save_data(data, 'info')

    def __save_data(self, data, type):
        allow_types = ('info', 'config')
        if type not in allow_types:
            raise KeyError("Type of errors. Allow: " + ",".join(allow_types))

        tip = ""
        if type == "info":
            path_dir = self.path_info
            tip = "_info"
        if type == "config":
            path_dir = self.path_config

        path_to_file = path_dir + "/" + self.connect_type + tip + "_" + self.name + ".txt"
        print(Bcolors.cyan("\tSaved to file: " + path_to_file))

        if not os.path.exists(path_dir):
            os.makedirs(path_dir, mode=0o755)

        # remove old config file
        if os.path.exists(path_to_file):
            os.unlink(path_to_file)

        if data == "":
            # print("Saving data from self._configuration")
            data = self._configuration

        f = open(path_to_file, 'bw+')
        try:
            f.write(data)
        except TypeError:
            f.write(data.encode())
        f.close
        del f

        if not os.path.exists(self.path_config):
            print(f"::: ERROR::: configuration not save for {self.name} [{self.ip}]")

        """"
        tmp = data['config']
        tmp = re.sub(r"ntp clock-period \d+", "", tmp)  # remove timestamp
        tmp = re.sub(r"Current configuration : \d+ bytes", "", tmp)
        data['config'] = tmp   
        """
        pass