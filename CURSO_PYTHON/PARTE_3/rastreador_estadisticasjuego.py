class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    # Propiedad de solo lectura para 'name'
    @property
    def name(self):
        return self._name

    # Getter y Setter para 'health'
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        # Limita la salud para que no sea menor a 0 ni mayor a 100
        self._health = max(0, min(value, 100))

    # Getter y Setter para 'mana'
    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        # Limita el mana para que no sea menor a 0 ni mayor a 50
        self._mana = max(0, min(value, 50))

    # Propiedad de solo lectura para 'level'
    @property
    def level(self):
        return self._level

    # Método para subir de nivel
    def level_up(self):
        self._level += 1
        self.health = 100  # Usa el setter para restablecer la salud
        self.mana = 50     # Usa el setter para restablecer el mana
        print(f"{self.name} leveled up to {self.level}!")

    # Representación en cadena del objeto
    def __str__(self):
        return (f"Name: {self.name} | "
                f"Level: {self.level} | "
                f"Health: {self.health}/100 | "
                f"Mana: {self.mana}/50")