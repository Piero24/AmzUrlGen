# pip3 install pyTelegramBotAPI
import time
import telebot
import list_file as lf

id_list = ["YOUR-TELEGRAM-ID"]
API_TOKEN = 'YOUR-TELEGRAM-API-TOKEN'
bot = telebot.TeleBot(API_TOKEN)
stat_var = 0

@bot.message_handler(commands=lf.command_list)
def send_welcome(message):

    global stat_var
    arrived_msg = message.text.replace('/', '')

    # Effettua il typing a schermo per l'utente
    bot.send_chat_action(message.from_user.id, "typing")
    time.sleep(1)

    if message.from_user.id in id_list:

        if arrived_msg == 'list': bot.send_message(message.from_user.id, lf.str_list, parse_mode='MarkdownV2')

        elif arrived_msg == 'spiegazione': bot.send_message(message.from_user.id, lf.what_the_link_do, parse_mode='MarkdownV2')

        elif arrived_msg == 'utilizzo': bot.send_message(message.from_user.id, lf.how_to_use, parse_mode='MarkdownV2')

        elif arrived_msg in lf.command_list and arrived_msg != 'list' \
                and arrived_msg != 'spiegazione' and arrived_msg != 'utilizzo':

            if arrived_msg in ['1', '2', '3', '12', '13']:
                bot.send_message(message.from_user.id, "Inserisci un ASIN e una KEYWORD")
            elif arrived_msg in ['4']:
                bot.send_message(message.from_user.id, "Inserisci una KEYWORD")
            elif arrived_msg in ['5']:
                bot.send_message(message.from_user.id, "Inserisci un ASIN una KEYWORD e il nome del BRAND")
            elif arrived_msg in ['6']:
                bot.send_message(message.from_user.id, "Inserisci un ASIN e una quantità per ogni prodotto (da 2 a 4 prodotti)")
            elif arrived_msg in ['7', '11']:
                bot.send_message(message.from_user.id, "Inserisci un ASIN e la quantità di unità")
            elif arrived_msg in ['8']:
                bot.send_message(message.from_user.id, "Inserisci un ASIN e da 2 a 5 KEYWORD")
            elif arrived_msg in ['9', '10']:
                bot.send_message(message.from_user.id, "Inserisci un ASIN")
            elif arrived_msg in ['14']:
                bot.send_message(message.from_user.id, "Inserisci un ASIN una KEYWORD e la quantità di unità")

            stat_var = arrived_msg

    else:

        bot.send_message(message.from_user.id, "Accesso negato.")
        bot.send_chat_action(message.from_user.id, "typing")
        time.sleep(1)
        bot.send_message(message.from_user.id, "Il tuo tentativo di accesso è stato reportato.")
        bot.send_message(id_list[0], "C'è stato un tentativo di accesso non autorizzato.")
        bot.send_message(id_list[0], "ID: " + message.from_user.id + "\nTEXT: " + message.text)


@bot.message_handler(func=lambda message: True)
def echo_message(message):

    
    global stat_var
    bot.send_chat_action(message.from_user.id, "typing")
    time.sleep(1)

    if message.from_user.id in id_list:

        if message.text == 'exit': stat_var = 0

        elif stat_var == 0: bot.send_message(id_list[0], "Seleziona prima un tipo di URL")

        elif stat_var != 0:

            list_link = message.text.split('\n')
            final_link = f"https://www.amazon.it/{lf.link_list_el[int(stat_var) - 1]}"

            if stat_var in ['1', '2', '3', '12', '13']:

                try:
                    final_link = final_link.replace("*ASIN*", list_link[0].replace(' ', ''))
                    final_link = final_link.replace("*KEYWORD*", list_link[1].replace(' ', '+'))
                except:
                    bot.send_message(message.from_user.id, "Devi aver inserito i dati in modo errato.\nRiprova.")

            elif stat_var in ['4']:

                try:
                    final_link = final_link.replace("*KEYWORD*", list_link[0].replace(' ', '+'))
                except:
                    bot.send_message(message.from_user.id, "Devi aver inserito i dati in modo errato.\nRiprova.")

            elif stat_var in ['5']:

                try:
                    final_link = final_link.replace("*ASIN*", list_link[0].replace(' ', ''))
                    final_link = final_link.replace("*KEYWORD*", list_link[1].replace(' ', '+'))
                    final_link = final_link.replace("*BRAND*", list_link[2].replace(' ', '%20'))
                except:
                    bot.send_message(message.from_user.id, "Devi aver inserito i dati in modo errato.\nRiprova.")

            elif stat_var in ['6']:

                # verificare se viene inserita la prima parte del link "gp/aws/cart/add.html?"

                try:
                    for i in range(1, int(len(list_link)/2)):
                        final_link += f"ASIN.{i}=" + list_link[2*i].replace(' ', '') + \
                        f"&Quantity.{i}=" + list_link[2*i + 1].replace(' ', '') + "&"

                    final_link = final_link[:-1]
                except:
                    bot.send_message(message.from_user.id, "Devi aver inserito i dati in modo errato.\nRiprova.")

            elif stat_var in ['7', '11']:

                try:
                    final_link = final_link.replace("*ASIN*", list_link[0].replace(' ', ''))
                    final_link = final_link.replace("*QUANTITY*", list_link[1].replace(' ', ''))
                except:
                    bot.send_message(message.from_user.id, "Devi aver inserito i dati in modo errato.\nRiprova.")

            elif stat_var in ['8']:

                try:
                    for i in range(1, len(list_link)):
                        final_link += f"{list_link[i].replace(' ', '+')}-"

                    final_link = final_link[:-1]
                    final_link += f"/dp/{list_link[0].replace(' ', '')}/?maas=ampattrib"

                except:
                    bot.send_message(message.from_user.id, "Devi aver inserito i dati in modo errato.\nRiprova.")


            elif stat_var in ['9', '10']:

                try:
                    final_link = final_link.replace("*ASIN*", list_link[0].replace(' ', ''))
                except:
                    bot.send_message(message.from_user.id, "Devi aver inserito i dati in modo errato.\nRiprova.")

            elif stat_var in ['14']:

                try:
                    final_link = final_link.replace("*ASIN*", list_link[0].replace(' ', ''))
                    final_link = final_link.replace("*KEYWORD*", list_link[1].replace(' ', '+'))
                    final_link = final_link.replace("*QUANTITY*", list_link[2].replace(' ', ''))
                except:
                    bot.send_message(message.from_user.id, "Devi aver inserito i dati in modo errato.\nRiprova.")

            bot.send_message(message.from_user.id, final_link)
            stat_var = 0

    else:

        bot.send_message(message.from_user.id, "Accesso negato.")
        bot.send_chat_action(message.from_user.id, "typing")
        time.sleep(1)
        bot.send_message(message.from_user.id, "Il tuo tentativo di accesso è stato reportato.")
        bot.send_message(id_list[0], "C'è stato un tentativo di accesso non autorizzato.")
        bot.send_message(id_list[0], "ID: " + message.from_user.id + "\nTEXT: " + message.text)
    


bot.infinity_polling(timeout=10, long_polling_timeout = 5)