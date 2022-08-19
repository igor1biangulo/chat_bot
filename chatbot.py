import telebot


CHAVE_API = "sua chave api"
bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, f"entre em contato comigo atravez do do\nemail: /igorbiangulo@gmail.com\nwhatszapp: /(61) 99250-5278 ")
    print(f"{mensagem.chat.id}")

"""===============================parte tabuada===================================="""
@bot.message_handler(commands=["2"])                                                #|
def mult(mensagem):                                                                 #|
    print("asd")                                                                    #|
    for i in range(1,11):                                                           #|
        x=2                                                                         #|
        bot.send_message(mensagem.chat.id,f"{x}*{i}={x*i} ")                        #|
        i+=1                                                                        #|
                                                                                    #|
@bot.message_handler(commands=["3"])                                                #|
def mult(mensagem):                                                                 #|
    print("asd")                                                                    #|
    for i in range(1,11):                                                           #|
        x=3                                                                         #|
        bot.send_message(mensagem.chat.id,f"{x}*{i}={x*i} ")                        #|
        i+=1                                                                        #|
@bot.message_handler(commands=["4"])                                                #|
def mult(mensagem):                                                                 #|
    print("asd")                                                                    #|
    for i in range(1,11):                                                           #|
        x=4                                                                         #|
        bot.send_message(mensagem.chat.id,f"{x}*{i}={x*i} ")                        #|
        i+=1                                                                        #|
@bot.message_handler(commands=["5"])                                                #|
def mult(mensagem):                                                                 #|
    print("asd")                                                                    #|
    for i in range(1,11):                                                           #|
        x=5                                                                         #|
        bot.send_message(mensagem.chat.id,f"{x}*{i}={x*i} ")                        #|
        i+=1                                                                        #|
@bot.message_handler(commands=["6"])                                                #|
def mult(mensagem):                                                                 #|
    print("asd")                                                                    #|
    for i in range(1,11):                                                           #|
        x=6                                                                         #|
        bot.send_message(mensagem.chat.id,f"{x}*{i}={x*i} ")                        #|
        i+=1                                                                        #|
@bot.message_handler(commands=["6"])                                                #|
def mult(mensagem):                                                                 #|
    print("asd")                                                                    #|
    for i in range(1,11):                                                           #|
        x=6                                                                         #|
        bot.send_message(mensagem.chat.id,f"{x}*{i}={x*i} ")                        #|
        i+=1                                                                        #|
@bot.message_handler(commands=["7"])                                                #|         
def mult(mensagem):                                                                 #|
    print("asd")                                                                    #|
    for i in range(1,11):                                                           #|
        x=7                                                                         #|
        bot.send_message(mensagem.chat.id,f"{x}*{i}={x*i} ")                        #|
        i+=1                                                                        #|
@bot.message_handler(commands=["8"])                                                #|
def mult(mensagem):                                                                 #|
    print("asd")                                                                    #|
    for i in range(1,11):                                                           #|
        x=8                                                                         #|
        bot.send_message(mensagem.chat.id,f"{x}*{i}={x*i} ")                        #|
        i+=1                                                                        #|
@bot.message_handler(commands=["9"])                                                #|
def mult(mensagem):                                                                 #|
    print("asd")                                                                    #|
    for i in range(1,11):                                                           #|
        x=9                                                                         #|
        bot.send_message(mensagem.chat.id,f"{x}*{i}={x*i} ")                        #|
        i+=1                                                                        #|
@bot.message_handler(commands=["10"])                                               #|
def mult(mensagem):                                                                 #|
    print("asd")                                                                    #|
    for i in range(1,11):                                                           #|
        x=10                                                                        #|
        bot.send_message(mensagem.chat.id,f"{x}*{i}={x*i} ")                        #|
        i+=1                                                                        #|
#====================================================================================# 
                                  
@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
   escolha quam tabuada vc quer ver
    _____________________________
    |/2|/3|/4|/5|/6|/7|/8|/9|/10|
    
    """
    bot.send_message(mensagem.chat.id, texto)


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
   ola aqui e o cygnus esse e o teste 001 do chat bot
    clique em alguma das opçoes
    /opcao1 tabuada
    /opcao2 entrar em contato comigo
    """
    bot.reply_to(mensagem,texto)

bot.polling()

