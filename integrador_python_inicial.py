from ast import Try
import csv
from operator import getitem

def generar_id():
    '''
    Funcion de ayuda, nos obtiene el ID para que insertemos una nuevo libro, el ID que devuelve
    es el último ID registrado + 1

    with open('prendas.csv', 'r') as csvfile:
        # Leer archivo CSV y almacenar los resultados en data
        data = list(csv.DictReader(csvfile))

    # Obtener ultima fila del CSV leído
    ultima_fila = data[-1]

    # Obtener el ID de la última fila
    ultimo_id = int(ultima_fila.get('id'))
    
    # Aumentar en 1 el ID encontrado, y retornarlo
    return ultimo_id + 1
    '''
    with open('Archivo_biblioteca.csv', 'r') as csvfile:
        # Leer archivo CSV y almacenar los resultados en data
        data = list(csv.DictReader(csvfile))

    # Obtener ultima fila del CSV leído
    ultimo_id = len(data)

    # Obtener el ID de la última fila
    # ultimo_id = int(ultima_fila.get('id'))
    
    # Aumentar en 1 el ID encontrado, y retornarlo
    return ultimo_id + 1

def nuevo_libro():
    control = True # Variable que se usa para verificar la existencia del ISBN
    isbn_existe = False
    variable_sn = None

    while control:
        with open('Archivo_biblioteca.csv', 'r') as csvfile:
            data = list(csv.DictReader(csvfile))
        
        csvfile = open('Archivo_biblioteca.csv', 'a', newline='', encoding='utf-8')
        header = ['id', 'ISBN', 'Nombre', 'Autor', 'Género'] # Se detallan los nombres del encabezado
        writer = csv.DictWriter(csvfile, fieldnames=header)
        if len(data) == 0:
            writer.writeheader()

        isbn = str(input("Ingrese el ISBN del libro:\n")) # Se solicita al usuario ingrese la información
        nombre_libro = str(input("Ingrese nombre del libro:\n")) # de un libro
        autor_libro = str(input("Ingrese autor del libro:\n"))
        genero_libro = str(input("Ingrese género del libro:\n"))
        nro_id = generar_id()
        dict_dato = {'id': nro_id, 'ISBN': isbn, 'Nombre': nombre_libro, 'Autor': autor_libro, 'Género': genero_libro}


        if len(data) == 0: # If que verifica si el libro es el primero en ser ingresado.
            writer.writerow(dict_dato)
            while True:
                variable_sn = str(input("Desea seguir cargando datos? S/N.\n"))
                if variable_sn == 'S' or variable_sn == 's':
                    break
                elif variable_sn == 'N' or variable_sn == 'n':
                    control = False
                    break
                else:
                    print("Debe Ingresar un valor válido")
        else:
            for i in range(0, nro_id - 1):
                if data[i]['ISBN'] == isbn:
                    isbn_existe = True
            if isbn_existe == True:
                print("El ISBN del libro ya existe en el archivo")
                while True: # En este bucle se realizará un control para determinar si el usuario desea continuar con la operación
                    variable_sn = str(input("Desea seguir con la operación? S/N.\n"))
                    if variable_sn == 'S' or variable_sn == 's':
                        break
                    elif variable_sn == 'N' or variable_sn == 'n':
                        control = False # Si la respuesta es N (No), se sale de este bucle, pero también se
                        break # cambia control a False, para garantizar que el programa salga del bucle principal
                    else:
                        print("Debe Ingresar un valor válido")
                isbn_existe = False
            else:
                writer.writerow(dict_dato)
                while True:
                    variable_sn = str(input("Desea seguir cargando datos? S/N.\n"))
                    if variable_sn == 'S' or variable_sn == 's':
                        break
                    elif variable_sn == 'N' or variable_sn == 'n':
                        control = False
                        break
                    else:
                        print("Debe Ingresar un valor válido")
    
        csvfile.close()


def borrar_libro():
    pass

def modificar_libro():
    pass

def reportes_varios():
    pass


if __name__ == '__main__':
    opcion = None
    print("Empezamos el Integrador")
    print("Bienvenido el Sistema de control de biblioteca, a continuación presentamos el menú, elija una opción:")
    while True:
        opcion = input("1.- Ingresar nuevo libro.\n2.- Borrar libro existente.\n3.- Modificar datos de entrada.\n4.- Pedir reportes varios.\n5.- Cerrar programa.\n")
        if opcion == '1':
            nuevo_libro()
        elif opcion == '2':
            borrar_libro()
        elif opcion == '3':
            modificar_libro()
        elif opcion == '4':
            reportes_varios()
        elif opcion == '5':
            print("Hasta pronto")
            break
        else:
            print("Debe ingresar un valor válido")

