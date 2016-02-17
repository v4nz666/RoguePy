from InputHandler import InputHandler
from RoguePy.libtcod import libtcod

class KeyboardHandler(InputHandler) :
  def __init__(self):
    self.keyInputs = {}
    self.key = None
    self.gotInput = False

  def handleInput(self):
    key = libtcod.console_check_for_keypress(libtcod.KEY_PRESSED)
    if key.vk != libtcod.KEY_NONE:
      self.handleKeyInput(key)
      self.gotInput = True
    else:
      self.gotInput = False

  def _addKeyInputs(self, inputs):
    for i in inputs:
      self.keyInputs[i] = inputs[i]
  def setInputs(self, inputs):
    self.keyInputs = {}
    self._addKeyInputs(inputs)
  
  
  def handleKeyInput(self, key):
    for name in self.keyInputs:
      cmd = self.keyInputs[name]
      if ( cmd['key'] and ( cmd['key'] == key.vk or str(cmd['key']).lower() == "any") ) or \
        ( cmd['ch'] and ( ord(cmd['ch']) == key.c ) ):
          cmd['fn']()
