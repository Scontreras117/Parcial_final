# Creamos la clase node
class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# Creamos la clase linked_list
class linked_list: 
    def __init__(self):
        self.head = None
        
    # Método para verificar si la estructura de datos esta vacia
    def is_empty(self):
        return self.head == None

    # Método para agregar elementos al final de la linked list
    def add_at_end(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)
        
    # Método para eleminar nodos
    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None       


        ################Esta es la función
        def pilas(pila):

            if pila.isempty:
              return None

            else:
              pila2 = linked_list
              for i in range(len(pila)-1): #Vaciado y llenado de la otra
                  pila2.add_at_end(pila.get_last_node) #Le ponemos el ultimo de la 1
                  pila.delete_node(pila.get_last_node) #borramos el ultimo de la 1

            return(pila2)
