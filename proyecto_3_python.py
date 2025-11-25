"""--1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias 
de cada letra en la cadena. Los espacios no deben ser considerados. """

def frecuencias(cadena):                                                        # Definimos funcion
    diccionario =  {}                                                                    # Creamos un diccionario donde agregaremos cada letra como clave y despues su frecuencia como valor
    for letra in cadena:                                                              # Recorremos la cadena letra por letra
        if letra != " ":                                                                     # Le indicamos que hacer si la letra es distinta a espacio 
            if letra in diccionario:                                                  # Le indicamos que hacer si ya esta la letra en diccionario
                diccionario[letra]  += 1                                            # Si la letra ya esta en el diccionario, le sumaremos 1 
            else:                                                                                # De otro modo
                diccionario[letra] = 1                                               # Lo dejamos en 1
    return diccionario                                                                # Le indicamos que nos devuelva el diccionario con su clave valor ya definida
texto="Hola amigos"                                                               #Creamos un texto para probar nuestra funcion
print(frecuencias(texto))                                                        #Imprimimos el texto con nuestra funcion 

{'H': 1, 'o': 2, 'l': 1, 'a': 2, 'm': 1, 'i': 1, 'g': 1, 's': 1}

"""--2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función 
map() """

lista_numeros = [ 2,4,6,8,10]                                               #Creamos una variable con nuestra lista de numeros
def multiplicar_por_2(numero):                                         # Creamos la funcion que multiplicara el elemento numero
    """Esta funcion multiplica por 2"""                                # Aclaramos que hace la funcion
    return numero *2                                                              # le indicamos que nos regrese el elemento numero multiplicado por 2

print(list(map(multiplicar_por_2, lista_numeros)))       # Aplicamos la función a cada elemento usando map y convertimos el resultado en lista

[4, 8, 12, 16, 20]

"""--3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe 
devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo."""

def buscar_palabras(lista, objetivo):                                                  # Definimos nuestra funcion con su lista y el objetivo como parametros
    lista_vacia = []                                                                                     # Creamos una lista vacia a donde pasaremos las palabras de la lista original que cumpla el objetivo
    for palabras in lista:                                                                           # Recorremos las palabras en la lista
        if objetivo in palabras:                                                                  # Si encontramos la palabra objetivo en las palabras de la lista                                                    
            lista_vacia.append(palabras)                                                   # Añadimos a nuestra lista las palabras que cumplan con el objetivo
    return lista_vacia                                                                               # Solicitamos la lista vacia con sus coincidencias              

lista_de_palabras = ["parasol", "tornasol", "girasol", "toro"]        # Creamos una lista con palabras similares
resultado = buscar_palabras(lista_de_palabras, "sol")                   # Creamos una variable, aplicamos la funcion a nuestra lista y definimos la palabra objetivo
print(resultado)                                                                                      # Imprimimos nuestro resultado

['parasol', 'tornasol', 'girasol']


"""--4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map() """

def diferencia_valores (valor1, valor2):                      # Generamos nuestra funcion con sus 2 parametros 
    """Esta función resta el valor2 del valor1"""       # Definimos la funcion
    return valor1 - valor2                                                # Solicitamos que nos regrese el resultado de la resta

lista1= [10, 20, 30, 40]                                                  # Creamos las listas para usar la funcion
lista2 = [5,  10, 15, 20]

print(list(map(diferencia_valores, lista1, lista2)))   #Imprimimos nuestro resultado en formato de lista

[5, 10, 15, 20]

"""--5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por 
defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual 
que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver 
una tupla que contenga la media y el estado."""

def calificaciones (lista, nota_aprobada=5):                   # Creamos nuestra funcion con sus parametros.
    media = sum(lista) / len(lista)                                        # Definimos la media con la que compararemos la nota final
    if media >=  nota_aprobada:                                         # Indicamos el estado "Aprobado" si es mayor a nota_aprobada 
        estado = "Aprobado"
    else:                                                                                   # Indicamos el estado "Suspendido" si es menor a nota_aprobada 
        estado = "Suspendido"
    return media, estado                                                      # indicampos que nos regrese el valor final de la media y el estado como una tupla
  
