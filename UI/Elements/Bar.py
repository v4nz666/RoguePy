'''
Documentation, License etc.

@package RoguePy.UI
'''
from RoguePy.libtcod import libtcod
from RoguePy.UI.Elements import Element

class Bar(Element):
  
  def __init__(self, x, y, w, h=1):
    super(Bar, self).__init__(x, y, w, h)
    self.setMin(0)
    self.setMax(100)
    self.setVal(100)
    
    self.chars = [
      libtcod.CHAR_BLOCK1,
      libtcod.CHAR_BLOCK2,
      libtcod.CHAR_BLOCK3
    ]
    print "Bar width " + str(self.width)
  
  def setMin(self, min):
    self._min = min
  def setMax(self,max):
    self._max = max
  def getMin(self):
    return self._min
  def getMax(self):
    return self._max
  
  def setVal(self,val):
    if val > self._max:
      val = self._max
    elif val < self._min:
      val = self._min
    self._val = val
  def getVal(self):
    return self._val
  
  def setChars(self,chars):
    self.chars = chars
  def getChars(self):
    return self.chars
  
  def draw(self):
    max = float(self._max - self._min)
    val = self._val - self._min
    
    chars = len(self.chars)
    steps = self.width * chars
    fullSteps = int(val / max * steps)
    fullChars = int(fullSteps / chars)

    lastChar = self.chars[fullSteps % chars]
    
    for y in range(self.height):
      for i in range(fullChars):
        libtcod.console_put_char(self.console, i, y, self.chars[-1])
      if lastChar > 0:
        libtcod.console_put_char(self.console, fullChars, y, lastChar)