import customtkinter as ctk
import random
import string
from bs4 import BeautifulSoup
import requests

if_suf = bool(1)
ws = []
url = ['https://www.merriam-webster.com/thesaurus/dark', 'https://www.merriam-webster.com/thesaurus/void', 'https://www.merriam-webster.com/thesaurus/cold', 'https://www.merriam-webster.com/thesaurus/ashed', 'https://www.merriam-webster.com/thesaurus/dead', 'https://www.merriam-webster.com/thesaurus/edgy']
for link in url:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    for site in soup.find_all('span', {'class': 'syl'}):
        ws.append(site.text)

if_leet = bool(1)
leet_map = {'a': '4', 'A': '4','e': '3', 'E': '3','i': '1', 'I': '1','o': '0', 'O': '0','s': '5', 'S': '5','t': '7', 'T': '7'}
def leet(text, chance=0.5):
    new_text = ''
    for char in text:
        if char in leet_map and random.random() < chance:
            new_text += leet_map[char]
        else:
            new_text += char
    return new_text

def generate():
    pref = random.choice(ws)
    if if_suf:
        suf = random.choice(ws)
    nick = f"{pref}{suf}"
    print(pref)
    print(suf)
    print(nick)
    if if_leet:
        nick = leet(nick)
    print(nick)

ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title('3dgy s0ftw4r3')
app.geometry('600x600')
title = ctk.CTkLabel(app,text='3dgy')
title.pack(pady=30)
btGenerate = ctk.CTkButton(app,text='Generate',command=generate)
btGenerate.pack(pady=10)
printGenerate = ctk.CTkLabel(app,text='')
printGenerate.pack(pady=10)
app.mainloop()