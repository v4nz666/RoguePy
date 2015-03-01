from RoguePy.libtcod import libtcod
from Terrain import Terrain

EMPTY = Terrain(True, True, "Empty space")

WALL = Terrain(False, False, "Stone wall")\
  .setColors(libtcod.light_grey)\
  .setChar('#')

FLOOR = Terrain(True, True, "Stone floor")\
  .setColors(libtcod.dark_grey)\
  .setChar('.')