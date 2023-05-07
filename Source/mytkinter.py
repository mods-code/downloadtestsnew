import tkinter as tk
import customtkinter
from myjson import create_info_json,save_info_json
from openworkspace import choose_folder_and_copy
from EDITOR import Workspace_window_open

def get_string_by_index(strings, index):
    if index >= len(strings):
        return None
    return strings[index]


def get_input(window):
    entry_list = []
    labels = ["Mod-name:", "Author:", "Description:","Factorio Version: \n (Default: 1.1)"]
    for i in range(len(labels)):
        label = customtkinter.CTkLabel(window, text=labels[i])
        label.pack()
        entry = customtkinter.CTkEntry(window)
        entry.pack()
        entry_list.append(entry)

    def ok():
        result = list()
        for i, entry in enumerate(entry_list):
            text = entry.get()
            if not text:
                tk.messagebox.showerror(title="Error", message="Please fill in all fields")
                return
            result.append(text)
            re1.append(i)
        print(result)
        window.destroy()
        result1 = get_string_by_index(result, 0)
        result2 = get_string_by_index(result, 1)
        result3 = get_string_by_index(result, 2)
        result4 = get_string_by_index(result, 3)
        json_string = create_info_json(result1, result2, result3,result4)
        save_info_json(result1, json_string)
        Workspace_window_open(result1)

    re1 = []

    button_ok = customtkinter.CTkButton(window, text="OK", command=ok)
    button_ok.pack(padx=0,pady=5)

    button_cancel = customtkinter.CTkButton(window, text="Cancel", command=window.destroy)
    button_cancel.pack(padx=20,pady=15)
    button = customtkinter.CTkButton(window, text="Open Workspace", command=choose_folder_and_copy)
    button.pack(padx=20,pady=00)
    window.mainloop()
