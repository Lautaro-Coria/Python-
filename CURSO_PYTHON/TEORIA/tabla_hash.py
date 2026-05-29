class HashTable:
    def __init__(self):
        # Inicializa la colección como un diccionario vacío
        self.collection = {}

    def hash(self, string):
        # Suma los valores Unicode de cada carácter en la cadena
        return sum(ord(char) for char in string)

    def add(self, key, value):
        hash_key = self.hash(key)
        
        # Si el índice hash no existe, creamos el diccionario anidado
        if hash_key not in self.collection:
            self.collection[hash_key] = {}
            
        # Agregamos el par clave-valor específico
        self.collection[hash_key][key] = value

    def remove(self, key):
        hash_key = self.hash(key)
        
        # Verifica si el hash existe y si la clave específica está dentro
        if hash_key in self.collection and key in self.collection[hash_key]:
            del self.collection[hash_key][key]
            
            # Opcional: si el diccionario anidado quedó vacío, lo limpiamos
            if not self.collection[hash_key]:
                del self.collection[hash_key]

    def lookup(self, key):
        hash_key = self.hash(key)
        
        # Si existe la estructura y la clave, devuelve el valor, si no None
        if hash_key in self.collection and key in self.collection[hash_key]:
            return self.collection[hash_key][key]
        return None