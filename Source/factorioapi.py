import subprocess
def start(id):
    dataname = 'tmp.bat'
    datei = open(dataname,'w')
    datei.write("start " + "steam://rungameid/"+ id)
    datei = open(dataname,'r')
    subprocess.call([r"tmp.bat"])
    datei.close()
