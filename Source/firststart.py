from delete_all_mods import delete_all_mods,delete_pycache

datei = open("id.fmmconfig",'w')
datei.write("427520")
datei.close
delete_all_mods()
delete_pycache()