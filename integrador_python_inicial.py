import csv

def abrir_archivo_lectura (modo): #Esta función realiza la apertura del archivo colocando los datos en una variable list
    '''El parametro modo indica el modo en el que se abrirá el archivo (w, r, a, r+)'''
    data = {}

    with open('Archivo_biblioteca.csv', modo, encoding='utf-8') as csvfile:
        data = list(csv.DictReader(csvfile))

    return data

def escribir_archivo (modo, data):
    if modo == 'w':
        with open('Archivo_biblioteca.csv', 'w', newline='', encoding='utf-8') as csvfile:
            header = ['id', 'ISBN', 'Nombre', 'Autor', 'Género']
            writer = csv.DictWriter(csvfile, fieldnames = header)
            writer.writeheader()
            writer.writerows(data)

def generar_id():
    '''
    Funcion de ayuda, nos obtiene el ID para que insertemos un nuevo libro, el ID que devuelve
    es el último ID registrado + 1
    
    # Aumentar en 1 el ID encontrado, y retornarlo
    return ultimo_id + 1
    '''

    # Obtener ultima fila del CSV leído
    ultimo_id = len(abrir_archivo_lectura('r'))

    # Aumentar en 1 el ID encontrado, y retornarlo
    return ultimo_id + 1

def reordenar_ids():
    '''
    Función que reordena los IDs del CSV de libros
    No tiene valor de retorno. 
    '''
    data = abrir_archivo_lectura('r')
    for i in range(len(abrir_archivo_lectura('r'))):
        # Asignar como id de un libro, su índice en la lista + 1, para no asignarle a nadie el ID = 0
        data[i]['id'] = i + 1

    escribir_archivo('w', data)


def nuevo_libro():
    control = True # Variable que se usa para verificar la existencia del ISBN
    isbn_existe = False
    variable_sn = None

    
    while control:
        data = abrir_archivo_lectura('r')
        
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
    id = None
    diccionario = {}

    data = abrir_archivo_lectura('r')
    dict = data[0]

    print("Estos son los libros que tiene en su biblioteca:")
    print('Id    Nombre              Autor')
    for diccionario in data:
        print(diccionario.get('id'), '  ', diccionario.get('Nombre'), '  ', diccionario.get ('Autor'))
    while True:
        print("Elija el Id del libro que desea borrar:")
        id = int(input()) - 1
        if id > 0 and id < len(data):
            data.pop(id)
            break
        else:
            print("Debe ingresar un valor válido!")
    escribir_archivo('w', data)
    reordenar_ids()

def modificar_libro():
    id = None

    data = abrir_archivo_lectura('r')
    
    print ("Estos son los libros que tiene en su biblioteca:")
    print('Id   ISBN         Nombre            Autor           Género')
    for diccionario in data:
        print(diccionario.get('id'), '  ',diccionario.get('ISBN'), '  ', diccionario.get('Nombre'), '  ', diccionario.get ('Autor'), '  ', diccionario.get('Género'))
    while True:
        print("Elija el Id del libro que desea borrar:")
        id = int(input()) - 1
        if id > 0 and id < len(data):
            data.pop(id)
            break
        else:
            print("Debe ingresar un valor válido!")
    isbn = str(input("Ingrese el ISBN del libro:\n")) # Se solicita al usuario ingrese la información
    nombre_libro = str(input("Ingrese nombre del libro:\n")) # de un libro
    autor_libro = str(input("Ingrese autor del libro:\n"))
    genero_libro = str(input("Ingrese género del libro:\n"))
    dict_dato = {'id': id + 1, 'ISBN': isbn, 'Nombre': nombre_libro, 'Autor': autor_libro, 'Género': genero_libro}
    data.insert(id, dict_dato)
    escribir_archivo('w', data)

def reportes_varios():
    opcion_reporte = None
    variable_sn = None
    autor = None
    genero = None
    isbn = None

    data = abrir_archivo_lectura('r')

    while True:
        opcion_reporte = input("Ingrese una opción:\n1.- Listado general.\n2.- Listado por autor.\n3.- Listado por género.\n4.- Libro por ISBN.\n")
        if opcion_reporte == '1':
            print('Id   ISBN        Nombre          Autor          Género')
            for diccionario in data:
                print(diccionario.get('id'), '  ',diccionario.get('ISBN'), '  ', diccionario.get('Nombre'), '  ', diccionario.get ('Autor'), '  ', diccionario.get('Género'))
        elif opcion_reporte == '2':
            autor = str(input('Ingrese nombre del autor:\n'))
            print('Id   ISBN        Nombre          Autor           Género')
            for diccionario in data:
                if diccionario.get('Autor') == autor:
                    print(diccionario.get('id'), '  ',diccionario.get('ISBN'), '  ', diccionario.get('Nombre'), '  ', diccionario.get ('Autor'), '  ', diccionario.get('Género'))
        elif opcion_reporte == '3':
            genero = str(input('Ingrese género:\n'))
            print('Id   ISBN          Nombre           Autor          Género')
            for diccionario in data:
                if diccionario.get('Género') == genero:
                    print(diccionario.get('id'), '  ',diccionario.get('ISBN'), '  ', diccionario.get('Nombre'), '  ', diccionario.get ('Autor'), '  ', diccionario.get('Género'))
        elif opcion_reporte == '4':
            isbn = str(input('Ingrese ISBN a buscar:\n'))
            print('Id   ISBN       Nombre          Autor        Género')
            for diccionario in data:
                if diccionario.get('ISBN') == isbn:
                    print(diccionario.get('id'), '  ',diccionario.get('ISBN'), '  ', diccionario.get('Nombre'), '  ', diccionario.get ('Autor'), '  ', diccionario.get('Género'))
        variable_sn = str(input("Desea seguir consultando datos? S/N.\n"))
        if variable_sn == 'S' or variable_sn == 's':
            continue
        elif variable_sn == 'N' or variable_sn == 'n':
            break
        else:
            print("Debe Ingresar un valor válido")



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
