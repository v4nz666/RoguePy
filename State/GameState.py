'''
GameState
'''
from RoguePy.Input import Input

class GameState(object):
  def __init__(self, name):
    self._name = name
    self._inputHandler = None
  
  def getName(self):
    return self._name
  
  def tick(self):
    self.processInput()
  
  
  ######
  # The good stuff
  ######
  def processInput(self):
    if isinstance(self._inputHandler, Input):
      self._inputHandler.handleInput()