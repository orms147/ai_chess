import pygame

from const import *
from board import Board
from dragger import Dragger

class Game:

  def __init__(self):
    #set default
    self.board = Board()
    self.dragger = Dragger()

  #Show back ground methods
  def show_bg(self, surface):
    for row in range(ROWS):
      for col in range(COLS):
        if(row + col) % 2 == 0 :
          color = (234, 234, 200) #light green
        else:
          color = (119, 154, 88) #dark green
        
        rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

        pygame.draw.rect(surface, color, rect)
  
  def show_pieces(self, surface):
    for row in range(ROWS):
      for col in range(COLS):
        #has piece ?
        if self.board.squares[row][col].has_piece():      #have piece in real square :> 
          piece = self.board.squares[row][col].piece      #set call default\
          
          #all pieces except dragger piece 
          if piece is not self.dragger.piece:
            piece.set_texture()
            img = pygame.image.load(piece.texture)              #have set_texture method in piece
            img_center = col * SQSIZE + SQSIZE  // 2, row * SQSIZE + SQSIZE  // 2   #basic math center
            piece.texture_rect = img.get_rect(center=img_center)
            surface.blit(img, piece.texture_rect)