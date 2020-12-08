from Array2d import Array2D
from stack import Stack
class laberintoADT:
    """
    0=pasillo, 1=pared, s=salida, e= entrada
    pasillo=tupla((2,1),(,2,2),(2,3),(2,4),(3,2),(4,2))
    entrata en una tupla(5,2)
    salida (2,5)
    """
    def __init__(self, rens, cols, pasillos, entrata, salida ):
        self.__laberinto=Array2D(rens, cols, "1")
        for pasillo in pasillos:
            self.__laberinto.set_item(pasillo[0],pasillo[1],"0")
        self.set__entrada(entrata[0],entrada[1])
        self.set_salida(salida[0],salida[1])
        self.__camino=satck()
        self.__previa=None #guardara la posicion previa


    def to_string (self):
        self.__laberinto.to_string()
        """
        establece la entrata "E" en la matriz, verificar los limites de la entrata
        no se pueden exceder el numero de la matriz original
        """
    def set_entrada(self, ren, col ):
        #Terminar la validacion de las coordenadas
        self.__laberinto.set_item(ren,col, "E")
"""
establecer salida dentro de los limites perifericos dentro de la matriz
"""
    def set_salida(self, ren, col):
        #terminar las validaciones
        self.__laberinto.set_item(ren, col, "S")

"""
aplica los pares de reglas para poder verificar si hacer o no el backtracking
si en la posicion ya no hay pasillos entonces hacer backtracking
si evaluas una posicion en la que ya estuvieste, entonces la ignras
utilizar la uncion pop( )para poder dar un paso atras de la casila anteriorment evaluada

"""
    def resolver_laberinto(self):
        actual=self.__camino.peek()
        if actual[1]-1 \
        and self.__laberinto.get_item(actual[0], actual[1]-1)=="0"\
        and self.get_previa()!=actual[0],actual[1]-1\
        and  self.__laberinto.get_item(actual[0], actual[1]-1)!="X":
            self.set_previa(actual)
            self.__camino.push((actual[0], actual[1]-1))
        #busca arriba
        elif actual[1]-1!=-1\
        and self.__laberinto.get_item(actual[0], actual[1]-1)=="0"\
        and self.get_previa()!=actual[0],actual[1]-1\
        and  self.__laberinto.get_item(actual[0], actual[1]-1)!="X":
            self.set_previa(actual)
            self.__camino.push((actual[0]-1,actual[1]))
        # buscar derecha
        elif 1==0 :
            pass

        # buscar abajo
        elif 1 == 0 :
            pass
        else:
            self.__laberinto.set_item( actual[0] , actual[1] ,'X' )
            self.__previa = actual
            self.__camino.pop()



        #aplicando las reglas

    def imprimir_camino(self):
        self.__camino.to_string()

    def geet_pos_actual(self):
        return self.__camino.peek()


    def set_previa(self, pos_previa):
        self.__previa=pos_previa

    def get_previa(self):
        return self.__previa


    def es_salida(self, ren, col):
        return self.__laberinto.get_item(ren, col)=="s"

    def buscar_entrada(self):
        encontrado=False
        for renglon in range(self.__laberinto.get_num_rows()):
            for columa in range(self.__laberinto.get_num_cols()):
                tope=self.__camino.peek()# va aregresar una tupla
                if self.__laberitno.get_item(renglon,columa)=="E":
                    self.__camino.push(tuple(renglon, columa))
                    encontrado=True
        return encontrado
