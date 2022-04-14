# -*- coding: utf-8 -*-
import sys
from getpass import getpass
from importlib import reload
import time
import inventory
import shutil
from Bcolors import Bcolors

reload(sys)

debug = 1



def start():
    if debug == 0:
        showCommandName = 1
        username = 'asp'
        password = getpass("Enter password fo username " + username + ": ")
    else:
        showCommandName = int(input(Bcolors.warning("\tDebug: show command name? [0 / 1] :\t")))
        username = input("Enter default username for hardware :   ")
        password = getpass()

    i = 1
    hardwares = []
    for hw in inventory.hardwares:
        hw.setAuthParam(username, password)

        current_time = time.strftime("%H:%M:%S")
        print(f"# {i}.\t {current_time} \t {hw.name} [{hw.ip}].\tConnection_type: {hw.connect_type}\t\t" + Bcolors.green("OK"))
        i = i + 1

        if hw.personal_auth:
            set_personal_auth(hw)

        hw.connect()
        hardwares.append(hw)

    print("\n\n")

    i = 1
    for hw in hardwares:
        current_time = time.strftime("%H:%M:%S")
        print(f"# {i}.\t{current_time} {hw.name} [{hw.ip}].\tConnection_type: {hw.connect_type}. Process backup...")
        i = i + 1
        configuration = hw.get_configuration()
        info = hw.get_info()
        hw.save_configuration()
        hw.save_info()

    return True


def set_personal_auth(hw):
    template = "Enter {0} for {1} [{2}] :   "
    username = input(template.format("username", hw.name, hw.ip))
    password = getpass(template.format("password", hw.name, hw.ip))
    hw.setAuthParam(username, password)


def log(value):
    if debug:
        print("::: LOG: " + value)


if __name__ == "__main__":
    start()
