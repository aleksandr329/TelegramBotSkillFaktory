import telebot
from telebot import types
from parameters import *
from extensions import *



bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'] )
def start(message):
    text = 'данный <b>телеграмБОТ</b> умеет конвертировать курсы валют такие как <b>рубль, доллар, евро, биткоин,</b> если у вас возникла проблема ввода нажмите ' \
           'команду /help где <b>БОТ</b> вам покажет как правильно ввести данные'
    bot.send_message(message.chat.id, f'Приветствую тебя {message.from_user.first_name}, {text}', parse_mode='HTML')


@bot.message_handler(commands = ['help'] )
def help(message):
    text = 'Если вы хотите узнать сколько евро в биткоине нужно ввести данные следующим образом ' \
           '<b>биткоин евро </b>'
    bot.send_message(message.chat.id, text, parse_mode='HTML')


@bot.message_handler(commands = ['values'] )
def info(message):
    s = ' , '.join(nam.keys())
    text = f'На сегодня доступны следующие виды валют - {s}'
    bot.send_message(message.chat.id, text)




@bot.message_handler()
def convert(message):
    value = message.text.split(' ')
    try:
        if len(value) != 2:
            raise EnterErorr('Вы ввели неправильное количество символов нажмите команду /help')
        base, quote = value

        x = Valuta(base, quote)
        base2 = x.get_price()
        bot.send_message(message.chat.id, f'В одном {base}, содержится {base2}, {quote} ')
    except EnterErorr:
        bot.send_message(message.chat.id, 'Ошибка ввода пользователя вы ввели некоректное количество символов. Нажмите команду /help ')
    except ValueError:
        bot.send_message(message.chat.id, 'Ошибка ввода пользователя вы ввели некоректное количество символов. Нажмите команду /help ')
    except KeyError:
        bot.send_message(message.chat.id, 'Ошибка ввода пользователя вы ввели некоректное количество символов. Нажмите команду /help ')




if __name__ == "__main__":
    bot.polling(none_stop=True)