# Funciones [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Este ejercicio representa ya un problema que forma parte de un juego
Lo que se desea realizar es una parte del juego "la generala".
El enunciado está armado a modo de guía, pueden resolver el problemla
de otra forma.
Si tienen dudas sobre el enunciado o alguno de los puntos por favor
comuníquelo por el campus y lo discutiremos entre todos, ya que siempre
puede haber varias interpretaciones de un mismo enunciado.

Deberá realizar una lista para guardar 5 dados, guardar los números
sacados en esa tirada de de dados (son 5 dados, cada uno del número 1 al 6)

1) El jugador tira la dados y saca 5 números aleatorios, puede usar
la función de "lista_aleatoria" para generar dichas lista de números.
Esa lista de datos se llamará "dados_tirados"
Lista "dados_tirados" se utiliza para guardar 5 dados, cada dado es de 6 caras,
es decir que cada dado puede valer un número de 1 a 6.

2) Luego debe analizar los 5 números y ver cual es el número que
más se repitio entre los 5 dados.
Debe usar la función de Python "max" con la "key" de list.count para
determinar cual fue el número que más se repitió en esa tirada. 
Consultar los ejemplos vistos en clase en donde se realizó esta operación con "max"

3) Una vez reconocido el número más repetido entre los 5 dados,
debe guardar en una variable aparte llamda "contador_generala"
cuantas veces se repitió hasta ahora el número más repetido. 
Ese número será el candidato para busscar sacar generala.
Si por ejemplo salió 4-4-2-1-4, debe quedarse con esos tres "4",
por lo canto el "contador_generala" valdrá 3, porque el primer número
más repetido fue 4, y este número salio tres veces en la primera tirada.

4) Debe volver a tira los dados, generar nuevos
números aleatorios.
Si en el contador "contador_generala" tengo 3 dados guardados
significa que ahora deberé tirar solo dos dados (5-3). 
Es decir que en este caso debería generar solo dos números
aleatorios nuevos con "lista_aleatoria"
Ahora tendré una nueva lista de "dados_tirados", en este caso
de dos nuevos números aleatorios entre 1 y 6 representando a los dados
tirados.

5) Luego de tirar nuevamente los datos en el paso anterior,
por ejemplo digamos que salieron los números: 4-1
Debo volver a contar cuantas veces aparece el número "4",
ya que es el número que estoy buscando almacenar para llegar a generala.
Se deberá aumentar el contador por cada cuatro que haya salido en la tirada.
Sino salió el "4" vuelvo a tirar sin aumentar el contador (repetir el punto 4)

5) Debe repetir este proceso hasta que el contador "contador_generala"
haya llegado a 5, es decir, he sacado 5 números iguales

NOTA: Recordar que en este ejemplo se buscó alcanzar la generala con "4" porque
fue el primero número más repetido en la primera tirada. Tener eso en cuenta que el
número que deberá buscar para alcanzar la generala depende de cual fue el más repetido
en la primera tirada.
'''

import random

# --------------------------------
# Dentro de esta sección copiar y crear
# todas las funciones que utilice

def lista_aleatoria (cantidad):              #funcion que arroja seis numeros aleatorios.
    dados_tirados = []                       #el el rango de uno a seis.
    for i in range(cantidad):                #y devuelve una lista de esos numeros
        dados_tirados.append(random.randrange(1,6+1))
    return dados_tirados


def numero_repetido (tirada):                 #funcion para determinar el numero que se repite
    dado_repetido = max(tirada, key=tirada.count)
    return dado_repetido





# --------------------------------
if __name__ == '__main__':
    print("¡juguemos a la generala!\n")
    # A partir de aquí escriba el código que
    # invoca a las funciones y resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda

    contador = 0   #variables globales del codigo
    cantidad = 5   #utilizadas como contador
    num_max = None
    tiradas_totales = 0

    while cantidad > 0:                            #bucle while, for, if
        for i in range (1,4):                      #imprime los num aleatorios
            if (num_max is None):                  #imprime el numero que se repite
                tirada = lista_aleatoria(cantidad) #imprime cuantas veces se repite dicho numero si se cumple la sentencia
                print('en la tirada numero', i, 'el resultado es: ', tirada)
                num_max = numero_repetido(tirada)
                print('el numero que mas se repite es:', num_max)
                cant_rep = tirada.count(num_max)
                print('el numero', num_max, 'se repite', cant_rep, 'veces')
                cantidad = cantidad - cant_rep
                print('ahora tienes', cantidad, 'dados')
            else:
                tirada = lista_aleatoria(cantidad)
                print('en la tirada numero', i, 'el resultado es: ', tirada)
                cant_rep = tirada.count(num_max)
                print('el numero', num_max, 'se repite', cant_rep, 'veces')
                cantidad = cantidad - cant_rep
                print('ahora tienes', cantidad, 'dados')
                if cantidad == 0:
                    break
            tiradas_totales+= 1     #tiradas maximas son tres, sino vuelve a empezar
            if tiradas_totales == 3:
                cantidad = 5
                tiradas = [None]
                num_max = None
                tiradas_totales = 0
            print('¿deseas intentarlo de nuevo?\n')
        contador+= 1

    print('¡¡¡genial, has hecho GENERALA!!!\n')
    print('los tiros fueron', tiradas_totales, 'y los intentos fueron', contador)
    




