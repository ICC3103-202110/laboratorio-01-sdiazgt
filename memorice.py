import random
def crear_lista(cartas):
    numero = cartas
    #lista visual, solo aparecen datos censurados
    visual =[]
    for i in range(2):
        visual.append([])
        for j in range(numero):
            visual[i].append("#")
    #Mezclador de listas   
    mezclar = []
    for i in range(numero+1):
        if i > 0:
            mezclar.append(i)
            mezclar.append(i)
    random.shuffle(mezclar)
    
    #lista real, se encuentran todos los datos ocultos en orden
    Real = []
    for i in range(2):
        Real.append([])
        for j in range(numero):
            Real[i].append(mezclar[0])
            mezclar.pop(0)
    print(visual)
    print(Real)
    return [visual,Real]

def imprimir(tablero):
    tabla= tablero
    for i in range(len(tabla)):
        print(" ",i, end="") 
        
    print(" ")
    print("")
    x=0
    for a in zip(*tabla):         #Zip() fue sacado de Stackoverflow
        print(x,end="  ")
        print(" ".join(map(str, a)))
        x += 1
    return

def dar_vuelta(lista,posicion):
    real = lista[1]
    print(real)
    censura = lista[0]
    print(censura)
    x = int(posicion.split(sep=',')[0])
    y = int(posicion.split(sep=',')[1])
    #if censura[x-1][y-1] != "#" or " ":
        #reint = input("Elija una casilla nueva: ")
        #dar_vuelta(lista,reint)
    censura[x-1][y-1] = real[x-1][y-1]
    imprimir(censura)
    return censura

def verificar(tabla,n1,n2):
    tab = tabla
    puntaje = 0
    x1 = int(n1.split(sep=',')[0])
    y1 = int(n1.split(sep=',')[1])
    x2 = int(n2.split(sep=',')[0])
    y2 = int(n2.split(sep=',')[1])
    if int(tab[x1-1][y1-1]) == int(tab[x2-1][y2-1]):
        print("\nSon iguales")
        tab[x1-1][y1-1] = " "
        tab[x2-1][y2-1] = " "
        puntaje = 1
        return [tab, puntaje]
    else:
        print("\nNo son iguales")
        tab[x1-1][y1-1] = "#"
        tab[x2-1][y2-1] = "#"
        puntaje = 0
        return [tab,puntaje]




activo = 0
jugador1 = 0
jugador2 = 0
xx = ""
yy = ""
sumar = []
turno = 0
total = 0
cartas = int(input("cuantas cartas quieres: "))
crear = crear_lista(cartas)
while activo == 0:
    if total == cartas:
        print("Se termino el juego")
        if jugador1 > jugador2:
            print("Gano el jugador 1 con %s puntos"% (jugador1))
        elif jugador1 < jugador2:
            print("Gano el jugador 1 con %s puntos"% (jugador1))
        elif jugador1 == jugador2:
            print("Fue un Empate")
        break
    elif turno == 0:
        imprimir(crear[0])
        print("\nJugador 1 es tu turno!")
        xx = str(input("ingrese la cordenada en el Formato x,y (Ej. 1,1 es la primera):")) #primera posicion
        crear[0] = dar_vuelta(crear,xx)
        yy = str(input("ingrese la segunda cordenada en el Formato x,y (Ej. 1,1 es la primera):"))
        crear[0] = dar_vuelta(crear,yy)
        sumar = verificar(crear[0],xx,yy)
        crear[0] = sumar[0]
        if int(sumar[1]) == 1:
            jugador1 += 1
            total += 1
            turno = 0
            print("Jugador 1 Ganaste un punto")
            print("Tienes %s puntos en total" % (jugador1))
        elif int(sumar[1]) == 0:
            turno = 1
    elif total == cartas:
        print("Se termino el juego")
        break
    elif turno == 1:
        imprimir(crear[0])
        print("\nJugador 2 es tu turno!")
        xx = str(input("ingrese la cordenada en el Formato x,y (Ej. 1,1 es la primera):")) #primera posicion
        crear[0] = dar_vuelta(crear,xx)
        yy = str(input("ingrese la segunda cordenada en el Formato x,y (Ej. 1,1 es la primera):")) #segunda posicion
        crear[0] = dar_vuelta(crear,yy)
        sumar = verificar(crear[0],xx,yy)
        crear[0] = sumar[0]
        if int(sumar[1]) == 1:
            jugador2 += 1
            total += 1
            turno = 1
            print("Jugador 2 Ganaste un punto")
            print("Tienes %s puntos en total" % (jugador2))
        elif int(sumar[1]) == 0:
            turno = 0


        