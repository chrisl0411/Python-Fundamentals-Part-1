import random

class Die():
    
    def __init__(self,sides):
        self.sides = sides

    def roll(self):
        return random.randint(1,self.sides)

def main():
    red = Die(6)
    blue = Die(10)

main()
