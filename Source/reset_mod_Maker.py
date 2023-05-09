from tkinter import messagebox
from delete_all_mods import delete_all_mods,delete_pycache

def reset_mod_maker():
    datei = open("id.fmmconfig",'w')
    datei.write("427520")
    datei.close
    delete_all_mods()
    delete_pycache()
result = messagebox.askyesno("Delete", "Are you sure you want to reset Mod Maker?", icon='warning', default='no')
if result == True:
  reset_mod_maker()
  messagebox.showinfo("Info","Mod Maker has been reset successfully.")