lista_notas = [5,8,4,3,7,2,5,8]
print(calificaciones(lista_notas))

(5.25, 'Aprobado')


"""--6. Escribe una función que calcule el factorial de un número de manera recursiva."""

def factorial(n):                                        # Definimos nuestra funcion
    if n == 0 or n == 1:                               # definimos un caso base. 0! y 1! = 1
        return 1
    else:                                                       # de otro modo, indicamos que continue de manera recursiva
        return n * factorial(n - 1)

print(f"El factorial de 5 es {factorial(5)}")

El factorial de 5 es 120

"""--7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()"""

def listas_tupla_a_string (lista):                                                             # Definimos la funcion 
    """Esta funcion transforma listas de tuplas a listas string"""
    def funcion_auxiliar(tupla):                                                                 # Creamos una funcion auxiliar 
        return str(tupla)                                                                                 # Convertimos a string
    resultado = map(funcion_auxiliar, lista)                                            # Hacemos uso de la funcion map
    return list(resultado)                                                                            # Transformamos a lista

entrada = [(1, 2), (3, 4), ('a', 'b')]
print(listas_tupla_a_string(entrada))

['(1, 2)', '(3, 4)', "('a', 'b')"]

"""--8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico 
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje 
indicando si la división fue exitosa o no.""" 

try:
    Num1= int(input("Selecciona un dividendo"))                                      # Solicitamos el dividendo y divisor al usuario convirtiendolos a int
    Num2= int(input("Selecciona un divisor"))
    resultado = Num1/Num2                                                                          # Creamos una variable que indique el valor de la division
    print(f"El resultado de la división es: {round(resultado, 2)}")             # Imprimimos el resultado haciendolo un float
except ValueError:                                                                                          # Indicamos un valor correcto al usuario
      print("Ingrese un número válido.")
except ZeroDivisionError:
     print("No es posible dividir entre 0.")                                                    # Indicamos que no es posible dividir entre 0
else:
     print("Division exitosa!")                                                                          # Finalizamos la division sin errores

El resultado de la división es: 5.0
Division exitosa!

"""--9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista 
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", 
"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función 
filter() """

def filtar_animales (lista):                                                                                                                   # Definimos nuestra funcion
    animales_prohibidos = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]         # Utilizamos la lista que ya tenemos
    def permitidos (animal):                                                                                                                  # Creamos una funcion auxiliar 
        return animal not in animales_prohibidos                                                                              # Indicamos que solo nos devuelva los animales permitidos
    resultado = filter(permitidos, lista)                                                                                               # Hacemos uso de filter en la funcion auxiliar
    return list(resultado)                                                                                                                       # Indicamos que nos devuelva una nueva lista

animales_prueba =["Gato", "Perro", "Pajaro", "Mapache"]
print(filtar_animales(animales_prueba))

['Gato', 'Perro', 'Pajaro']

"""--10.Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una 
excepción personalizada y maneja el error adecuadamente."""

class ListaVaciaError(Exception):                                                                                                                # Creamos una clase para  el error de la lista vacía 
    """Excepción lanzada cuando la lista está vacía."""
    pass
def calcular_promedio(numeros):                                                                                                             # Definimos la función que calcula el promedio
    """Calcula el promedio de una lista de números."""
    if not numeros:                                                                                                                                         # Verificamos si la lista está vacía
        raise ListaVaciaError(" Error: La lista está vacía. No se puede calcular el promedio.")
    promedio = sum(numeros) / len(numeros)                                                                                         # Calculamos el promedio
    return promedio
try:
    lista = [10, 20, 30, 40]                                                                                                                               # Creamos una lista con números
    resultado = calcular_promedio(lista)                                                                                                     # Llamamos a la función
    print(f"El promedio es: {resultado}")                                                                                                     # Mostramos el resultado si todo sale bien
    lista_vacia = []                                                                                                                                             # Lista vacía para probar el error
    resultado_vacio = calcular_promedio(lista_vacia)                                                                              # Intentamos calcular el promedio
    print(f"El promedio es: {resultado_vacio}")                                                                                         # No se ejecutará si hay error
