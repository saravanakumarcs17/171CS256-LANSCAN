#!/usr/bin/python
# -*- coding: utf-8 -*-
# Xerosploit banners

import random

header1 = """  

 ██▓    ▄▄▄      ███▄    █   ██████  ▄████▄  ▄▄▄      ███▄    █
▓██▒   ▒████▄    ██ ▀█   █ ▒██    ▒ ▒██▀ ▀█ ▒████▄    ██ ▀█   █
▒██░   ▒██  ▀█▄ ▓██  ▀█ ██▒░ ▓██▄   ▒▓█    ▄▒██  ▀█▄ ▓██  ▀█ ██▒
▒██░   ░██▄▄▄▄██▓██▒  ▐▌██▒  ▒   ██▒▒▓▓▄ ▄██░██▄▄▄▄██▓██▒  ▐▌██▒
░██████ ▓█   ▓██▒██░   ▓██░▒██████▒▒▒ ▓███▀  ▓█   ▓██▒██░   ▓██░
░ ▒░▓   ▒▒   ▓▒█░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░░ ░▒ ▒   ▒▒   ▓▒█░ ▒░   ▒ ▒
░ ░ ▒    ░   ▒▒ ░ ░░   ░ ▒░░ ░▒  ░    ░  ▒    ░   ▒▒ ░ ░░   ░ ▒░
  ░ ░    ░   ▒     ░   ░ ░ ░  ░  ░  ░         ░   ▒     ░   ░ ░
    ░        ░           ░       ░  ░ ░           ░           ░        
"""

header2 = """

██╗      █████╗ ███╗   ██╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
██║     ██╔══██╗████╗  ██║    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██║     ███████║██╔██╗ ██║    ███████╗██║     ███████║██╔██╗ ██║
██║     ██╔══██║██║╚██╗██║    ╚════██║██║     ██╔══██║██║╚██╗██║
███████╗██║  ██║██║ ╚████║    ███████║╚██████╗██║  ██║██║ ╚████║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝                                                   
"""

header3 = """

    ( )   (  _  )( ) ( )   (  _ \ (  _ \(  _  )( ) ( )
 | |   | (_) ||  \| |   | (_(_)| ( (_) (_) ||  \| |
 | |  _(  _  )|     |    \__ \ | |  _(  _  )|     |
 | |_( ) | | || | \ |   ( )_) || (_( ) | | || | \ |
 ((___/(_) (_)(() (_)    \(___)(____/(_) (_)(() (_)
 (_)          (_)        (_)                (_)  
"""

header4 = """
 _____         __      ____  _____ \033[1;36m     _______   ______      __      ____  ____\033[1;m
|_   _|       /  \    |_   \|_   _|\033[1;36m  /  ___  |./ ___  |    /  \    |_   \|_     \033[1;m
  | |        / /\ \     |   \ | |  \\033[1;36m|  (__ \_| ./   \_|   / /\ \     |   \ | |\033[1;m
  | |   _   / ____ \    | |\ \| |  \033[1;36m  '.___\-.| |         / ____ \    | |\ \| |\033[1;m
 _| |__/ |_/ /    \ \_ _| |_\   |_ \033[1;36m/|\\____) | \.___.'\_/ /    \ \_ _| |_\   |\033[1;m
|________|____|  |____|_____|\____|\033[1;36m |_______.'\._____.'____|  |____|_____|\___\\033[1;m
"""



def xe_header():
    headers = [header1, header2, header3, header4]
    return random.choice(headers)
