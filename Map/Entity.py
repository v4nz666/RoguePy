from RoguePy.UI import Colors

class Entity(object):
  def __init__(self, name):
    self.name = name
    self.char = ' '
    self.color = Colors.black

  def setChar(self, ch):
    self.char = ch
  def setColor(self, color):
    self.color = color
