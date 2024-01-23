#-------------------------JUEGO DE PIEDRA PAPEL O TIJERAS.---------------------------
# codigo completamente de mi autoria.. por lo que tengo claro que se puede optimizar
# haciendo un mejor uso de bucles y no tantos condicionales pero en esencia funciona
# en el futuro pienso actualizar este codigo haciendolo mas limpio y optimo.

# importamos la libreria "random" para hacer uso de un metodo mas adelante.
import random

# en este codigo quise practicar la POO (programación orientada a objetos)
# ademas haciendo uso de "clases", "objetos", "funciones", "condicionales", "bucles"
# se puede practicar de todo un poco a continuación...

#creamos la clase juego que tendra como parametros el nombre del jugador, las vidas y
# el elemento que usara sea piedra papal o tijeras:
class JuegoRSP():
    def __init__(self, nombre_jugador, vidas, elemento_usado ):
        self.nombre = nombre_jugador
        self.vidas = vidas
        self.RSP = elemento_usado

# creamos el objeto usuario1 que en efecto es el jugador, primero pidiendo su nombre
# las vidas seran asignadas por defecto como 3
# y pedimos el elemento que usara en el primer turno con un menu numerico; .1 .2 .3
usuario1 = JuegoRSP(input("Introdusca su nombre de jugador: "),
3,(input("""escoje un numero para asi usar ese elemento este primer turno
1.piedra
2.tijeras
3.papel
""")))

# luego creamos el objeto maquina, que en esencia es contra quien nos vamos a enfrentar.
# su nombre por defecto, igualmente 3 vidas por defecto y el elemento a usar
# sera escojido aleatoriamente por medio del uso del metodo "int(random.randint(1,3))"
# que nos dara un numero entero entre 1 y 3 siendo estos igualmente  piedra tijeras papel.
maquina1 = JuegoRSP("MAQUINA1", 3 , int(random.randint(1,3)))

# esta funcion esta orientada al objeto usuario y es donde por medio del menu numerico
# sera escojido equivalentemente el elemento ya sea piedra, papel o tijeras
# ademas de un manejo de exepciones por si el usuario ingreso algo diferente a los numeros del menu.
def Escojer_correctamente_rsp():
    while True:
        if usuario1.RSP == "1":
            usuario1.RSP = "piedra"
            return usuario1.RSP
        elif usuario1.RSP == "2":
            usuario1.RSP = "tijeras"
            return usuario1.RSP
        elif usuario1.RSP == "3":
            usuario1.RSP = "papel"
            return usuario1.RSP
        else:
            try:
                usuario1.RSP = (input("""----------------------------------------------------
vuelve a escojer tu elemento 1.piedra, 2.tijeras, 3. papel: """))
            except:
                print("porfavor escoje ""1"" para piedra, ""2"" para tijeras y ""3"" para papel.")  

# esta funcion esta orientada al objeto maquina y es donde se le da el valor del elemento
# que usara la maquina cuando ya este en el bucle que veremos mas adelante y su respectiva equivalencia.
def maquina_elemento_RSP():
    maquina1.RSP = int(random.randint(1,3))
    if maquina1.RSP == 1:
        maquina1.RSP = "piedra"
        return maquina1.RSP
    elif maquina1.RSP == 2:
        maquina1.RSP = "tijeras"
        return maquina1.RSP
    elif maquina1.RSP == 3:
        maquina1.RSP = "papel"
        return maquina1.RSP

# en esta funcion es donde haremos los respectivos enfrentamientos de los elementos escojidos.
def ver_que_elemento_gana():
    while True:
        if maquina1.RSP == "piedra" and usuario1.RSP =="tijeras":
            usuario1.vidas -= 1
            print(" tu pierdes este enfrentamiento")
        elif maquina1.RSP == "piedra" and usuario1.RSP =="papel":
            maquina1.vidas -= 1
            print(" tu ganas este enfrentamiento")
        elif maquina1.RSP == usuario1.RSP:
            print(" empatan este enfrentamiento")
        elif maquina1.RSP == "papel" and usuario1.RSP =="tijeras":
            maquina1.vidas -= 1
            print(" tu ganas este enfrentamiento")
        elif maquina1.RSP == "papel" and usuario1.RSP =="piedra":
            usuario1.vidas -= 1
            print(" tu pierdes este enfrentamiento")
        elif maquina1.RSP == "tijeras" and usuario1.RSP =="piedra":
            maquina1.vidas -= 1
            print(" tu ganas este enfrentamiento")
        elif maquina1.RSP == "tijeras" and usuario1.RSP =="papel":
            usuario1.vidas -= 1
            print(" tu pierdes este enfrentamiento")
        break

# aqui esta el bucle que es donde nos encontraremos realizando los enfrentamientos 
# hasta que el usuario o la maquina pierdan sus 3 vidas.
while usuario1.vidas >= 1 and maquina1.vidas >= 1:
    # ejecutamos las funciones orientadas a los objetos que vimos anteriormente
    usuario1.RSP = Escojer_correctamente_rsp()
    maquina1.RSP = maquina_elemento_RSP()
    # interfaz que nos grafica nuestro nombre, cuantas vidas nos quedan y el elemento usado
    print("--------------------------------------------------------------------------------")
    print(f"Bien {usuario1.nombre.upper()} ahora vamos a jugar contra la maquina")
    print(f"Tienes {usuario1.vidas} vidas") 
    print(f"Y usaste {usuario1.RSP.upper()} en este turno")
    print("--------------------------------------------------------------------------------")
    # igualmente para la maquina.
    print("--------------------------------------------------------------------------------")
    print(f"ahora {maquina1.nombre}")
    print(f"Tiene {maquina1.vidas} vidas") 
    print(f"Y este turno uso {maquina1.RSP.upper()}")
    print("--------------------------------------------------------------------------------")
    # y al final del bucle ejecutamos esta funcion que nos dira el resultado
    # del enfrentamiento de este turno.
    ver_que_elemento_gana()

# si el codigo sale del bucle quiere decir que alguien perdio sus 3 vidas ya sea el usuario
# o la maquina por lo tanto el ultimo condicional nos dira el resultado del juego.
if usuario1.vidas == 0:
    print("----------------------------PERDISTE EL JUEGO-----------------------------------")
else:
    print("----------------------------GANASTE EL JUEGO------------------------------------")










