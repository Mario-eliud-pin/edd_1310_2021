class NodoArbol:
    def __init__(self, value, left=None , right=None ):
        self.data=value
        self.left=left
        self.right=right

class BinarySearchtree:
    def __init__(self):
        self.__root=None

    def insert(self, value):
        #regla 1
        if self.__root==None:
            self.__root=NodoArbol(value, None, None)
        #regla 2
        else:
            self.__insert__(self.__root, value)

    def __insert__(self, nodo, value ):
        #nodo es una copia
        if nodo.data==value:
            print("el dato ya existe y no insertara nada ")
        elif value > nodo.data:
            #alicamos las 2 reglas
            if nodo.left==None:
                nodo.left=NodoArbol(value)
            else:
                seelf.__insert__(nodo.left, value)
        else:
            if nodo.right==None:
                nodo.right=NodoArbol(value)
            else:
                self.__insert__(nodo.right, value )

    def __recorrido_in(self, nodo):
        if nodo!=None:
            self.__recorrido_in(nodo.left)
            print(nodo.data)
            self.__recorrido_in(nodo.right)

   def __recorrido_pos( self, nodo ):
        if nodo:
            self.__recorrido_pos(nodo.left)
            self.__recorrido_pos(nodo.right)
            print(nodo.data, end=", ")

    def __recorrido_pre(self,nodo):
        if nodo:
            print(nodo.data, end=", ")
            self.__recorrido_pre(nodo.left)
            self.__recorrico_pre(nodo.right)

    def transversal(self, format="inorden"):
        if format=="inorden":
            self.__recorrido_in(self.__root)
        elif format =="preorden":
            print("recorrico en preorden")
        elif format =="posorden":
            print("posorden")
        else:
            print("Error, ese formato no existe ")
        print("")

    def search(self, value ):
        if self.__root:
            return None
        else:
            return self.__search(self.__root, value )

    def __search(self,nodo,value):
        if nodo==None:
            print("caso base ") #si es un arbol vacio? caso base
            return None
        elif nodo.data==value: #caso base de recursividad
            print("encontrado ")
            return nodo
        elif value<nodo.data:
            print("buscar a la izquierda")
            return self.__search(nodo.left, value)
        else:
            print("buscar a la derecha")
            return self.__search(nodo.right, value )

    def remove(self, value):
        # eliminar hoja
        #eliminar padre con un solo hijo
        # eliminar un nodo con dos hijos
        if self.__root==None:
            print("Nada que eliminar")
        else:
            self.__remove(None, None, self.__root, value )

    def __remove(self, padre_hi, padre_hd, actual, value ):
        if actual==None: # caso base
            print("caso base")
            return None
        elif actual.data==value: # caso base
            print("encontrado",actual.data)
            #caso 1: hoja
            if actual.left==None and actual.right==None:
                if padre_hi!=None:

                else:
                    padre_hd.right=None
            #caso 2: un hijo
            if (actual.left!= None and actual.rigth==None) or (actual.left== None and actual.rigth!=None):
                print("es un nodo con un hijo", actual.data)
                if actual.left!=None:
                    actual.data=ctual.left.data
                    actual.lrft=None
                else:
                    actual.data=actual.right.data
                    actual.rigth=None

            #caso 3
            
        elif value<actual.data:
            print("buscar a la iquierda")
            self.__remove(actual, None, actual.left, value )
        else:
            print("buscando a la derecha")
            self.__remove(None, actual, actual.right, value )
