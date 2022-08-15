![books-g4be6700ba_1280](https://user-images.githubusercontent.com/107430928/182972258-add20013-a605-4eb2-a85b-c94a984a3e5a.jpg)
# Sistema de control de biblioteca

Versión del proyecto: 1.1                                                           
Autor: sjrougo - Santiago Rougoski                                          
Contacto: santiagorougoski@gmail.com                                        

Este es un pequeño administrador de libros. A veces tenemos unos cuantos libros (o muchos!) y es un poco engorroso no saber bien cuáles son, los autores o títulos que ya poseemos.

A continuación coloco un diagrama de flujo del programa.

![Diagrama Proyecto Integrador - Python Inicial - Inove 2022](https://user-images.githubusercontent.com/107430928/183225857-32cf001c-b9cf-4ac4-bec1-00576f3cd433.jpeg)

En el programa trabaja con un archivo .csv y cuando lo ejecutemos se encontrará un menú inicial en el que debemos elegir entre varias opciones: podemos agregar entradas de libros nuevos, borrar alguno por alguna razón, modificar e incluso solicitar listados por autor o género.

Se realiza un control de flujo y verificación en todas las funciones que posee el programa. Primeramente en la opción de ingresar un nuevo elemento, se verifica que el ISBN del libro no exista ya en el archivo. El la función borrar libro, se despliega un listado general de los libros que posea el usuario, para que solamente se elija el Id del libro. Seguidamente, en la opción de modificar libro, se despliega un listado general y se pide al usuario que elija el Id del libro a modificar y luego se pide que ingrese los valores del libro (ISBN, nombre, autor y género). Cuando se elije la opción de reportes varios, se despliega otro menú con las opciones que tiene el programa para generar reportes, ellas son la de listado general, listado por autor, listado por género y finalmente recuperar la información de un libro por medio de su ISBN.

Espero que puedan disfrutar de este proyecto!
