import telegram
import pyautogui

TOKEN = 'сюда токен бота'
bot = telegram.Bot(token=TOKEN)


def send_screenshot(chat_id): #вставить вместо chat_id свой айди тг
    screenshot = pyautogui.screenshot()
    bot.send_photo(chat_id=chat_id, photo=screenshot)


def handle_message(update, context):

    chat_id = update.message.chat_id

    #
    send_screenshot(chat_id)


updater = telegram.ext.Updater(TOKEN)


dispatcher = updater.dispatcher


dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))


updater.start_polling()
updater.idle()
