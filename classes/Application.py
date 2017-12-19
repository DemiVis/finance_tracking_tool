"""
Class to act as the actual application GUI and whatnot.
"""

from Tkinter import *
import Year
import Month
import AnnualPot
import Account


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_open_screen()

    def create_open_screen(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side": "left"})
