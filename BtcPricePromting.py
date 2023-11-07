import time
from pybit.inverse_perpetual import HTTP as htp
import telegram.ext

telegramToken = #enter your token here

updater = telegram.ext.Updater(telegramToken, use_context=True)
dispatcher = updater.dispatcher

#function to get prices from bybit and convert it to float
def getPrice():
	global price

	tme= time.time()
	tme = (tme - 12000)

	#requesting pricing information
	session = htp("https://api.bybit.com")
	price = (session.query_index_price_kline(
	    symbol="BTCUSD",
	    interval=1,
	    limit=200,
	    from_time= round(tme)
	))
	
	price = (price["result"][-1]['close'])#converting historical pricing to accurate on time prices



def sendPrice(update, context):
	getPrice()

	user = (update.message.from_user)

	#replying current price inforamtion to user
	update.message.reply_text(price)

	#write log file
	U = open("UserLog.txt", "a")
	U.write(str(user))
	U.write("\n")
	U.write("command: " + "sendPrice")
	U.write("\n")
	U.write("\n")
	U.write("\n")
	U.close()

	print("request recieved")

#defining telegram commands
dispatcher.add_handler(telegram.ext.CommandHandler("getPrice", sendPrice))
updater.start_polling()