except ListaVaciaError as e:                                                                                                                         # Capturamos la excepción personalizada
    print(e)                                                                                                                                                         # Mostramos el mensaje de error
except Exception as e:                                                                                                                                  # Capturamos cualquier otro error inesperado
    print(f" Ocurrió un error inesperado: {e}")
finally:
    print("Programa finalizado.")                                                                                                                   # Se ejecuta siempre al final

El promedio es: 25.0
Error: La lista está vacía. No se puede calcular el promedio.
Programa finalizado.


"""--11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un 
valor fuera del rango esperado por ejemplo, menor que 0 o mayor que 120, maneja las excepciones 
adecuadamente."""

try:
    edad_usuario = input("Introduce tu edad: ")                       # Solicitamos la edad al usuario
    edad = int(edad_usuario)                                                         # Convertimos a número
    if edad < 0 or edad > 120:                                                         # Revisamos si está fuera del rango permitido
        raise Exception("Edad fuera de rango.")                            # Lanzamos excepción si no es válida
    print("Edad aceptada.")                                                            # Mensaje si la edad está dentro del rango
except ValueError:                                                                          # Si el usuario ingresa algo que no es número
    print("Introduce un número válido.")                                     # Indicamos que debe ingresar un número
except Exception as error:                                                             # Capturamos edades fuera de rango
    print(error)                                                                                   # Mostramos el mensaje correspondiente

    Introduce un número válido.


"""--12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()"""

def longitudes(frase):                                             # Definimos nuestra función
    oracion = " "                                                          # Variable para ir formando cada palabra
    lista_palabras = []                                                # Lista donde guardaremos las palabras completas
    for letra in frase:                                                 # Recorremos cada letra de la frase
        if letra != " ":                                                    # Si la letra no es un espacio
            oracion += letra                                           # Seguimos formando la palabra
        else:                                                                   # Si encontramos un espacio
            lista_palabras.append(oracion)                # Guardamos la palabra formada
            oracion = " "                                                   # Reiniciamos para formar la siguiente palabra
    lista_palabras.append(oracion)                         # Agregamos la última palabra
    return list(map(len, lista_palabras))                  # Devolvemos las longitudes con map()

print(longitudes("Hola The Power School"))        

[5, 4, 6, 7]

"""--13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en 
mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función 
map()""" 

def mayus_y_minus (letras):                                                         # Definimos la función principal
    lista_letras = []                                                                             # Lista para guardar letras sin repetir
    
    for letra in letras:                                                                        # Recorremos cada carácter recibido
        if letra not in lista_letras:                                                      # Si la letra no está ya en la lista
            lista_letras.append(letra)                                                  # Agregamos a nuestra lista vacia

    def convertir(letra):                                                                     # Generamos una función auxiliar 
        return (letra.upper(), letra.lower())                                      # Aplicamos funciones para mayusculas y minusculas
    resultado = map(convertir, lista_letras)                                   # Hacemos uso de la suncion map

    return list(resultado)                                                                    # Convertimos a lista
print(mayus_y_minus("abcd"))                                  

[('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd')]

 """--14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la 
función filter()""" 

def filtrar_palabras(lista_palabras, letra):                                 # Función que recibe la lista y la letra
    def empieza_con(palabra):                                                      # Función interna para revisar cada palabra
        return palabra[0].lower() == letra.lower()                         # Devuelve True si empieza con la letra
    return list(filter(empieza_con, lista_palabras))                     # Filtra usando la función interna
palabras = ["casa", "carro", "perro", "cielo", "sol"]                   # Lista de ejemplo
print(filtrar_palabras(palabras, "c"))                                            # Imprime palabras que empiezan con "c"

['casa', 'carro', 'cielo']

"""--15.Crea una función lambda que  sume 3 a cada número de una lista dada."""

funcion_lambda_3 = lambda x: x + 3                           #Creamos nuestra funcion lambda +3 
lista = [1,2,3,4,5]                                                              # Definimos nuestra lista
print (list(map(funcion_lambda_3, lista)))                   #Convertimos a lista y sumamos elemento por elemento

[4, 5, 6, 7, 8]

