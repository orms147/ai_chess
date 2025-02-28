
from const import *
from square import Square
from piece import *
from move import Move

class Board:

  def __init__(self):
    self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
    self._create()
    self._add_pieces('white')
    self._add_pieces('black')

  def calc_moves(self, piece, row, col):

    # Caculate move of piece

    # Move method 
    def pawn():
      piece = self.squares[row][col].piece
      if piece.color == 'black':
          if row != 1: piece.moved = True
      if piece.color == 'white':
          if row != 6: piece.moved = True
      # steps can move ( = 1 if moved)
      steps = 1 if piece.moved else 2

      # vertical move     piece.dir = -1 for white, = 1 for black
      start = row + piece.dir       
      end = row + piece.dir * (1 + steps)

      # Loop start -> end-1
      for move_row in range(start, end, piece.dir):  
          if Square.in_range(move_row):   # The piece in Board = true
              if self.squares[move_row][col].isempty(): # If don't have any piece
                  # new move
                  initial = Square(row, col)
                  final = Square(move_row, col, self.squares[move_row][col].piece)
                  move = Move(initial, final)
                  piece.add_move(move)
                  # got blocked
              else: break
              #not in range
          else: break
      
      # diagonal
      move_cols = [col - 1, col + 1]  # 2 col: right and left to move
      move_row = row + piece.dir
      for move_col in move_cols:
          if Square.in_range(move_col):
              if self.squares[move_row][move_col].has_enemy_piece(piece.color):
                  # new move
                  initial = Square(row, col)
                  final = Square(move_row, move_col, self.squares[move_row][move_col].piece)
                  move = Move(initial, final)
                  piece.add_move(move)  

    def knight():
      possible_moves = {
        (row - 2, col + 1),
        (row - 1, col + 2),
        (row + 1, col + 2),
        (row + 2, col + 1),
        (row + 2, col - 1),
        (row + 1, col - 2),
        (row - 1, col - 2),
        (row - 2, col - 1),
      }

      for possible_move in possible_moves:
        possible_move_row, possible_move_col = possible_move

        if Square.in_range(possible_move_row, possible_move_col):
          if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.color):
            # Create new move
            initial = Square(row, col, piece.color)
            final = Square(possible_move_row, possible_move_col, piece.color)
            #
            move = Move(initial, final)
            # append new valid move
            piece.add_move(move)


    if isinstance(piece, Pawn): pawn()                #if it's Pawn  ( == piece.name == "Pawn")
    if isinstance(piece, Knight): knight()
    if isinstance(piece, Bishop): pass
    if isinstance(piece, Rook): pass
    if isinstance(piece, Queen): pass
    if isinstance(piece, King): pass

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