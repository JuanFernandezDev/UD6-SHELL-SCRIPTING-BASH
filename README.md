# UD6-SHELL-SCRIPTING-BASH
Sistemas Informaticos


El programa consiste en tres opciones, una para instalarlo, otra para ejecutar, y otra para desinstalarlo. La ejecucion consiste en la impresion de un documento de texto por pantalla de un color especifico, rojo, verde y amarillo.

La funcion instalar que seria con el parametro "-i" : Para instalacion, en la cual pide el directorio en el que se va a instalar el programa, se creara un usuario y grupo para la ejecucion del mismo. Se copia el archivo.class en el directorio que se ha pasado anteriormente. Se instala o actualiza el paquete default-jre para la ejecucion del programa.
     
        
La funcion ejecutar que seria con el parametro "-e" : Para la ejecucion del programa, se pide un archivo de texto al usuario y se pide una opcion de color al usuario \"R\" para rojo, \"G\" para verde, \"Y\" para amarillo. Y el programa mostrara el contenido del fichero de texto en el color deseado.
     
La funcion desintalar que seria con el parametro "-u" : Para desinstalar borramos el usuario creado y el grupo, con ello se elimina el directorio del programa ques es el home de dicho usuario. Se da la opcion de desinstalar el jre si lo desea.

Y la opcion con el parametro "-HELP" para tener una informacion mas detallada del programa


Del Actividad6.py es solo la funcion instalar del ejercicio anterior completa, que utiliza la libreria os para poder utilizar los comandos de sistema, y la libreria subprocess para poder ejecutar comando y guardarlos en variables.
