from classes.Board import Board
from classes.Piece import Piece
from classes.Pawn import Pawn
from classes.Bishop import Bishop
from classes.Rook import Rook
from classes.Knight import Knight
from classes.King import King
from classes.Queen import Queen
from classes.Player import Player
from classes.Setup import chess_pieces

import pygame
from pygame.locals import *


import os
import time



class Game: 
  def __init__(self,screen):
    self.player1 = Player(1)
    self.player2 = Player(2)
    
    self.board = Board(self.player1,self.player2)
    
    self.players = [self.player1,self.player2]
    self.setup()
    
    self.focus = 0

    self.running = True
    self.piece = 0
    self.piece_selected = False
    self.screen = screen

    self.loop()
  def setup(self):
    
    for i in range (8):
      piece = Pawn([i,1],"white",self.board)
      self.player1.add_piece(piece)

    for i in range (8):
      piece = Pawn([i,6],"black",self.board)
      self.player2.add_piece(piece)
      

    piece = Bishop([2,0],"white",self.board)
    self.player1.add_piece(piece)
    piece = Bishop([5,0],"white",self.board)
    self.player1.add_piece(piece)

    piece = Bishop([2,7],"black",self.board)
    self.player2.add_piece(piece)
    piece = Bishop([5,7],"black",self.board)
    self.player2.add_piece(piece)


    piece = Rook([0,0],"white",self.board)
    self.player1.add_piece(piece)
    piece = Rook([7,0],"white",self.board)
    self.player1.add_piece(piece)

    piece = Rook([0,7],"black",self.board)
    self.player2.add_piece(piece)
    piece = Rook([7,7],"black",self.board)
    self.player2.add_piece(piece)


    piece = Knight([1,0],"white",self.board)
    self.player1.add_piece(piece)
    piece = Knight([6,0],"white",self.board)
    self.player1.add_piece(piece)

    piece = Knight([1,7],"black",self.board)
    self.player2.add_piece(piece)
    piece = Knight([6,7],"black",self.board)
    self.player2.add_piece(piece)

    piece = King([4,0],"white",self.board)
    self.player1.add_piece(piece)
    self.player1.set_king_piece(piece)
    piece = King([4,7],"black",self.board)
    self.player2.add_piece(piece)
    self.player2.set_king_piece(piece)




    piece = Queen([3,0],"white",self.board)
    self.player1.add_piece(piece)
    piece = Queen([3,7],"black",self.board)
    self.player2.add_piece(piece)


    pass
 
  def mouse_coords(self):
    screenPos = list(pygame.mouse.get_pos())
    boardPos = [int(screenPos[0]/80),int(screenPos[1]/80)]
    return boardPos


  def check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
       self.running = False
      elif event.type == MOUSEBUTTONDOWN:
        pos = self.mouse_coords()
        if pos:
          if self.piece_selected:
            if self.get_piece_from_coord(pos) != 0 and self.get_piece_from_coord(pos).color == self.players[self.focus].color:
              self.piece = self.get_piece_from_coord(pos)
            else:
              self.turn(self.piece,pos)
              self.piece_selected = False
          else:
            if self.get_piece_from_coord(pos):
              self.piece = self.get_piece_from_coord(pos)
              self.piece_selected = True


  def take_move_input(self,player,piece,pos):

    possible_positions = self.board.filter(piece.possible_positions())
    if not possible_positions:
      return False
    if pos not in possible_positions or (piece.color == "black" and player.num == 1) or (piece.color == "white" and player.num == 2):
      return False
    piece.moveTo(pos)
    
    player.update_turns(piece)
    return True
      

  def checkmate_check(self,player):
    other_player = self.player2 if player.num ==1 else self.player1  
    ret = self.board.check_checkmate(player.king_piece,other_player.pieces)
    if ret:
      print("%s king is in checkmate %s player has won" % (player.color, other_player.color))
      time.sleep(100)

  def get_piece_from_coord(self,pos):
    piece = self.board.getSquare(pos)
    return piece

  def turn(self,piece,pos):
      player = self.players[self.focus]

      ret = self.take_move_input(player,piece,pos)
      
      if ret:
        if self.focus == 0:
          self.focus = 1
        else:
          self.focus = 0
      
      #self.checkmate_check(self.player1)
      #self.checkmate_check(self.player2)
  def draw_selected(self):
    if self.piece_selected:
      if self.piece.color == self.players[self.focus].color:
        self.screen.blit(chess_pieces["selected"],(80*self.piece.position[0],80*self.piece.position[1]))
    


  def loop(self):
    while self.running:
      self.check_events()

      pygame.display.update()

      #Draw board
      self.board.draw(self.screen)
      self.draw_selected()