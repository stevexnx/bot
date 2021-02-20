import datetime
import telepot
import os
import time

global reg
reg=[]

def handle(msg):
    #registros=[]
    chat_id = msg['chat']['id']
    command = msg['text']
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def start():
        try:
            username = bot.getChat(user_name) 
            bot.sendMessage(chat_id,("Bienvenido" + username + "Bot de tickets"))
            bot.sendMessage(chat_id,("Puedes utilizar los siguientes comandos: \n"))
            bot.sendMessage(chat_id,("1) /ingresar + (tu matrícula).  Para agregarte a la cola."))
            bot.sendMessage(chat_id,("2) /consultar + (tu matrícula). Para consultar tu numero de ticket."))
            bot.sendMessage(chat_id,("3) /borrar + (tu matrícula).    Para eliminarte de la lista."))
        except(TypeError, NameError, ValueError):
            bot.sendMessage(chat_id,"No envie una cadena donde vaa un entero")
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def Ingresar_Articulo(command):
        try:
            datos=command.split()
            placa=int(datos[1])
            if len(reg)<10:
                reg.append(placa)
                bot.sendMessage(chat_id, ("Usted a sido añadido con exito"))
                bot.sendMessage(chat_id, reg)
            else:
                bot.sendMessage(chat_id ,"No quedan asientos")
        except(TypeError, NameError, ValueError):
            bot.sendMessage(chat_id,"No envie una cadena donde debe ir un entero")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def Consultar_Articulo(command):
        try:
            comp=command.split()
            c=int(comp[1])
            if c in reg:
                bot.sendMessage(chat_id,"Usted esta registrado")
            else:
                bot.sendMessage(chat_id, "Usted no esta registrado")
        except(TypeError, NameError, ValueError):
            bot.sendMessage(chat_id,"No envie una cadena donde va un entero")
            
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def Borrar(command):#funcion para borrar un articulo
        try:
            comp=command.split()
            c=int(comp[1])
            if c in reg:
                reg.remove(c)
                bot.sendMessage(chat_id,"Usted ha salido de la cola")
            else:
                bot.sendMessage(chat_id, "Usted no esta registrado")
        except(TypeError, NameError, ValueError):
            bot.sendMessage(chat_id,"No envie una cadena donde vaa un entero")
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    lista1=['/ingresar','/consultar','/borrar']
    div=command.split()
    comparacion = []
    for item in lista1:
        if item in div:
            comparacion.append(item)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    try:
        if command==("/start"):#comparo y decido que funcion se ejecutara, para el caso de /start, como no contiene valores de entrada de usuario va directo
            start()#la funcion tiene los valores de entrada del id de la persona y el objeto bot, para no utilizaro 2 veces
        elif comparacion[0]==("/ingresar"):#a esta funcion le envio command porque las cosas llegan por ejemplo
            Ingresar_Articulo(command)#/Ingresar 123(codigo) 25(cantidad) 100(precio) zapatos(nombre)
        elif comparacion[0]==("/consultar"):#para diferenciar eso hago lo del .split()
            Consultar_Articulo(command)#haci con todas las funciones similares
        elif comparacion[0]==("/borrar"):
            Borrar(command)
    except(IndexError):
        bot.sendMessage(chat_id, ("Ingreso una funcion no valida"))
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#


TOKEN=("1506443426:AAHW6mxxM18pBi85Wpd5sgUPFmFB6QCHo-M")
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Estoy escuchando...')


while 1:
     time.sleep(10)
