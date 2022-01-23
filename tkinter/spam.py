from tkinter import *
import tkinter
from dhooks import Webhook
import requests
import os


root = Tk()


root.title("webhook spam")
root.iconbitmap('img\kalb.ico')
root.geometry("500x300")




def spam():
    hook = Webhook(webhook.get())
    for i in range(int(num.get())):
        hook.send(msg.get())

tkinter.Label(root , text="webhook:").pack()
webhook= Entry(root, width= 40)
webhook.focus_set()
webhook.pack()

tkinter.Label(root , text="spam message:").pack()
msg= Entry(root, width= 40)
msg.focus_set()
msg.pack()

tkinter.Label(root , text="number of spam messages: #max 30").pack()
num= Entry(root, width= 40)
num.focus_set()
num.pack()



tkinter.Button(root, text= "spam",width= 20, command= spam).pack(pady=20)



root.mainloop()