class Lista: 
    def __init__(self):
        self.items=[]
        self.is_array=True
    
    def agregar(self,objeto):
        self.items.append(objeto)

    def eliminar(self, indice):
        if indice < 0 or indice >= len(self.items):
            raise IndexError("El índice está fuera de rango")
        self.items.pop(indice)
    
    def actualizar(self, indice, nuevo_objeto):
        if indice < 0 or indice >= len(self.items):
            raise IndexError("El índice está fuera de rango")
        self.items[indice] = nuevo_objeto

    
