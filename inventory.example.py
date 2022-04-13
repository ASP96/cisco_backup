from hardware.cisco_switch import CiscoSwitch
from hardware.cisco import Cisco
from hardware.watchguard import Watchguard
from command import Command

router_1 = Cisco("10.10.10.1", "router_1", "ssh", personal_auth=True)
router_1.add_setting_command(Command("en")).add_setting_command(Command("pass_for_enable"))

router_2 = Cisco("10.10.10.2", "router_2", "ssh", personal_auth=True)
router_2.add_setting_command(Command("en"))

hardwares = [
    router_1,
    router_2,

    # Building #1
    CiscoSwitch("10.20.20.1", "sw1", "ssh"),
    CiscoSwitch("10.20.20.2", "sw2", "telnet"),

    ## Object #2
    CiscoSwitch("10.30.30.1", "sw1-obj2", "telnet"),

    ## Routers

    {"name": "ro1", "ip": "10.20.30.1", "tip": "ssh", "asklogin": 1, "cmds": ["en"]},
    {"name": "ro2", "ip": "10.20.30.2", "tip": "ssh", "asklogin": 1},
]
