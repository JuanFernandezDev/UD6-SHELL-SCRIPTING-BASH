#!/usr/bin/env python3
import os
import subprocess

usuarioApp = "UsuarioApp"
nombreGrupo = "groupApp"

def install():
    direccion = input("Donde quieres instalar el programa: ")
    #Con input recogemos los datos
    if os.path.isdir(direccion): #isdir sirve para ver si es un directorio
        print("Directorio ya existe")
    else:
        print("El directorio no existe lo creo")
        os.mkdir(direccion)
    ruta_directorio = "/home/juan/Documents/Sistemas/" + direccion
    os.system("cp pizarra.class " + ruta_directorio)

    #Con el subprocess llama hace el comando grep del directorio que se ha mandado y guarda el resultado en la variable
    result_nombre = subprocess.run(["grep", usuarioApp, "/etc/passwd"], capture_output=True)
    result_grupo = subprocess.run(["grep", nombreGrupo, "/etc/group"], capture_output=True)

    #El stdout lo que comprueba es que el resultado de hacer el run del subproceso se haya realizado con exito.
    if len(result_nombre.stdout) == 0:
        print("El usuario " + usuarioApp + " no existe, pero se crea")
        os.system("sudo useradd -d " + ruta_directorio + " -s /bin/bash " + usuarioApp)
        os.system("sudo chown -R " + usuarioApp + " " + ruta_directorio)
    else:
        print("El usuario " + usuarioApp + " existe")
    if len(result_grupo.stdout) == 0:
        print("El grupo " + nombreGrupo + " no existe, pero se crea")
        os.system("sudo groupadd " + nombreGrupo)
        os.system("sudo usermod -aG " + nombreGrupo + " " + usuarioApp)
    else:
        print("El grupo " + nombreGrupo + " existe")

    print("Instalamos el paquete JRE o actualizamos")
    os.system("sudo apt install default-jre")

install()