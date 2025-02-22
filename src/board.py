
from const import *
from square import Square
from piece import *

class Board:

  def __init__(self):
    self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
    self._create()
    self._add_pieces('white')
    self._add_pieces('black')

  def _create(self):
    for row in range(ROWS):
      for col in range(COLS):
        self.squares[row][col] = Square(row, col )

  def _add_pieces(self, color):

    #set row default for white and black
    row_pawn, row_other = (6, 7) if color == "white" else (1, 0)

    #set col
    #pawns  (row = 6 and any col)
    for col in range(COLS):
      self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

    #knight (row = 7 and col = 1 or 6)
    self.squares[row_other][1] = Square(row_other, 1, Knight(color))
    self.squares[row_other][6] = Square(row_other, 6, Knight(color))

    #bishop (row = 7 and col = 2 or 5)
    self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
    self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

    #Rook (row = 7 and col = 0 or 7)
    self.squares[row_other][0] = Square(row_other, 0, Rook(color))
    self.squares[row_other][7] = Square(row_other, 7, Rook(color))

    #queen (row = 7 and col = 3)
    self.squares[row_other][3] = Square(row_other, 3, Queen(color))

    #king
    self.squares[row_other][4] = Square(row_other, 4, King(color))