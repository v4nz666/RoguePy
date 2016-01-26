'''
Quit GameState
'''
import sys
import RoguePy.State.GameState as GameState

class Quit(GameState):
  def __init__(self, name, manager, ui):
    super(Quit, self).__init__(name, manager, ui)
    self.addHandler('quit', 1, self.tick)

  def tick(self):
    print "Quiting!"
    sys.exit()