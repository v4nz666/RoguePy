from InputHandler import InputHandler

class KeyboardHandler(InputHandler) :
  def __init__(self):
    self.keyInputs = {}
    self.key = None
  
  def addKeyInputs(self, inputs):
    for i in inputs:
      self.keyInputs[i] = inputs[i]
    
  
  def handleKeyInput(self, key):
    for name in self.keyInputs:
      cmd = self.keyInputs[name]
      if ( cmd['key'] and cmd['key'] == key.vk ) or (
        cmd['ch'] and ( ord(cmd['ch'].lower()) == key.c or ord(cmd['ch'].upper()) == key.c ) ):
          return cmd['fn']()
    return self