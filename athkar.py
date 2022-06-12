import os
try :
    import requests,telebot,random
    from telebot import *
    from time import sleep
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install telebot')
    os.system('pip install pyTelegramBotAPI==3.7.7')
hassan = "5129335924:AAEfWBvRIe4BDminHq3fILH_y2LSCpBh8MA"
bot = telebot.TeleBot(hassan)
sudo = 1483182240
def id_ls(id):

    result = False

    file = open("ids.txt", 'r')

    for line in file:

        if line.strip()==id:

            result = True

    file.close()

    return result



def id_ls_pr(id):

    result = False

    file = open("private.txt", 'r')

    for line in file:

        if line.strip()==id:

            result = True

    file.close()

    return result



def id_ls_gr(id):

    result = False

    file = open("groups.txt", 'r')

    for line in file:

        if line.strip()==id:

            result = True

    file.close()

    return result



def id_ls_ca(id):

    result = False

    file = open("channels.txt", 'r')

    for line in file:

        if line.strip()==id:

            result = True

    file.close()

    return result



@bot.message_handler(commands=['start'])
def o(message):
	use = message.from_user.username
	ID = message.from_user.id
	ph = "https://pin.it/1mCHKyc"
	bot.send_photo(message.chat.id,ph, f"""
مرحبًا @{use}
• اهلاً بك في بوت اذكار،
•قم بأضافة البوت الى قروبك، قناتك وسيقوم البوت بنشر الاذكار
• ارسل تفعيل بوت الاجر ليتم تفعيل البوت،
ثبت الاجرُ ان شاء الله ❤️
المطور ~ @h_69053""")
@bot.message_handler(func=lambda m: True)

def d(message):

    if message.text == "send" and message.chat.id == sudo:

        r = random.randint(0, 336)

        g = requests.get("https://raw.githubusercontent.com/osamayy/azkar-db/master/azkar.json").json()

        what = "\n".join(re.findall("'category': '(.*?)', '", str(g))).splitlines()[int(r)]

        base = "\n".join(re.findall(", 'description': '(.*?)', '", str(g))).splitlines()[int(r)]

        fromm = "\n".join(re.findall("'reference': '(.*?)', '", str(g))).splitlines()[int(r)]  # 'reference': '

        what_is = "\n".join(re.findall("'zekr': '(.*?)}, {'category': '", str(g))).splitlines()[int(r)]

        done = f"{what}\n{base}\n{fromm}\n{what_is}"

        done_send = 0

        private = open("private.txt", "r").read().splitlines()

        groups = open("groups.txt", "r").read().splitlines()

        of_all = private + groups
        for one in of_all:

            try:

                if one.count("-"):

                    bot.send_message(f"{one}", done)

                else:

                    bot.send_message(one,done)

                done_send += 1

            except:

                pass

        bot.send_message(message.chat.id, f"- تم الارسال الى {done_send} عضو وشخص ومجموعة وقناة .")

    if message.text == "الاحصائيات" and message.chat.id == sudo:

        private  = open("private.txt","r",encoding="utf-8").read().splitlines()

        groups = open("groups.txt","r",encoding="utf-8").read().splitlines()


        of_all = private + groups 
        al = f"""

- الاحصائيات :



- المجموعات :{len(groups)} .

- الخاص :{len(private)} .

- الكل :{len(of_all)} .



"""

        bot.reply_to(message,al)

    name = message.from_user.first_name

    msg = message.text

    #####

    ####

    if msg ==  "تفعيل بوت الاجر" and message.chat.type == "private":

        try:

            idu = message.from_user.id

            us = str(message.chat.first_name)

            f3 = open("private.txt", 'a')

            if (not id_ls_pr(str(idu))):

                f3.write("{}\n".format(idu))

                f3.close()

                bot.reply_to(message,f"- اهلا عزيزي {name} تم تفعيل بوت الاجر بنجاح .")

            else:

                bot.reply_to(message,f"- البوت مفعل من قبل ! .")

        except Exception as err:

            bot.reply_to(message,f"- حصل خطأ !\nرمز الخطأ :\n{err}")

    if msg ==  "تفعيل بوت الاجر" and message.chat.type == "supergroup" or message.chat.type == "group":

        try:

            idu = message.chat.id

            us = str(message.chat.first_name)

            f3 = open("groups.txt", 'a')

            if (not id_ls_gr(str(idu))):

                f3.write("{}\n".format(idu))

                f3.close()

                bot.reply_to(message,f"- اهلا عزيزي {name} تم تفعيل بوت الاجر بنجاح .")

            else:

                bot.reply_to(message,f"- البوت مفعل من قبل ! .")

        except Exception as err:

            bot.reply_to(message,f"- حصل خطأ !\nرمز الخطأ :\n{err}")



@bot.channel_post_handler(func=lambda m: True)

def f(message):

    msg = message.text

    if msg == "تفعيل بوت الاجر":

        try:

            idu = message.chat.id

            us = str(message.chat.first_name)

            f = open("channels.txt", 'a')

            if (not id_ls_ca(str(idu))):

                f.write(f"{idu}\n")

                f.close()

                bot.reply_to(message, f"- اهلا عزيزي  تم تفعيل بوت الاجر بنجاح .")

            else:

                bot.reply_to(message, f"- البوت مفعل من قبل ! .")

        except Exception as err:

            bot.reply_to(message, f"- حصل خطأ !\nرمز الخطأ :\n{err}")
server.route(f'/{bot_token}', methods=['POST'])
def redirect_message():
	json_string = requests_get_data().decode("utf-8")
	update = telebot.types.update.de_json(json_string)
	bot_set_webhook(url="https://spyrxbot.herokuapp.com/"+str(bot_token))
	server.run(host="0.0.0.0",port=int(os.environ.get("PORT",5000)))

bot.infinity_polling()