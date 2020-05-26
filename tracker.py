from bs4 import BeautifulSoup as bs
from playsound import playsound
from multiprocessing import *

import requests
import re
import os
import ctypes
import time


def visual_notification(notification,status):
    reply = ctypes.windll.user32.MessageBoxW(
        0, status, "OPT Status", 1)
    notification.value = False


def audible_notification(notification,status):
    while notification.value != False:
        playsound('success.wav')
        os.system("espeak \""+"Your O.P.T is "+status+"\"")

def main():

    Receipt_number = "YSC2090193503"
    url = "https://opttimeline.com/mycase?RCPT_NUM="+Receipt_number

    response = requests.get(url)
    parsed_html = bs(response.text, 'html.parser')

    status = re.findall(r'"([^"]*)"', parsed_html.p.text )

    # print(status[0])
    if status[0] == "Received":
        playsound('failure.wav')
        # print("Still Received")
    else:
        notification = Value('b', True)
        p1 = Process(target=visual_notification, args=(notification,status[0]))
        p2 = Process(target=audible_notification, args=(notification,status[0]))

        p2.start()
        p1.start()
        p1.join()
        p2.join()

if __name__ == "__main__":
    while True:
        notification = Value('b', True)
        main()
        time.sleep(3600)  # 1 hour