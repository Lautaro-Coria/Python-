# Clase base para vectores en 2 dimensiones
class R2Vector:
    def __init__(self, *, x, y):
        # Inicializamos los componentes x e y
        self.x = x
        self.y = y

    def norm(self):
        # Calcula la norma (longitud del vector) como √(x² + y² + ...)
        return sum(val**2 for val in vars(self).values())**0.5

    def __str__(self):
        # Representación "bonita" del vector, como tupla (x, y, ...)
        return str(tuple(getattr(self, i) for i in vars(self)))

    def __repr__(self):
        # Representación más técnica, útil para debugging
        # Ejemplo: R2Vector(x=2, y=3)
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def __add__(self, other):
        # Suma de vectores (componente a componente)
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __sub__(self, other):
        # Resta de vectores (componente a componente)
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __mul__(self, other):
        # Multiplicación por escalar (número)
        if type(other) in (int, float):
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)
        # Producto escalar (dot product) entre dos vectores
        elif type(self) == type(other):
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)
        return NotImplemented

    def __eq__(self, other):
        # Igualdad: todos los componentes deben coincidir
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))

    def __ne__(self, other):
        # Desigualdad: lo contrario a ==
        return not self == other

    def __lt__(self, other):
        # Menor que: compara según la norma del vector
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    def __gt__(self, other):
        # Mayor que: compara según la norma del vector
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    def __le__(self, other):
        # Menor o igual: opuesto de >
        return not self > other

    def __ge__(self, other):
        # Mayor o igual: opuesto de <
        return not self < other


# Clase hija para vectores en 3 dimensiones
class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        # Llamamos al constructor de R2Vector para inicializar x e y
        super().__init__(x=x, y=y)
        # Agregamos el componente z
        self.z = z

    def cross(self, other):
        # Producto vectorial (cross product), válido solo en 3D
        if type(self) != type(other):
            return NotImplemented
        kwargs = {
            'x': self.y * other.z - self.z * other.y,   # axb componente X
            'y': self.z * other.x - self.x * other.z,   # axb componente Y
            'z': self.x * other.y - self.y * other.x    # axb componente Z
        }
        # Retorna un nuevo vector resultado del producto cruz
        return self.__class__(**kwargs)


# ------------------------------
# Ejemplos de uso
# ------------------------------

# Creamos dos vectores en 3D
v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)

# Mostramos los vectores
print(f'v1 = {v1}')
print(f'v2 = {v2}')

# Operaciones básicas
v3 = v1 + v2     # suma
print(f'v1 + v2 = {v3}')

v4 = v1 - v2     # resta
print(f'v1 - v2 = {v4}')

v5 = v1 * v2     # producto escalar
print(f'v1 * v2 = {v5}')

v6 = v1.cross(v2)  # producto vectorial
print (f'v1 x v2 = {v6}')