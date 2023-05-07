import tkinter as tk
import customtkinter
from mytkinter import get_input
def new_work():
    window = customtkinter.CTk()
    customtkinter.set_appearance_mode("Dark")
    window.title("New")
    window.iconbitmap("icon.ico")
    window.geometry("440x415")

    get_input(window)
