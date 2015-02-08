'''
GameState
'''
from RoguePy import Input

class GameState(object):
  def __init__(self, name, manager):
    self._name = name
    self._manager = manager
    self._inputHandler = None
  
  def getName(self):
    return self._name
  
  def setBlocking(self, blocking):
    if blocking:
      self._inputHandler = Input.BlockingKeyboardHandler()
    else:
      self._inputHandler = Input.NonBlockingKeyboardHandler()
  
  def getInputHandler(self):
    return self._inputHandler
  
  def initKeyInputs(self, inputs):
    if self._inputHandler:
      self._inputHandler.initKeyInputs(inputs)
    
    
  
  
  ######
  # The good stuff
  ######
  def tick(self):
    self.processInput()
  
  def processInput(self):
    if isinstance(self._inputHandler, Input.InputHandler):
      self._inputHandler.handleInput()
  