"""--16.Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de 
todas las palabras que sean más largas que n. Usa la función filter() """

def palabras_largas(cadena, n):                                                 # Definimos función
    palabras = cadena.split()                                                         # Separamos la cadena en palabras
    def es_larga(palabra):                                                              # Función auxiliar
        return len(palabra) > n                                                         # Comprobamos si es más larga que n
    resultado = filter(es_larga, palabras)                                     # Filtramos las palabras largas
    return list(resultado)                                                                 # Devolvemos lista

print(palabras_largas("Hola The Power School", 3))

['Hola', 'Power', 'School']

"""--17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] 
corresponde al número quinientos setenta y dos (572). Usa la función reduce()"""

from functools import reduce                                      # Importamos reduce para combinar elementos
def lista_a_numero(lista_digitos):                               # Definimos la función principal
    def combinar(acumulado, nuevo):                          # Función auxiliar que combina los dígitos
        return acumulado * 10 + nuevo                           # Construye el número multiplicando por 10 y sumando el nuevo dígito
    resultado = reduce(combinar, lista_digitos)           # Aplica combinar a toda la lista
    return resultado                                                         # Devuelve el número final
print(lista_a_numero([5, 7, 2]))                                   # Probamos la función
572

"""--18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes 
(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 
90. Usa la función filter()"""

lista_estudiantes = [ {"nombre": "Ana", "edad": 20, "calificacion": 95}, 
                      {"nombre": "Luis", "edad": 22, "calificacion": 88}, 
                      {"nombre": "Marta", "edad": 19, "calificacion": 90},
                      {"nombre": "Pedro", "edad": 21, "calificacion": 72} ]

def es_excelente(estudiante):                                                                # Creamos una función que filtra estudiantes
    return estudiante["calificacion"] >= 90                                             # Devuelve True si su calificación es 90 o más
resultado = filter(es_excelente, lista_estudiantes)                             # Aplicamos filter con nuestra funcion
print(list(resultado))                                                                                 # Convertimos el resultado a lista y mostramos los estudiantes filtrados

"""--19.Crea una función lambda que filtre los números impares de una lista dada."""

lambda_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))            # Hacemos uso de filter y convertimos a lista
lista_prueba = [92, 71, 54, 89, 67, 43]                                                                    # Lista de ejemplo
resultado = lambda_impares(lista_prueba)                                                          # Creamos una variable con el uso de nuestra funcion
print(resultado)                                                                                                         

[71, 89, 67, 43]

"""--20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()"""

lista = [10, "hola", 25, "mundo", 7]                                                          # Creamos nuestra lista con ints y strings
solo_enteros = list(filter(lambda x: type(x) == int, lista))                     # Hacemos uso de filter y list
print(solo_enteros)                                                                                     # Muestra solo los enteros

[10, 25, 7]

"""--21. Crea una función que calcule el cubo de un número dado mediante una función lambda"""

cubo = lambda x: x ** 3                                            # Eleva un numero al cubo usando **3

numero = 4                                                                  #Número de ejemplo
resultado = cubo(numero)                                        #Hacemos uso de nuestra funcion 
print("El cubo del número es:", resultado)            

El cubo del número es: 64

"""--22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() ."""

from functools import reduce                                         # importamos reduce

lista = [2, 3, 4, 5] 
producto_total = reduce(lambda x, y: x * y, lista)       # multiplica de manera  acumulativa  todos los valores
print(producto_total)  

120

"""--23. Concatena una lista de palabras. Usa la función reduce() """
from functools import reduce                                              

def concatenar_palabras(lista):                                             # Definimos nuestra función que recibe la lista de palabras
    resultado = reduce(lambda x, y: x + y, lista)                    # Usamos reduce para concatenar todas las palabras
    return resultado                                                                   # Imprimimos el resultado

palabras = ["Hola", " ", "mundo", " ", "Python"]                 
resultado = concatenar_palabras(palabras)                         # Hacemos uso de nuestra funcion
print(resultado)  

Hola mundo Python

"""--24. Calcula la diferencia total en los valores de una lista. Usa la función reduce()""" 

from functools import reduce  

