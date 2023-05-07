from tkinter import PhotoImage, messagebox
import tkinter as tk
from tkinter.ttk import Button
import customtkinter
def generateworkspace():
      loader = tk.Tk()
      loader.destroy()
      loader.mainloop()
def Workspace_window_open(name):
    generateworkspace()
    Workspace = customtkinter.CTk()
    Workspace.title("Fatorio Mod Creator--"+name)
    Workspace.iconbitmap("icon.ico")
    Workspace.geometry("500x500")
    customtkinter.CTkButton(Workspace, text = '').grid(row=0, column=0)
    Workspace.mainloop()
