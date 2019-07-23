class Rectangle:

    def __init__(self,length,width):
        self.length=length
        self.width=width
		
    def getPerimeter(self):
    	return 2*self.length*self.width
		
    def getArea(self):
    	return self.length*self.width
	
    def setLength(self,length):
    	self.length = length
		
    def setWidth(self,width):
        self.width = width


