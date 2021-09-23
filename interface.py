import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.constants import *

import ctypes
from ctypes import wintypes
import time

from commands import *

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()
		self.uploadedFile = None

	def create_widgets(self):
		# self.display = tk.Entry(self)
		self.display = tk.Text(self)
		self.display.pack(side="top", expand=True, padx=20, pady=20)
		
		self.upload = tk.Button(self)
		self.upload["text"] = "Upload File"	
		self.upload["command"] = self.UploadAction
		self.upload.pack(side=LEFT, padx=20)

		self.downloadban = tk.Button(self)
		self.downloadban["text"] = "Save /ban list"
		# self.downloadban["command"]
		self.downloadban.pack()

		self.downloadblock = tk.Button(self)
		self.downloadblock["text"] = "Save /block list"
		# self.downloadblock["command"]
		self.downloadblock.pack()

		self.ban = tk.Button(self)
		self.ban["text"] = "Execute /ban commands"
		# self.ban["command"] = 
		self.ban.pack()

		self.block = tk.Button(self)
		self.block["text"] = "Execute /block commands"
		# self.block["command"] = 
		self.block.pack()

	def UploadAction(self, event=None):
		self.uploadedFile = filedialog.askopenfilename(title="Open Text File", filetypes=[("Text Files", "*.txt")])
		self.display.insert(INSERT, pretty_print(self.open_file()))

	def open_file(self):
		f = open(self.uploadedFile)
		return f.read().splitlines()


root = tk.Tk()
root.title("Mass Ban Tool")
root.geometry("500x700")

app = Application(master=root)

app.mainloop()