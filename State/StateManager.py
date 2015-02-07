'''
StateManager
'''
from RoguePy.State.GameState import GameState

class StateManager():
  def __init__(self):
    self._states = {}
    self._currentState = None
    self._nextState = None
  
  def addState(self, gameState):
    self._states[gameState.getName()] = gameState
  
  def getCurrentState(self):
    return self._currentState
  def setCurrentState(self, stateName):
    self._currentState = self._states[stateName]
  
  def getNextState(self):
    return self._nextState
  def setNextState(self, stateName):
    self._nextState = self._states[stateName]
  
  def stateTransition(self):
    # do some stuff.. callbacks and the like
    self._currentState = self._nextState
  