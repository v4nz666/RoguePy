'''
Quit GameState
'''
import sys
import RoguePy.State.GameState as GameState

class Quit(GameState):

  def tick(self):
    print "Quiting!"
    sys.exit()