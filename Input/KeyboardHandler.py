from InputHandler import InputHandler

class KeyboardHandler(InputHandler) :
  def __init__(self):
    self.key = None
  
  def initInputs(self, inputs):
    self.initKeyInputs(inputs)
    
  def handleKeyInput(self, key):
    for name in self.inputs:
      cmd = self.inputs[name]
      if ( cmd['key'] and cmd['key'] == key.vk ) or (
        cmd['ch'] and ( ord(cmd['ch'].lower()) == key.c or ord(cmd['ch'].upper()) == key.c ) ):
          return cmd['fn']()
    return self