lista = [50, 10, 5] 
diferencia_total = reduce(lambda x, y: x - y, lista)                # Hacemos uso de reduce con nuestra funcion lambda
print(diferencia_total)             

35

"""--25. Crea una función que cuente el número de caracteres en una cadena de texto dada."""

def contar_caracteres(cadena):                     # Creamos la funcion con un parametro
    return len(cadena)                                       # Indicamos que devolver
texto = "Hola mundo"                                     
resultado = contar_caracteres(texto)           # Hacemos uso de la funcion
print(resultado)

10

"""--26. Crea una función lambda que calcule el resto de la división entre dos números dados."""

resto = lambda x, y: x % y                  # Creamos ña función lambda que calcula el resto
resultado = resto(17, 5)                     # Probamos con dos números
print(resultado)

2

"""--27. Crea una función que calcule el promedio de una lista de números."""

def promedio(lista):                                            # Definimos nuestra funcion
    return sum(lista) / len(lista)                           # Sumamos todos los elementos y los dividimos entre la longitud de la lista
numeros = [4, 8, 15, 16, 23, 42]                        
print(promedio(numeros))                                 

18.0

"""--28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada."""

def primer_duplicado(lista):                         # Definimos nuestra funcion
    vistos = []                                                      # Creamos una lista vacia
    for elemento in lista:                                  # Recorremos la lista
        if elemento in vistos:                              # Revisamos si ya aparecio antes
            return elemento                                  # Si es asi, tenemos el primer duplicado
        vistos.append(elemento)                      # Agrefamos el elemento a la lista
    return None                                                 # Si no hubo duplicados devolvemos None

print(primer_duplicado([3,5,1,4,3,7,5]))  

3

"""--29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el 
carácter '#', excepto los últimos cuatro."""

def enmascarar(valor):                                # Creamos nuestra funcion
    texto = str(valor)                                       #  Creamos la variable  cadena
    if len(texto) <= 4:                                     # Si la cadena de texto tiene 4 o menos caracteres, indicamos que nos devuelva el texto
        return texto                                          
    
    cantidad = len(texto) - 4                         # Definimos la variable cantidad con la longitud de texto -4
    mascara = "#" * cantidad                       # Definos una variable mas con la operacion que necesitamos '
    return mascara + texto[-4:]                   # Unimos la máscara con los últimos 4 caracteres

print(enmascarar("123456789"))         

#####6789

"""--30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras 
pero en diferente orden."""

def son_anagramas(p1, p2):                             # Creamos la función principal
    if len(p1) != len(p2):                                        # Si no miden igual, no pueden ser anagramas
        return False

    lista = list(p2)                                                   # Convertimos p2 en lista para poder quitar letras

    for letra in p1:                                                 # Recorremos cada letra de p1
        if letra in lista:                                             # Si la letra existe en la lista, la quitamos.
            lista.remove(letra)                                 
        else:
            return False                                             # Si no esta, no son anagramas

    return True                                                     

print(son_anagramas("roma", "amor"))

True

"""--31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en 
esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se 
lanza una excepción."""

def buscar_nombre():                                                                                          #Creamos la función principal
    lista = input("Ingresa nombres separados por coma: ").split(",")            # Hacemos uso de split `para convertir texto a lista
    nombre = input("Ingresa el nombre a buscar: ")                                        # Solicitamos al usuario un nombre que buscar
    if nombre in lista:                                                                                              # Verificamos si existe
        print(f"El nombre {nombre} fue encontrado.")                                       # Mensaje si el nombre fue encontrado 
    else:
        raise Exception("El nombre no está en la lista.")                                     # Mostramos una excepción sino esta

try:
    buscar_nombre()                                                                                              # Llamamos la función
except Exception as e:
    print(e)                                                                                                               # Mostramos error

El nombre Andres fue encontrado.

"""--32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y 
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona 
no trabaja aquí."""

def buscar_empleado(nombre_completo, empleados):                                      # Definimos nuestra función que busca al empleado
    for empleado in empleados:                                                                                  # Recorremos la lista de empleados
        if empleado["nombre"] == nombre_completo:                                              # Comparamos el nombre completo
            return empleado["puesto"]                                                                            # Si coincide, devolvemos el puesto
    return "La persona no trabaja aquí."                                                                    # Si no está, devolvemos mensaje

