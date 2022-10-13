def listas():
    #Metodo append
    lista = [1,2,3,4,5]
    lista.append(6)
    print(lista)

    #metodo clear
    lista.clear()
    print(lista)

    #metodo extend
    lista1 = [1,2,3]
    lista2 = [4,5,6]
    lista1.extend(lista2)
    print(lista1)

    #metodo count
    Universo = ["mundo", "tierra", "universo", "planeta","planeta","mundo","planeta","universo","tierra"]
    print(Universo.count("planeta"))

    #metodo index
    Universo = ["mundo", "tierra", "universo", "planeta","planeta","mundo","planeta","universo","tierra"]
    print(Universo.index("universo"))

    #metodo insert
    lis = [1,2,3]
    lis.insert(0,0)
    print(lis)

    lis1 = [5,10,15,25]
    lis1.insert(-1,20)
    print(lis1)

    #metodo pop
    numeros = [10,20,30,40,50]
    print(numeros.pop())
    print(numeros)

    #metodo remove
    l = [20,30,30,30,40]
    l.remove(30)
    print(l)

    #metodo reverse
    reverso = [10,9,8,7,6,5,4]
    reverso.reverse()
    print(reverso)

    #metodo sort
    ordena = [5,-10,35,0,-65,100]
    ordena.sort()
    print(ordena)

    #Compresion de una lista
    personas=[('pedro',33),('ana',3),('juan',13),('carla',45)]
    personas_mayores=[per for per in personas if per[1]>=18]
    print(personas_mayores)

def tuplas():
    #A continuacin usaremos tuplas y secuenias
    tupla=(1,2,3,4,"mundo")
    print(tupla[0])

def conjuntos():
    #Conjuntos
    Fruits = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(Fruits)

    #compara si el elemento se encuentra detro del conjunto
    print('orange' in Fruits)
    print('crabgrass' in Fruits)


    #operaciones con set conjuntos
    a = set("hello")
    b = set("world")

    #Mostrata unicamente las letras de a
    print(a)

    #letras en a pero no en b
    print(a - b)

    #letras en a o b
    print(a | b)

    #letras en a y b
    print(a & b)

    #letras en a o b pero no en ambas
    print(a^b)

    #Comprension en conjuntos
    a = {x for x in 'abracadabra' if x not in 'abc'}
    print(a)

def diccionarios():
    #Diccionarios
    Años = {"Maria":1994, "Jorge":1953 }
    Años['guido'] = 1983

    print(Años)

    #Muestra la lista de los nombres
    print(list(Años))

    #ordena el diccionario
    print(sorted(Años))

    #comprueba si esta en la lista o no
    print('guido' in Años)
    print('Maria' not in Años)

listas()
conjuntos()
tuplas()
diccionarios()


















