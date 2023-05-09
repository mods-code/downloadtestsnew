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


def lua_editor(modname,code,script_name,textColor):


    def save_code():
        Textbox_text = text_zone.get("1.0", "end-1c")
        File_name = scriptname.get()

        if File_name == "":
            File_name = script_name


        with open("mods/" + modname + "/" + File_name + ".lua", "w") as file:
            file.write(Textbox_text)
        file.close()
        print("Debug: Save Code as a Lua File in mod > " + modname + " < with Name: " + File_name)
        window.quit()
        window.destroy()

    window = customtkinter.CTk()
    customtkinter.set_appearance_mode("Dark")
    window.title("Lua editor -- " + modname + ": NewScript.lua")
    window.iconbitmap("icons/luaedit/luaedit.ico")
    window.geometry("900x800")


    tabview = customtkinter.CTkTabview(window,width=700,height=900)
    tabview.pack(padx=20, pady=20)
    tabview.add("Code")
    tabview.add("Options & Save")
    tabview.set("Code")

    button_save = customtkinter.CTkButton(tabview.tab("Options & Save"), text="Save & Quit", command=save_code)
    button_save.pack(padx=0,pady=5)

    script_name_lable = customtkinter.CTkLabel(tabview.tab("Options & Save"), text="Script-Name:")
    script_name_lable.pack(padx=0,pady=5)

    scriptname = customtkinter.CTkEntry(tabview.tab("Options & Save"), placeholder_text="Faster tanks")
    scriptname.pack(padx=0,pady=5)


    text_zone = customtkinter.CTkTextbox(tabview.tab("Code"),fg_color="#646464",scrollbar_button_color="#414141",scrollbar_button_hover_color="#4E4E4E",text_color=textColor)
    text_zone.pack(expand = tk.YES, fill = tk.BOTH, side = tk.LEFT)
    text_zone.insert("0.0", code)
    window.mainloop()

with open("mods/" + "mymod" + "/" + "testtoloadcode" + ".lua", "r") as file:
    filetext = file.read()
    file.close()