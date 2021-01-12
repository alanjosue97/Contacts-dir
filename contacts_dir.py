
import os 

FOLDER = 'contacts/' #carpeta de contactos

def app():
    #revisa si la carpeta existe o no
    create_directoro()


def create_directoro():
    if not os.path.exists(FOLDER):    
        #create file
        os.makedirs(FOLDER)           # si no existe creala
    #este else es opcional
    else:
        print('La carpeta ya existe')



app()