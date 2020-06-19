# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 20:01:20 2020

@author: MAYANK SHAW
"""


# pip install pyttsx3 pypiwin32
import pyttsx3
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as sct
from time import sleep

# One time initialization
engine = pyttsx3.init()

# Set properties _before_ you add things to say
engine.setProperty('rate', 100)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1

class GUI:
    def __init__(self):
        self.win = tk.Tk()
        self.text = tk.StringVar()
        self.win.title('Text to speech converter')
        self.win.resizable(False, False)

        self.body_frame = ttk.Frame(self.win)
        self.body_frame.grid(row=0, column=0)

        tk.Label(self.body_frame, text='Enter Any Text:', bd=10).grid(row=0, column=0, sticky=tk.W)
        self.input_box = ttk.Entry(self.body_frame, textvariable=self.text, width=50)
        self.input_box.grid(row=1, column=0, padx=8, pady=1, columnspan=3, sticky='WE')
        self.convert_btn = ttk.Button(self.body_frame, text='Convert to voice', command=self.convert_to_speech)
        self.convert_btn.grid(row=2, column=0, padx=5, pady=5, columnspan=3)

        self.sc = sct.ScrolledText(self.body_frame, width=40, height=10)
        self.sc.grid(row=3, column=0, columnspan=3, padx=5, pady=5)


    def sys_reply(self):
        user_txt = str(self.text.get()).lower()
        if user_txt == 'how are you':
            self.sc.insert(tk.INSERT, '[SYSTEM] : '+'I am fine'+'\n')
        elif user_txt == 'are you alive':
            self.sc.insert(tk.INSERT, '[SYSTEM] : '+'I am a simulated unconcious subconcious'+'\n')
        elif user_txt == 'hi':
            self.sc.insert(tk.INSERT, '[SYSTEM] : '+'Hello'+'\n')
        else:
            self.sc.insert(tk.INSERT, '[SYSTEM] : '+'??? I dont understand you'+'\n')

    def convert_to_speech(self):
        voice: str = self.text.get()
        engine.say(voice)
        
        # Flush the say() queue and play the audio
        engine.runAndWait()
        # after speaking print the text in the scrolled text
        self.sc.insert(tk.INSERT, '[USER] : '+str(self.text.get())+'\n')
        #self.sys_reply()

    def run(self):
        self.win.mainloop()


start = GUI()
start.run()
# Program will not continue execution until
# all speech is done talking
