from newproject import new_work
import customtkinter
mainroot = customtkinter.CTk()
mainroot.title("Mod-Maker")
mainroot.iconbitmap("icon.ico")
mainroot.geometry("440x415")
customtkinter.set_appearance_mode("Dark")
def new_workspace():
    mainroot.destroy()
    new_work()
button_ok = customtkinter.CTkButton(mainroot, text="New Workspace", command=new_workspace)
button_ok.pack(padx=0,pady=5)



mainroot.mainloop()