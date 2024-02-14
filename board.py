
class Piece:
    pass


class Cell:
    def __init__(self, color: str, piece: Piece | None) -> None:
        self.color = color
        self.piece = piece


class Board:
    def __init__(self, border_size: int) -> None:
#        self.cells: list[Cell] = border_size * border_size
        self.num_cells: int = border_size*border_size
