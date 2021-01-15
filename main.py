import pygame

from classes.Game import Game
from classes.Setup import setup


if __name__ == "__main__":
  screen = setup()
  game = Game(screen)
