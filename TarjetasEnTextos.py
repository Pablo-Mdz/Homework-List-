
import os
from tkinter import ARC
#en mayuscula porque es una constante y no se debe modificar
CARPETA = 'contactos/' #carpeta de contactos
EXTENSION= '.txt' #extension de archivos

#contactos
class Contactos:
    def __init__(self,nombre,telefono,categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    #crea la carpeta solo si no existe
    crear_directorio()

    #muestra menu de opciones
    mostrar_menu()

    #preguntar al usuario la accion a realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

        #ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opción no válida')

def eliminar_contacto():
    nombre = input('seleccione el nombre que desea eliminar: \r\n')

    try:
        os.remove(CARPETA+ nombre + EXTENSION)
        print('\r\n Contacto eliminado correctamente \r\n')
    except IOError:
        print('\r\n No existe ese contacto\r\n') 
    app()  

def buscar_contacto():
    nombre = input('seleccione el nombre que desea buscar: \r\n')
    
    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('\r\n El archivo no existe\r\n')
        print(IOError)

    #reiniciar la app
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)] 

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                #imprime los contenidos
                print(linea.rstrip())
                #imprime un separador entre contactos
            print('\r\n')
    app()
          
def editar_contacto():

    nombre_anterior = input('Ingrese el nombre de contacto que desea editar \r\n')
    #lo verifica en la funcion existe contacto y lo devuelve
    existe = existe_contacto(nombre_anterior)
    if existe:
       with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

           #resto de los campos
           nombre_contacto = input('Agrega el nuevo nombre: \r\n')
           telefono_contacto = input('Agrega el nuevo teléfono: \r\n')
           categoria_contacto= input('Agrega la nueva categoría: \r\n')

        #instanciar
           contacto = Contactos(nombre_contacto,telefono_contacto,categoria_contacto)
        #escribir en el archivo
           archivo.write('Nombre: '+ contacto.nombre+ '\r\n')
           archivo.write('Teléfono: '+ contacto.telefono+ '\r\n')
           archivo.write('Categoría: '+ contacto.categoria+ '\r\n')

           #renombrar el archivo
           os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto+ EXTENSION )
    
                    #mostrar un mensaje de exito
           print('\r\n Contacto editado Correctamente\r\n')   
    else:
        print('Ese contacto no existe')
    
    #reiniciar aplicacion
    app()

def agregar_contacto():
    print('Escribe los datos para agregar el  nuevo contacto ')
    nombre_contacto = input('Nombre del Contacto: \r\n')

#revisar si el archivo ya existe
    existe = os.path.isfile(CARPETA + nombre_contacto + EXTENSION) 
    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            #resto de los campos
            telefono_contacto = input('Agrega el teléfono: \r\n')
            categoria_contacto= input('Categoría de Contacto: \r\n')

        #instanciar la clase
            contacto = Contactos(nombre_contacto,telefono_contacto,categoria_contacto)

        #escribir en el archivo

            archivo.write('Nombre: '+ contacto.nombre+ '\r\n')
            archivo.write('Teléfono: '+ contacto.telefono+ '\r\n')
            archivo.write('Categoría: '+ contacto.categoria+ '\r\n')
        #mostrar un mensaje de exito
            print('\r\n Contacto creado Correctamente\r\n')
    else:
        print('Este contacto ya existe')
        #reiniciar la app
    app()

def mostrar_menu():
    print('Seleccione del Menu lo que desea hacer: ')
    print('1) Agregar nuevo contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar contacto')
       
def crear_directorio():  #crear la carpeta
    if not os.path.exists('contactos/'):
        os.makedirs('contactos/')

def existe_contacto(nombre):
    return  os.path.isfile(CARPETA + nombre + EXTENSION) 
app()