
import os 

FOLDER = 'contacts/' #carpeta de contactos

def app():
    #revisa si la carpeta existe o no
    create_directorio() 

    #Muestra el menu de opciones
    mostrar_menu()

def mostrar_menu():
    print('Seleccione del menu lo que desea hacer: ')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')

def create_directorio():
    if not os.path.exists(FOLDER):    
        #create file
        os.makedirs(FOLDER)           # si no existe creala
        #este else es opcional
    #else:
        #print('La carpeta ya existee')
    

app()