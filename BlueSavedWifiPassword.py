import os
import subprocess

def Limpieza():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def Menu():
    print('''
██████╗ ██╗     ██╗   ██╗███████╗    ███████╗ █████╗ ██╗   ██╗███████╗██████╗
██╔══██╗██║     ██║   ██║██╔════╝    ██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
██████╔╝██║     ██║   ██║█████╗      ███████╗███████║██║   ██║█████╗  ██║  ██║
██╔══██╗██║     ██║   ██║██╔══╝      ╚════██║██╔══██║╚██╗ ██╔╝██╔══╝  ██║  ██║
██████╔╝███████╗╚██████╔╝███████╗    ███████║██║  ██║ ╚████╔╝ ███████╗██████╔╝
╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝    ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═════╝

██╗    ██╗██╗███████╗██╗
██║    ██║██║██╔════╝██║
██║ █╗ ██║██║█████╗  ██║
██║███╗██║██║██╔══╝  ██║
╚███╔███╔╝██║██║     ██║
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝

██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝

[-] Sources | https://github.com/lSources [-]

[════════════════════════════════════════════════════════════════════════════]
''')

def Windows():
    print('Estas son todas las redes guardadas en el computador, cada con su respectiva contraseña:')
    print('')

    comandows = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
    redws = [i.split(":")[1][1:-1] for i in comandows if "Perfil de todos los usuarios" in i]

    for i in redws:
        try:
            pwdws = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            pwdws = [b.split(":")[1][1:-1] for b in pwdws if "Contenido de la clave" in b]
            try:
                print("{:<20} -    {:<}".format(i, pwdws[0]))
            except IndexError:
                print("{:<20} -    {:<}".format(i, ""))

        except subprocess.CalledProcessError:
            print("{:<20} -    {:<}".format(i, "Error de codificacion"))

    print('')
    print('[════════════════════════════════════════════════════════════════════════════]')
    print('')

def Linux():
    os.chdir('/etc/NetworkManager/system-connections')
    print('Estas son las redes guardadas en el computador:')
    print('')
    os.system('ls')

    print('')
    print('[════════════════════════════════════════════════════════════════════════════]')
    print('')
    redlx = input('Ingrese el nombre de la red de la cual quiere extraer la contraseña: ')
    comandolx = 'cat ' +redlx+ ' | grep -oP "psk=\K.*"'

    tomarPassword =  subprocess.Popen(comandolx, shell=True, stdout=subprocess.PIPE).stdout
    pwd =  tomarPassword.read()

    Limpieza()
    print('La contraseña de la red"' +redlx+ '"es: ',pwd.decode())

try:
    if os.name == 'nt':
        Limpieza()
        Menu()
        Windows()
        input("Presione cualquier tecla para salir...")
        print('')
        print('[════════════════════════════════════════════════════════════════════════════]')
        exit('')
    else:
        Limpieza()
        Menu()
        Linux()
        input("Presione cualquier tecla para salir...")
        print('')
        print('[════════════════════════════════════════════════════════════════════════════]')
        exit('')

except KeyboardInterrupt:
    print('\n')
    print('[════════════════════════════════════════════════════════════════════════════════════════════]')
    print('')
    print('Cerrando programa...')
    print('')
    print('[════════════════════════════════════════════════════════════════════════════════════════════]')
    exit('')
