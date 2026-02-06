import customtkinter as ctk
import random
import string
from bs4 import BeautifulSoup
import requests
from PIL import Image
from customtkinter import CTkEntry


pref = ""
suf = ""
nick = ""
ws = []
url = ['https://www.merriam-webster.com/thesaurus/dark', 'https://www.merriam-webster.com/thesaurus/void', 'https://www.merriam-webster.com/thesaurus/cold', 'https://www.merriam-webster.com/thesaurus/ashed', 'https://www.merriam-webster.com/thesaurus/dead', 'https://www.merriam-webster.com/thesaurus/edgy']

for link in url:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    for site in soup.find_all('span', {'class': 'syl'}):
        ws.append(site.text)

def print_nick():
    nick = f"{pref}{suf}"
    entry.delete(0, 'end')
    entry.insert(0, nick)

def generate():
    global pref, suf, nick
    suf = ""
    pref = random.choice(ws)
    nick = pref
    if if_suf.get():
        suf = random.choice(ws)
    if if_leet.get():
        nick = leet(nick)
    print_nick()

def rerol_pref():
    global pref
    pref = random.choice(ws)
    print_nick()

def rerol_suf():
    global suf
    suf = random.choice(ws)
    print_nick()

#função foi criada pela propria IDE
leet_map = {'a': '4', 'A': '4','e': '3', 'E': '3','i': '1', 'I': '1','o': '0', 'O': '0','s': '5', 'S': '5','t': '7', 'T': '7'}
def leet(new_text, chance=0.5):
    new_text = ""
    for char in new_text:
        if char in leet_map and random.random() < chance:
            new_text += leet_map[char]
        else:
            new_text += char
    return new_text

def copy():
    app.clipboard_clear()
    app.clipboard_append(entry.get())

ctk.set_appearance_mode('black')
app = ctk.CTk()
app.configure(fg_color="black")
app.title('3dgy s0ftw4r3')
app.geometry('600x500')

tittle = ctk.CTkLabel(app, text="3DGY", text_color="red", font=("Verdana", 60))
tittle.place(relx=0.02, rely=0)
sub = ctk.CTkLabel(app, text="little software to create “edgy” nicknames for games", text_color="red", font=("Consolas", 14))
sub.place(relx=0.02, rely=0.15)

btn_generate = ctk.CTkButton(app, text="generate", command=generate, text_color="white", fg_color="red", width=20, corner_radius=60)
btn_generate.place(relx=0.02, rely=0.3)
btn_pref = ctk.CTkButton(app, text="rerol prefix", command=rerol_pref, text_color="white", fg_color="red", width=20, corner_radius=60)
btn_pref.place(relx=0.02, rely=0.45)
btn_sufix = ctk.CTkButton(app, text="rerol sufix", command=rerol_suf, text_color="white", fg_color="red", width=20, corner_radius=60)
btn_sufix.place(relx=0.185, rely=0.45)
btn_leet = ctk.CTkButton(app, text="rerol leet", command=leet, text_color="white", fg_color="red", width=20, corner_radius=60)
btn_leet.place(relx=0.34, rely=0.45)
btn_copy = ctk.CTkButton(app, text="copy", command=copy, text_color="white", fg_color="red", width=20, corner_radius=60)
btn_copy.place(relx=0.53, rely=0.37)

if_leet = ctk.BooleanVar()
if_suf = ctk.BooleanVar()
check_sufix = ctk.CTkCheckBox(app, text="sufix", variable=if_suf, text_color="red", corner_radius=60)
check_sufix.place(relx=0.17, rely=0.305)
check_leet = ctk.CTkCheckBox(app, text="leet/l33t", variable=if_leet, text_color="red", corner_radius=60)
check_leet.place(relx=0.29, rely=0.305)

entry = CTkEntry(app, width=300)
entry.place(relx=0.02, rely=0.37)

app.mainloop()