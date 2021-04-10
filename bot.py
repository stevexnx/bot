import datetime
import telepot
import os
import time
import sys

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def start(command):
        try:
            bot.sendMessage(chat_id,("Bienvenido"))
            bot.sendMessage(chat_id,("Puedes utilizar los siguientes comandos: \n"))
            bot.sendMessage(chat_id,("1) /ingresar + (tu matrícula). Para agregarte a la cola."))
            bot.sendMessage(chat_id,("2) /consultar + (tu matrícula). Para consultar tu numero de ticket."))
            bot.sendMessage(chat_id,("3) /borrar + (tu matrícula). Para eliminarte de la lista."))
        except(TypeError, NameError, ValueError):
            bot.sendMessage("Ha habido algún error. \nCodigo #S1. Si persiste, comuniquese con el administrador.")
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def ingresar(command):
        try:
            datos=command.split()
            placa=int(datos[1])
            if len(reg)<10:
                reg.append(placa)
                bot.sendMessage(chat_id, ("Usted a sido añadido satisfactoriamente."))
                bot.sendMessage(chat_id, reg)
            else:
                bot.sendMessage(chat_id ,"No quedan asientos.")
        except(TypeError, NameError, ValueError):
            bot.sendMessage(chat_id,"Ha habido algún error. \nCodigo #I1. Si persiste, comuniquese con el administrador.")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def consultar(command):
        try:
            comp=command.split()
            c=int(comp[1])
            if c in reg:
                bot.sendMessage(chat_id,"Usted ya esta registrado.")
            else:
                bot.sendMessage(chat_id, "Usted aún no esta registrado.")
        except(TypeError, NameError, ValueError):
            bot.sendMessage(chat_id,"Ha habido algún error. \nCodigo #C1. Si persiste, comuniquese con el administrador.")
            
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def borrar(command):#funcion para borrar un articulo
        try:
            comp=command.split()
            c=int(comp[1])
            if c in reg:
                reg.remove(c)
                bot.sendMessage(chat_id,"Usted ha sido eliminado satisfactoriamente.")
            else:
                bot.sendMessage(chat_id, "Usted no esta registrado.")
        except(TypeError, NameError, ValueError):
            bot.sendMessage(chat_id,"Ha habido algún error. \nCodigo #B1. Si persiste, comuniquese con el administrador.")
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    lista1=['/start','/ingresar','/consultar','/borrar']
    div=command.split()
    comparacion = []
    for item in lista1:
        if item in div:
            comparacion.append(item)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    try:
        if command==("/start"):#Para inicar el bot#
            start(command)#la funcion tiene los valores de entrada del id de la persona y el objeto bot, para no utilizaro 2 veces#
        elif comparacion[0]==("/ingresar"):#Para comprar un ticket#
            ingresar(command)#Solo es posible infresar caracteres numericos#
        elif comparacion[0]==("/consultar"):#Para consultar si has comprado un ticket#
            consultar(command)#Se debe ingresar la matricula.
        elif comparacion[0]==("/borrar"):#Para borrar tu compra#
            borrar(command)#Se debe ingresar la matricula que se quiere borrar#
    except(IndexError):
        bot.sendMessage(chat_id, ("Ha habido algún error. \nCodigo. #CM.Error. Si persiste, comuniquese con el administrador."))
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#


TOKEN=("1506443426:AAHW6mxxM18pBi85Wpd5sgUPFmFB6QCHo-M")
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Estoy escuchando...')


while 1:
     time.sleep(10)
