import pygame

chess_pieces = {}

def setup():
    WIDTH = 80*8
    HEIGHT = 80*8


    dir = "assets/"
    chess_files = ["Base.png","whitePawn.png","whiteKnight.png","whiteRook.png","whiteBishop.png","whiteQueen.png","whiteKing.png","blackPawn.png","blackKnight.png","blackRook.png","blackBishop.png","blackQueen.png","blackKing.png","selected.png"]
    chess_names = ["base","w_pawn","w_knight","w_rook","w_bishop","w_queen","w_king","b_pawn","b_knight","b_rook","b_bishop","b_queen","b_king","selcted"] 
  
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    for i in range(13):
      file = chess_files[i]
      string = chess_names[i] 
      chess_pieces[string] = pygame.image.load(dir + file)
    
    icon = pygame.image.load(dir + "icon.png")
    pygame.display.set_icon(icon)
    return screen

