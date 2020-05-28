
from bs4 import BeautifulSoup as bs
import requests
import re

number_in_receipt = 2090193500
for i in range(100):
    Receipt_number = "YSC"+str(number_in_receipt+i)
    url = "https://opttimeline.com/mycase?RCPT_NUM="+Receipt_number
    response = requests.get(url)
    # print(response.text)
    if 'Unfortunately' in response.text:
        print(Receipt_number+'\t'+"Not available")
        continue
    parsed_html = bs(response.text, 'html.parser')
    splits = parsed_html.p.text.split(' ')
    print(Receipt_number+'\t'+splits[6]+'\t'+splits[11]+' '+splits[12])
