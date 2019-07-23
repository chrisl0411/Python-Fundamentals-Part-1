#  File: LinearEquations.py
#  Description: HW11: Linear Equations
#  Student's Name: Christopher Lee
#  Student's UT EID: cl37976
#  Identifier: XXXXXXXXXX
#  Course Name: CS 303E 
#  Unique Number: 51200
#
#  Date Created: 10/29/18
#  Date Last Modified: 10/31/18

############################################################################

#defines a class called "LinearEquation" with several methods
class LinearEquation:
    def __init__(self,m,b):
        self.m = m
        self.b = b

    #returns the string of the linear equation
    def showEq(self):
        self.mabs = abs(self.m)
        self.babs = abs(self.b)
        
        if self.m == 0 and self.b == 0:
            self.equation = ""
        elif self.m == 0:
            if self.b > 0:
                self.bsign = ""
            elif self.b < 0:
                self.bsign = "- "
            self.equation = self.bsign+""+str(self.babs)
        elif self.b == 0:
            if self.m < 0:
                self.msign = "- "
            elif self.mabs == 1:
                self.mabs = ""
            else:
                self.msign = ""
            self.equation = self.msign+str(self.mabs)+"x "
        else:
            if self.m < 0:
                self.msign = "- "
                if self.b > 0:
                    self.bsign = "+ "
                else:
                    self.bsign = "- "
            elif self.m > 0:
                self.msign = ""
                if self.b > 0:
                    self.bsign = "+ "
                else:
                    self.bsign = "- "
            elif self.m == 1:
                self.mabs = ""
            self.equation = self.msign+str(self.mabs)+"x "+self.bsign+str(self.babs)
            
        return self.equation

    #adds two LinearEquations and returns a new LinearEquation
    def add(self,equation):
        self.m2 = equation.m
        self.b2 = equation.b
        self.newm = self.m + self.m2
        self.newb = self.b + self.b2
        return LinearEquation(self.newm,self.newb)

    #subtracts two LinearEquations and returns a new LinearEquation
    def sub(self,equation):
        self.m2 = equation.m
        self.b2 = equation.b
        self.newm = self.m - self.m2
        self.newb = self.b - self.b2
        return LinearEquation(self.newm,self.newb)

    #calculates composition of two Linear Equations 
    def compose(self,equation):
        self.m2 = equation.m
        self.b2 = equation.b
        self.newm = self.m*self.m2
        self.newb = (self.m*self.b2)+self.b
        return LinearEquation(self.newm,self.newb) 

    #evaluates the LinearEquation given variable x
    def evaluate(self,x):
        self.x = x
        self.value = (self.m*self.x) + self.b
        return self.value

#main function outputs several instances of the class and methods in LinearEquation above
def main():
    
   f = LinearEquation(5,3)
   print("f(x) =",f.showEq())
   print("f(3) =",f.evaluate(3),"\n")
         
   g = LinearEquation(-2,-6)
   print("g(x) =",g.showEq())
   print("g(-2) =",g.evaluate(-2),"\n")

   h = f.add(g)
   print("h(x) = f(x) + g(x) =",h.showEq())
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f.sub(g)
   print("j(x) = f(x) - g(x) =",j.showEq())
   print("j(-4) =",j.evaluate(-4),"\n")

   k = f.compose(g)
   print("f(g(x)) =",k.showEq(),"\n")
   
   m = g.compose(f)
   print("g(f(x)) =",m.showEq(),"\n")

   g = LinearEquation(5,-3)
   print("g(x) =",g.showEq())
   print("g(-2) =",g.evaluate(-2),"\n")
   
   h = f.add(g)
   print("h(x) = f(x) + g(x) =",h.showEq())
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f.sub(g)
   print("j(x) = f(x) - g(x) =",j.showEq())
   print("j(-4) =",j.evaluate(-4),"\n")

main()
