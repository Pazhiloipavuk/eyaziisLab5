from pathlib import Path
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
import pyttsx3

en_male_voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_MARK_11.0"
ru_male_voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_RU-RU_PAVEL_11.0"
en_female_voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
ru_female_voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_RU-RU_IRINA_11.0"

lang = "en"
voice = "male"
voice_path = ""

root=Tk()
space0 = Label(root,text='\n')
aboutButton = Button(root,text='About',width=8,height=2,bg='light grey')
space01 = Label(root,text='\n')
chooseDocButton=Button(root,text='Choose doc',width=55,height=2,bg='light grey')
space1 = Label(root,text='\nChoose language:\n')
enButton=Button(root,text='English',width=55,height=2,bg='light grey')
ruButton=Button(root,text='Russian',width=55,height=2,bg='light grey')
space2 = Label(root,text='\nEnter text:\n')
inputText = tk.Text(root, width=80, height=20)
space3 = Label(root,text='\nSelect voice:\n')
maleButton=Button(root,text='Male',width=55,height=2,bg='light grey')
femaleButton=Button(root,text='Female',width=55,height=2,bg='light grey')
space4 = Label(root,text='\n')
synthesizeButton=Button(root,text='Synthesize text to speech',width=55,height=2,bg='light grey')
space5 = Label(root,text='\n')

def chooseDocsClicked():
    files = filedialog.askopenfilename(multiple=False)
    splitlist = root.tk.splitlist(files)
    text = ""
    for doc in splitlist:
        text = Path(doc, encoding="UTF-8", errors='ignore').read_text(encoding="UTF-8", errors='ignore')
    inputText.configure(state='normal')
    inputText.delete('1.0', END)
    inputText.insert('end', text)
    inputText.configure(state='disabled')

def enButtonClicked():
    global voice_path, lang, voice
    lang = "en"
    if voice == "male":
        voice_path = en_male_voice_id
    else:
        voice_path = en_female_voice_id

def ruButtonClicked():
    global voice_path, lang, voice
    lang = "ru"
    if voice == "male":
        voice_path = ru_male_voice_id
    else:
        voice_path = ru_female_voice_id

def maleButtonClicked():
    global voice_path, lang, voice
    voice = "male"
    if lang == "en":
        voice_path = en_male_voice_id
    else:
        voice_path = ru_male_voice_id

def femaleButtonClicked():
    global voice_path, lang, voice
    voice = "female"
    if lang == "en":
        voice_path = en_female_voice_id
    else:
        voice_path = ru_female_voice_id

def synthesizeButtonClicked():
    global voice_path, lang, voice
    engine = pyttsx3.init()
    engine.setProperty('voice', voice_path)
    engine.say(inputText.get(1.0, END))
    engine.runAndWait()

def aboutButtonClicked():
    messagebox.showinfo("Lab 5", "Usage: Enter text. Then click \"Synthesize text to speech\" button.\n\nDeveloped by: Artyom Gurbovich and Pavel Kalenik.")

aboutButton.config(command=aboutButtonClicked)
chooseDocButton.config(command=chooseDocsClicked)
enButton.config(command=enButtonClicked)
ruButton.config(command=ruButtonClicked)
maleButton.config(command=maleButtonClicked)
femaleButton.config(command=femaleButtonClicked)
synthesizeButton.config(command=synthesizeButtonClicked)

space0.pack()
aboutButton.pack()
space01.pack()
chooseDocButton.pack()
space1.pack()
enButton.pack()
ruButton.pack()
space2.pack()
inputText.pack()
space3.pack()
maleButton.pack()
femaleButton.pack()
space4.pack()
synthesizeButton.pack()
space5.pack()
root.mainloop()