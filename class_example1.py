# A class definition chracterizes the properties and the behaviour of a group of objects
# that are of a certain kind
import random
class Die:
    def __init__(self,number_of_sides,color):
        # initializes the instance attributes (properties) of the object
        self.sides = number_of_sides
        self.color = color
    def roll(self):
        print(self.color)
        return random.randint(1,self.sides)
def main():
    d6 = Die(6,'red') # 1. object is created 2. init method is called
    print(d6.roll())
    d8 = Die(8,'green')
    print(d8.roll())
    d12 = Die(12,'purple')
    print(d12.roll())
    
    
main()    