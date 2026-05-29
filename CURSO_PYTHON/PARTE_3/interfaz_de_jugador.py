import abc
import random

class Player(abc.ABC):
    def __init__(self) -> None:
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        selected_move = random.choice(self.moves)
        
        new_x = self.position[0] + selected_move[0]
        new_y = self.position[1] + selected_move[1]
        
        self.position = (new_x, new_y)
        self.path.append(self.position)
        
        return self.position

    @abc.abstractmethod
    def level_up(self):
        pass


class Pawn(Player):
    def __init__(self) -> None:
        super().__init__()
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self) -> None:
        diagonal_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.moves.extend(diagonal_moves)

if __name__ == '__main__':
    # Creamos un peón
    mi_peon = Pawn()
    print("Posición inicial:", mi_peon.position)
    print("Movimientos iniciales:", mi_peon.moves)
    
    # Hacemos que se mueva una vez
    nueva_pos = mi_peon.make_move()
    print("Se movió a:", nueva_pos)
    print("Ruta recorrida:", mi_peon.path)
    
    # Sube de nivel y aprende diagonales
    mi_peon.level_up()
    print("Movimientos después de subir de nivel:", mi_peon.moves)