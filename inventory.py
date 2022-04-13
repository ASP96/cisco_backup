from hardware.cisco_switch import CiscoSwitch
from hardware.cisco import Cisco
from hardware.watchguard import Watchguard
from command import Command


ro1 = Cisco("10.239.5.101", "ro1", "ssh", personal_auth=True)
ro1.add_setting_command(Command("en")).add_setting_command(Command("cisco"))

ro2 = Cisco("10.239.5.102", "ro2", "ssh", personal_auth=True)
ro2.add_setting_command(Command("en"))


hardwares3 = [
    ## PPP
    CiscoSwitch("10.113.77.31", "ppp-center", "telnet"),
    CiscoSwitch("10.113.77.32", "ppp-left", "telnet"),
    CiscoSwitch("10.113.77.33", "ppp-right", "telnet"),
    CiscoSwitch("10.113.77.34", "ppp-k202", "telnet"),
    CiscoSwitch("10.113.77.35", "ppp-stm", "telnet"),
]

hardwares4 = [
    Watchguard("10.113.7.1", "watchguard", "ssh", personal_auth=True)
]

hardwares = [
    # ro1,
    # ro2,
    # USSI
    # k428
    CiscoSwitch("10.113.77.11", "ussi-k428-sw1", "ssh"),
    # CiscoSwitch("10.113.77.14", "sw4", "ssh", personal_auth=True),
    CiscoSwitch("10.113.77.14", "ussi-k428-sw4", "ssh"),
    CiscoSwitch("10.113.77.15", "ussi-k428-sw5", "ssh"),
    # CiscoSwitch("10.113.77.19", "ussi-519", "ssh"),
    CiscoSwitch("10.113.77.16", "ussi-k422-core", "telnet"),
    CiscoSwitch("10.113.77.18", "ussi-k207-ns", "telnet"),

    ## mIstok
    CiscoSwitch("10.113.77.61", "m_istok-kinozal", "ssh"),
    # {"name":"mistok-mainhouse", "ip":"10.113.77.62", "tip":"telnet"},

    ## PPP
    CiscoSwitch("10.113.77.31", "ppp-center", "telnet"),
    CiscoSwitch("10.113.77.32", "ppp-left", "telnet"),
    CiscoSwitch("10.113.77.33", "ppp-right", "telnet"),
    CiscoSwitch("10.113.77.34", "ppp-k202", "telnet"),
    CiscoSwitch("10.113.77.35", "ppp-stm", "telnet"),
    # GFI
    CiscoSwitch("10.113.77.41", "gfi", "ssh"),

    ## Priemnaya
    CiscoSwitch("10.113.77.51", "priemnaya", "telnet"),

    # Whitehouse
    CiscoSwitch("10.113.77.52", "whitehouse", "ssh"),

    # RGSO
    CiscoSwitch("10.113.77.71", "rgso", "ssh")

    ## Routers

    # {"name":"ro2", "ip":"10.240.80.83", "tip":"ssh", "asklogin":1, "cmds": ["en"]},
    # {"name":"ro2", "ip":"10.113.0.17", "tip":"ssh", "asklogin":1},
]
