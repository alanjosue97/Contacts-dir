
import os 

FOLDER = 'contacts/' #carpeta de contactos

def app():
    #revisa si la carpeta existe o no
    create_directorio() 

    #Muestra el menu de opciones
    mostrar_menu()

    #preguntar al usuario la accion a realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opcion: \r\n')
        opcion = int(opcion)

        #ejecutar las opciones
        if opcion == 1:
            print('Agregar contacto')
            preguntar = False
        elif opcion == 2:
            print('Editar Contacto')
            preguntar = False
        elif opcion == 3:
            print('Ver Contactos')
            preguntar = False
        elif opcion == 4:
            print('Buscar Contacto')
            preguntar = False
        elif opcion == 5:
            print('Eliminar Contacto')
            preguntar = False
        else:
            print('Opcion no valida. Intente de nuevo')

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