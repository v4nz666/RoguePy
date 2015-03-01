import materials


class Cell(object):
  def __init__(self, material = materials.EMPTY):
    """
    Cell class. Represents one space on the Map

    :return: self
    """

    self.material = material
    print self.material


  def setMaterial(self, material):
    print "Setting material " + str(material)
    self.material = material

  def transparent(self):
    return self.material.see

  def passable(self):
    return self.material.walk