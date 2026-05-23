class Planet:
    def __init__(self, name, planet_type, star): 
        #validar que sean string ( el tipo de dato que necesito )
        if not (isinstance(name, str) and isinstance (planet_type, str) and isinstance( star, str )): 
            raise TypeError("name, planet_type, and star must be strings")
        
        #validar que no sean string vacios. 
        if name == "" or planet_type == "" or star == "": 
            raise ValueError ("name, planet_type, and star cannot be empty str")        
        
        self.name= name 
        self.planet_type= planet_type
        self.star= star
    
    def orbit(self): 
        return f" {self.name} is orbiting around {self.star}"
    
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"

#creamos instancias 
planet_1 = Planet("Earth", "Terrestrial", "the Sun")
planet_2 = Planet("Jupiter", "Gas Giant", "the Sun")
planet_3 = Planet("Proxima Centauri b", "Super-Earth", "Proxima Centauri")

#imrpimir el objeto (usa automaticamente __str__())
print(planet_1)
print(planet_2)
print(planet_3)

#llamar al metodo orbit e imprimir el resultado: 
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())