import time
import requests
import os
# import datetime as dt
# import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

BOT_TOKEN = os.environ.get('BOT_TOKEN')

# checking status every 2 hours
SLEEP_INTERVAL = 7200
FINANCE_URL = "http://resources.finance.ua/ua/public/currency-cash.json"
sched = BlockingScheduler()


def send_telegram(dollar):
    # chat = "-383060434"
    # chat_test = "-277675492"
    chat_viki = "232590195"
    # bot = telegram.Bot(token=token)
    # print(bot.get_me())
    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={chat_viki}&text=Hallo Tiere!🐱🐰%20Dollar={dollar}.\nMehr%20unter%20https://crystalbank.com.ua/")


while True:
    print("Ok")
    sent_weekly = 0
    myResponse = requests.get(FINANCE_URL)
    if myResponse.status_code != 200:
        print('Not Found.')

    content = myResponse.json()
    date = content["date"]

    # if dt.date.today().isoweekday() == 2:
    #     print("Sending weekly...")

    for bank in content["organizations"]:
        if bank["id"] == "7oiylpmiow8iy1smgg3":
            usd = float(bank["currencies"]["USD"]["ask"])
            send_telegram(usd)

            #every monday
            # if dt.date.today().isoweekday() == 1:
            #     print("Sending weekly...")
            #     send_telegram(usd)
                # sent_weekly = 1
            # else:
                # sent_weekly = 0
            #if is interesting
            if 26.40 < usd < 26.96:
                print("Sending message...")
                send_telegram(usd)

    print("Sleeping for {} seconds".format(SLEEP_INTERVAL))
    time.sleep(SLEEP_INTERVAL)
