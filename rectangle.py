class rectangle():


  def __init__(self,length,width):   
     
    self.length = length
    self.width = width

  def rectagle_area(self):
    return self.length*self.width
    


newRectangle = rectangle(12,10)
print("length"  ,newRectangle.length, "width" ,newRectangle.width  )