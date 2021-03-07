import os
import qrcode
from telegram.ext import CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import ChatAction, InlineKeyboardMarkup, InlineKeyboardButton

INPUT_TEXT = 0

def start(update, context):

    update.message.reply_text(
        text = "Hola, Bienvenido, ¿Que desea hacer?\n\n Utiliza /qr para generar un Código qr.",
        
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = "Generar código qr", callback_data = "qr")],
            [InlineKeyboardButton(text = "Sobre los autores", url = "https://www.googl.com.do")]
        ])
    )

def qr_command_handler(update, context):
    
    update.message.reply_text("¿De que quieres el código QR?")
    
    return INPUT_TEXT

def qr_callback_handler(update, context):
   
   query = update.callback_query
   query.answer()

   query.edit_message_text(
       text = "¿De que quieres el código QR?"
   )

   return INPUT_TEXT

def generate_qr(text):

    filename = text + ".jpg"
    
    img = qrcode.make(text)
    
    img.save(filename)

    return filename

def sed_qr(filename, chat):

    chat.send.action(
        action = ChatAction.upload_photo,
        timeout = None
    )

    chat.send_photo(
        photo = open(filename, 'rb')
    )

    os.unlink(filename)

def input_text(update, context):
    
    text =  update.message.text
    
    filename = generate_qr(text)
    
    chat = update.message.chat
    
    send_qr(filename, chat)

    return ConversationHandler.END

if __name__ == "__main__":
    
    updater = Updater(token = "1506443426:AAHW6mxxM18pBi85Wpd5sgUPFmFB6QCHo-M", use_context = True) 

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(ConversationHandler(
        entry_points = [
            CommandHandler("qr", qr_command_handler),
            CallbackQueryHandler(pattern = "qr", callback = qr_callback_handler)
        ],

        states = {
            INPUT_TEXT: [MessageHandler(Filters.text, input_text)]
        },

        fallbaks = []        
    ))

    updater.start_polling()
    updater.idle()




TOKEN=("1506443426:AAHW6mxxM18pBi85Wpd5sgUPFmFB6QCHo-M")
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Estoy escuchando...')