empleados = [                                                                                                             
    {"nombre": "Ana López", "puesto": "Gerente"},                                                
    {"nombre": "Juan Pérez", "puesto": "Programador"},                                
    {"nombre": "Luis García", "puesto": "Diseñador"}                                   
]

print(buscar_empleado("Juan Pérez", empleados))                                      
print(buscar_empleado("Juan Andres", empleados))                                     

"""--33. Crea una función lambda que sume elementos correspondientes de dos listas dadas."""

sumar_listas = lambda a, b: [x + y for x, y in zip(a, b)]  # Hacemos uso de la funcion zip para unir elementos por posición y sumarlos
lista1 = [1, 2, 3]                                                                    # Primera lista
lista2 = [4, 5, 6]                                                                    # Segunda lista
print(sumar_listas(lista1, lista2))  

[5, 7, 9]

"""--34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para 
manipular la estructura del árbol.
 Código a seguir:
 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
 6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las 
mismas.
 Caso de uso:
 1. Crear un árbol.
 2. Hacer crecer el tronco del árbol una unidad.
 3. Añadir una nueva rama al árbol.
 4. Hacer crecer todas las ramas del árbol una unidad.
 5. Añadir dos nuevas ramas al árbol.
 6. Retirar la rama situada en la posición 2.
 7. Obtener información sobre el árbol."""     

class Arbol:                                                                                                                                  # define la clase Arbol
    def __init__(self):                                                                                                                   # inicializar un árbol nuevo
        self.tronco = 1                                                                                                                      # el tronco empieza con longitud 1
        self.ramas = []                                                                                                                       # inicialmente no hay ramas

    def crecer_tronco(self):                                                                                                         # aumentar el tronco
        self.tronco += 1                                                                                                                    # suma una unidad al tronco

    def nueva_rama(self):                                                                                                            # agregar una nueva rama
        self.ramas.append(1)                                                                                                          # cada rama nueva empieza con longitud 1

    def crecer_ramas(self):                                                                                                           # aumentar TODAS las ramas
        self.ramas = [r + 1 for r in self.ramas]                                                                               # suma 1 a cada una

    def quitar_rama(self, posicion):                                                                                            # eliminar rama por posición
        if 0 <= posicion < len(self.ramas):                                                                                      # validar que exista
            self.ramas.pop(posicion)
        else:
            print("Posición inválida")

    def info_arbol(self):                                                                                                                  # mostrar información del árbol
        return f"Tronco: {self.tronco}, Ramas: {len(self.ramas)}, Longitudes: {self.ramas}"

# ----- Caso de uso -----

arbol = Arbol()          # 1. Crear árbol
arbol.crecer_tronco()    # 2. Crecer tronco
arbol.nueva_rama()       # 3. Agregar rama
arbol.crecer_ramas()     # 4. Crecer todas las ramas
arbol.nueva_rama()       # 5. Agregar otra rama
arbol.nueva_rama()       # 5. Otra más
arbol.quitar_rama(2)     # 6. Quitar la rama en posición 2
print(arbol.info_arbol())  # 7. Mostrar info final

Saldo final de Alicia: 130
Saldo final de Bob: 10


"""-- 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta 
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y 
agregar dinero al saldo.

Código a seguir:
 1. - Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False
2. - Implementar el metodo retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no 
poder hacerse.
3. - Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. 
Lanzará un error en caso de no poder hacerse
4. - Implementar el método agregar_dinero para agregar dinero al saldo del usuario

Caso de uso:
1. - Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
2. - Agregar 20 unidades de saldo de "Bob".
3. - Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
4. - Retirar 50 unidades de saldo a "Alicia"."""

