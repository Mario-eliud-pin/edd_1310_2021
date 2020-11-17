class Nodo:
    def __init__(self, valor, siguiente= None):
        self.data=valor
        self.siguiente=siguiente

class Linked_List:
    def __init__(self):
        self.head=None # cuando creamos la cabeza iicialmente no apunta  nada

    def is_empty(self):
        return self.__head==None

    def append(self, valor): # curr_node va  ahacer una copia de la cabeza y encuentra el ultimo elemento y agrega un elemento en None y el nuevo elemento apuntaria a generaciones
        nuevo=Nodo(valor)
        if self.__head==None: #es equivalente al metodo is_empty
            self.__head=nuevo
        else:
            curr_node = self.__head # self
            while curr_node.siguiente != None:
                curr_node = curr_node.siguiente #se garantisa que curr_node apunta al ultimo elementos
            curr_node.siguiente=nuevo
    def transversal(self):
        curr_node=self.__head
        while curr_node != None:
            print(f"{curr_node.data}->", end="")
            curr_node=curr_node.siguiente
        print("")
    def remove(self,valor):
        curr_node= self.__head
        while curr_node.data != valor and curr_node.siguiente != None: # validar si es diferente al valor y si n existe un valor pues se recorre al final
            curr_node= curr_node.siguiente
        if curr_node.data=valor:
