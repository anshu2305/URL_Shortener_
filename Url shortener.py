#!/usr/bin/env python
# coding: utf-8

# # URL shortener in Python



import tkinter as tk
from tkinter import font

def shorturl(event):
    shorten=pyshorteners.Shortener()
    x=shorten.tinyurl.short(entry.get())
    res.configure(text = "Your link is : " + x,fg="green",font="Helvetica 10")


w = tk.Tk()
w.geometry("450x200")
w.title("URL Shortener")
tk.Label(w, text="URL Shortener", font="Helvetica 11 bold",fg="Red" ).pack(side="top")
tk.Label(w).pack()
tk.Label(w, text="Enter the link: ", font="Helvetica 10").pack()
w.resizable(False, False)
entry = tk.Entry(w)
entry.bind("<Return>", shorturl)
entry.pack()
tk.Label(w, text="Press Enter to see the results", font="Helvetica 10").pack()
res = tk.Label(w)
res.pack()
btn = tk.Button(w, text = '  Exit  ', bd = '3', command = w.destroy)      
btn.place(x=200,y=150) 
w.mainloop()