class UsuarioBanco:                                                                                                              # Crea la clase
    def __init__(self, nombre, saldo, cuenta_corriente):                                                  # Inicializa atributos
        self.nombre = nombre                                                                                                   # Guarda nombre
        self.saldo = saldo                                                                                                             # Guarda saldo
        self.cuenta_corriente = cuenta_corriente                                                                  # Guarda si tiene cuenta corriente

    def retirar_dinero(self, cantidad):                                                                                    # Método para retirar
        if cantidad > self.saldo:                                                                                                  # Si no tiene suficiente dinero
            raise ValueError("Saldo insuficiente para retirar.")                                               # Error
        self.saldo -= cantidad                                                                                                      # Resta del saldo

    def transferir_dinero(self, otro_usuario, cantidad):                                                      # Transferir desde otro usuario
        if cantidad > otro_usuario.saldo:                                                                                   # Si el otro usuario no tiene suficiente
            raise ValueError("El usuario que transfiere no tiene suficiente saldo.")             # Error
        otro_usuario.saldo -= cantidad                                                                                       # Se descuenta al que transfiere
        self.saldo += cantidad                                                                                                       # Se suma al usuario actual

    def agregar_dinero(self, cantidad):                                                                                   # Método para agregar dinero
        self.saldo += cantidad                                                                                                      # Suma al saldo


# CASO DE USO 

alicia = UsuarioBanco("Alicia", 100, True)  # Alicia con 100
bob = UsuarioBanco("Bob", 50, True)  # Bob con 50

bob.agregar_dinero(20)  # Bob ahora tiene 70
bob.agregar_dinero(20)  # Agregamos 20 extra → ahora tiene 90 ✔

alicia.transferir_dinero(bob, 80)  # Transferencia válida

alicia.retirar_dinero(50)  # Alicia retira 50

print("Saldo final de Alicia:", alicia.saldo)
print("Saldo final de Bob:", bob.saldo)

Saldo final de Alicia: 130
Saldo final de Bob: 10


"""--37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras, eliminar_palabras.
Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto.

Código a seguir:

1. - Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene 
que devolver un diccionario.

2. - Crear una función reemplazar_palabras para reemplazar una palabra_original del texto por una nueva palabra_nueva. Tiene que devolver el texto con el
reemplazo de palabras

3. - Crear una funcion eliminar_palabra  para eliminar una palabra del texto. Tiene que devolver el texto con la palabra 
eliminada.

4. - Crear una funcion procesar_texto  que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un 
número de argumentos variable según la opción indicada.

Caso de uso:
 Comprueba el funcionamiento completo de la función 
procesar_texto"""

def contar_palabras(texto):                                                                                                      # Cuenta cuántas veces aparece cada palabra
    palabras = texto.split()                                                                                                           # Separa palabras
    conteo = {}                                                                                                                                # Diccionario donde guardaremos las palabras
    for p in palabras:                                                                                                                     # Recorremos cada palabra
        if p in conteo:                                                                                                                      # Si ya existe en el diccionario
            conteo[p] += 1                                                                                                                 # Aumentamos su contador
        else:
            conteo[p] = 1                                                                                                                   # Si no existe, la iniciamos en 1
    return conteo                                                                                                                           # Devolvemos diccionario

def reemplazar_palabras(texto, palabra_original, palabra_nueva):                                   # Reemplaza palabra
    palabras = texto.split()                                                                                                            # Separa palabras
    resultado = []                                                                                                                             # Lista para guardar palabras nuevas
    for p in palabras:                                                                                                                       # Recorremos palabra por palabra
        if p == palabra_original:                                                                                                       # Si coincide con la original
            resultado.append(palabra_nueva)                                                                                # Añadimos la nueva palabra
        else:
            resultado.append(p)                                                                                                         # Si no coincide, dejamos la misma
    return " ".join(resultado)                                                                                                          # Unimos en una cadena de texto

def eliminar_palabra(texto, palabra_eliminar):                                                                       # Elimina palabra del texto
    palabras = texto.split()                                                                                                              # Separamos palabras
    resultado = []                                                                                                                              # Lista para almacenar palabras que sí quedan
    for p in palabras:                                                                                                                        # Recorremos palabras
        if p != palabra_eliminar:                                                                                                        # Si no es la palabra a eliminar
            resultado.append(p)                                                                                                          # La agregamos
    return " ".join(resultado)                                                                                                          # Unimos en texto final

