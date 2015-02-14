from libtcod import libtcod
import UI.UI
import UI.View
from Core import *
from State import *
from Input import *

def setFps(fps):
  libtcod.sys_set_fps(fps)
