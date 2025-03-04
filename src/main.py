import pygame
import sys

#import class
from const import *
from game import Game

class Main:

  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
    pygame.display.set_caption('Chess')
    self.game = Game() 


  def mainloop(self):
    
    #set default name :
    screen = self.screen 
    game = self.game
    board = game.board
    dragger = game.dragger  

    while True :
      game.show_bg(screen)  
      game.show_moves(screen)
      game.show_pieces(screen)
 
      if dragger.dragging:
        dragger.update_blit(screen)

      for event in pygame.event.get():

        #click down mouse event
        if event.type == pygame.MOUSEBUTTONDOWN:
          dragger.update_mouse(event.pos)
          clicked_col = int(dragger.mouseX // SQSIZE) 
          clicked_row = int(dragger.mouseY // SQSIZE)

          if board.squares[clicked_row][clicked_col].has_piece():
            piece = board.squares[clicked_row][clicked_col].piece
            board.calc_moves(piece, clicked_row, clicked_col)
            dragger.save_initial(event.pos) 
            dragger.drag_piece(piece)
            #show methods
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

        #mouse motion event
        elif event.type == pygame.MOUSEMOTION:
          if dragger.dragging:
            dragger.update_mouse(event.pos)
            game.show_bg(screen)
            game.show_pieces(screen)
            dragger.update_blit(screen)

        #click up xevent
        elif event.type == pygame.MOUSEBUTTONUP:
          dragger.undrag_piece()

        #out
        elif event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

      pygame.display.update()

main = Main()
main.mainloop()