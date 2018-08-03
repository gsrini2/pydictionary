# -*- coding: utf-8 -*-
"""

@author: Srinivasan 
e-mail : gsrini2@yahoo.com

"""
import time
from tkinter import Tk
import requests,re
from bs4 import BeautifulSoup
import fnotify as fn

http_proxy="your proxy here"
https_proxy="your proxy here"
proxy_dict={"http":http_proxy, "https":https_proxy}

prevword = ''

def find_meaning(wd):
    link='https://www.dictionary.com/browse/'+wd
    page = requests.get(link,proxies=proxy_dict)
    soup = BeautifulSoup(page.content,'html.parser')
    content = soup.select('section')
    title = content[0].h1.text
    spelt_as = content[0].div.span.text
    meaning_title1 = content[0].header.span.text
    meaning1 = content[0].ol.li.span.text
    msg = "Spelt as:"+spelt_as+"\n"+"-"+meaning_title1+"\n"+meaning1
    return msg

while True:
    r = Tk()
    try:
        word = r.selection_get(selection="CLIPBOARD")
        if((prevword != word)and(len(word)<50)):
            print(word)
            message = find_meaning(word)
            fn.balloon_tip(word,message)
            prevword = word
        time.sleep(1)
    except:
        selection = None
