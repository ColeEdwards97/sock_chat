import threading
import tkinter as tk
from tkinter import *

class chat_gui(object):


    # INIT
    def __init__(self, client, width=None, height=None):

        self.client = client

        self.tThread = threading.Thread(target=self.main_loop, args=(width, height))
        self.tThread.start()


    # CREATE GUI
    # define gui objects
    def create_gui_objects(self):

        self.frame = tk.Frame(self.root)

        # chat text area
        self.scrollbar = tk.Scrollbar(self.frame)
        self.text_area = tk.Listbox(self.frame, height=15, width=100, yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH)

        self.frame.pack()


        # text entry field
        self.message = tk.StringVar()
        self.message.set("start typing here!")
        self.entry_field = tk.Entry(self.root, textvariable=self.message, width=85)
        self.entry_field.bind("<Return>", self.send)
        self.entry_field.pack()

        # send button
        self.send_btn = tk.Button(self.root, text="send", command=self.send)
        self.send_btn.pack()

    
    # SEND
    # send a message
    def send(self, event=None):

        self.client.send(bytes(self.message.get(), "UTF-8"))
        self.message.set("")


    # PUSH MESSAGE
    # push a message to the text area
    def push_message(self, message):
        self.text_area.insert(tk.END, message)
        self.text_area.yview(tk.END)


    # ON CLOSE
    # close client and gui
    def on_close(self, event=None):
        self.client.close()
        self.root.quit()


    def main_loop(self, width=None, height=None):

        self.root = tk.Tk()
        self.root.title("py_chat")
        
        if width != None and height != None:
            self.root.geometry(''.join([str(width), "x", str(height)]))

        #self.root.protocol("WM_DELETE_WINDOW", on_close)

        self.create_gui_objects()

        self.root.mainloop()