def procesar_texto(texto, opcion, *args):                                                                                 # Procesa según opción dada
    if opcion == "contar":                                                                                                                # Si la opción es contar
        return contar_palabras(texto)                                                                                             # Llamamos a la función de contar
    elif opcion == "reemplazar":                                                                                                    # Si se va a reemplazar
        return reemplazar_palabras(texto, args[0], args[1])                                                       # Usamos las dos palabras
    elif opcion == "eliminar":                                                                                                         # Si se va a eliminar
        return eliminar_palabra(texto, args[0])                                                                             # Llamamos eliminando palabra
    else:
        return "Opción inválida"                                                                                                       # Mensaje por opción no válida

# --------- CASO DE USO ---------
texto_prueba = "hola mundo hola python mundo"

print(procesar_texto(texto_prueba, "contar"))  # Prueba de contar
print(procesar_texto(texto_prueba, "reemplazar", "hola", "hi"))  # Prueba de reemplazar
print(procesar_texto(texto_prueba, "eliminar", "mundo"))  # Prueba de eliminar

{'hola': 2, 'mundo': 2, 'python': 1}
hi mundo hi python mundo
hola hola python

"""- 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario."""

hora = int(input("Introduce la hora (0-23): "))                          # Pide la hora al usuario
if hora < 0 or hora > 23:                                                                # Verifica que la hora sea válida
    print("Hora inválida")                                                                # Mensaje de error
elif 6 <= hora < 12:                                                                         # Entre 6 y 11
    print("Es de mañana")                                                              # Mensaje
elif 12 <= hora < 18:                                                                       # Entre 12 y 17
    print("Es de tarde")                                                                   # Mensaje
else:                                                                                                  # De 18 a 23 o de 0 a 5
    print("Es de noche")                                                                  # Mensaje

Es de mañana

"""--39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.  
Las reglas de calificación son:
 0 - 69 insuficiente 
 70 - 79 bien 
 80 - 89 muy bien 
 90 - 100 excelente """

calificacion = int(input("Introduce la calificación (0-100): "))                        # Pide la nota

if calificacion < 0 or calificacion > 100:                                                              # Verifica rango válido
    print("Calificación inválida")                                                                           # Error
elif calificacion <= 69:  
    print("Insuficiente")  
elif calificacion <= 79:  
    print("Bien")  
elif calificacion <= 89: 
    print("Muy bien")  
else:  
    print("Excelente")  

    Bien

"""--40. Escribe una función que tome dos parámetros: figura  (una cadena que puede ser "rectangulo" , "circulo" o 
"triangulo") y datos  (una tupla con los datos necesarios para calcular el área de la figura)"""

def area(figura, datos):                                             # figura es el nombre y datos son los números
    if figura == "rectangulo":                                      # si es un rectángulo
        base, altura = datos                                           # saco base y altura
        return base * altura                                           # área del rectángulo

    elif figura == "circulo":                                           # si es un círculo
        (radio,) = datos                                                    # saco el radio
        return 3.1416 * (radio ** 2)                              # área del círculo

    elif figura == "triangulo":                                       # si es un triángulo
        base, altura = datos                                             # saco base y altura
        return (base * altura) / 2                                    # área del triángulo

    else:
        return "Figura no válida"                                     # si no existe esa figura
    
print(area("rectangulo", (5, 3))) 

15

"""-- 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el 
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo 
siguiente:
 1. Solicita al usuario que ingrese el precio original de un artículo.
 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor 
a cero). Por ejemplo, descuento de 15€. 
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu 
programa de Python"""

precio = float(input("Ingresa el precio original: "))                                        # Pedimos el precio original


cupon = input("¿Tienes cupón de descuento? (si/no): ").lower()              # Preguntamos si tiene cupón

if cupon == "si":                                                                                                   # Si dice que sí
    valor = float(input("Ingresa el valor del cupón: "))
    if valor > 0:                                                                                                       # Si el cupón sirve
        precio_final = precio - valor
    else:                                                                                                                   # Cupón inválido
        print("Cupón no válido.")
        precio_final = precio
else:                                                                                                                       # Si no tiene cupón
    precio_final = precio

print("El precio final es:", precio_final)

El precio final es: 59.0