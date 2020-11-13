
from os import system

print('ESTE APLICATIVO TRANSFORMA .PY EM EXE')
system('pip3 install pyinstaller')
n = input('local do arquivo: ')
system(f'pyinstaller {n}')
