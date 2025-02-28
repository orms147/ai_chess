class Square:

  def __init__(self, row, col, piece=None):
    self.row = row
    self.col = col
    self.piece = piece

  def has_piece(self):
    return self.piece !=None  #return true if not None
  
  def isempty(self):
    return not self.has_piece()
  
  # Same color
  def has_teammate(self, color):
    return self.has_piece() and self.piece.color == color

  # Black >< White
  def has_enemy_piece(self, color):
    return self.has_piece() and self.piece.color != color
  
  # Empty or is enemy
  def isempty_or_enemy(self, color):
    return self.isempty() or self.has_enemy_piece(color)

  # Check valid in the board
  @staticmethod     
  def in_range(*args):
    for arg in args:
      if arg < 0 or arg > 7:
        return False
    return True
  
#s = Square()
print(Square.in_range(2, 2, 5, 3))