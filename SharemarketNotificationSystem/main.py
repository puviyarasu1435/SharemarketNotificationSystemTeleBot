from yahoo_fin import stock_info
from plyer import notification
import datetime,time
from telegram.ext import *

Apikey="< api key>" # api key bot father
brands="<brand name>" # brands name 
chat_id="<chart id>" # telegram chart id
minutes= 15 # dely of cheking price

def send(temp,price):
    notification.notify(
        title = "AMZN Share market {}".format(datetime.date.today()),
        message = f"amazon share market price increase {round(temp,2)} to {round(price,2)}",
        timeout  = 30
    )
    updater=Updater(Apikey,use_context=True)
    updater.bot.send_message(chat_id=chat_id, text=f"amazon share market price increase {round(temp,2)} to {round(price,2)}")

temp=0

while True:
    price=stock_info.get_live_price(brands)
    if price>temp:
        send(temp,price)
    temp=price
    time.sleep(60*minutes)

