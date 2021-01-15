from classes.Piece import Piece


class Player:
  def __init__(self,num):
    self.num = num
    self.pieces = []
    self.king = 0
  def add_piece(self,piece):
    self.pieces.append(piece)
  def remove_piece(self,piece):
    self.pieces.remove(piece)
  def print_pieces(self):
    print("Your pieces on the board:")
    for i,piece in enumerate(self.pieces):
      print(i," - ",piece," at coord",piece.position)
    print("\n")
  def set_king_piece(self,king):
    self.king_piece = king
  def update_turns(self,piece):
    piece.turns = piece.turns + 1


   