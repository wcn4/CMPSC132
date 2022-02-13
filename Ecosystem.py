#This program was written by Bill Neubauer
import random

def main():
    #Generate a river
    Snohomish = Ecosystem()
    #Insert the animals
    Fish(Snohomish)
    Fish(Snohomish)
    Fish(Snohomish)
    Bear(Snohomish)
    Bear(Snohomish)

    print(Snohomish)
    for x in range(0, 20):
        Snohomish.GenerateMoves()
        print(Snohomish)

class Ecosystem:
    

    def __init__(self):
        self.river = []
        for i in range(10):
            self.river.append(None)
        

    #Sequentially generate moves for each animal
    def GenerateMoves(self):
        i = 0
        while( i < len(self.river) ):
            x = 0
            if not self.river[i] == None:
                x = self.river[i].Move()
            if x == 1:
                i += 1
            i += 1
            
    
    #Can set rules of where next new valid index would be 
    def ValidRandomIndex(self):
        newIndex = random.randint(0, len(self.river)-1)
        while not self.river[newIndex] == None:
            newIndex = random.randint(0, len(self.river)-1)
        return newIndex

    def __str__(self):
        string = "[ " 
        for animal in self.river:
            string = string + " " + str(animal) + ", " 
        return string + " ]"



class Fish:
    #Will be born in at a random point in the river where space allows
    def __init__(self, ecosystem):
        self.ecosystem = ecosystem
        self.lastIndex = -1
        self.index = ecosystem.ValidRandomIndex()
        self.ecosystem.river[self.index] = self
    
    #Will have three scenarios:
    #   It will move and will have no collisions.
    #   It will move and there will be a collision.
    #       It will collide into the same type
    #           Will tell other fish to move back to where they were
    #           Will not move, will birth a new fish.
    #       It will collide into other type
    #Returns how much it moved by
    def Move(self):
        newIndex = self.index + random.randint(-1,1)
        #If fish goes out of bounds
        if newIndex < 0 or newIndex > len(self.ecosystem.river):
            print("\t[Fish] Went out of bounds, did not move")
            lastIndex = self.index
            return 0
        
        if self.ecosystem.river[newIndex] == None or self.index == newIndex:
            print("\t[Fish] Moving from " + str(self.index) +" to " + str(newIndex)) 
            self.ecosystem.river[self.index] = None
            self.lastIndex = self.index
            self.index = newIndex
            self.ecosystem.river[newIndex] = self
             
            return (self.index - self.lastIndex)
         
        if str(self.ecosystem.river[newIndex]) == "Fish":
            print("\t[Fish to Fish]: Collided with " + str(self.index) + " and " + str(newIndex))
            self.ecosystem.river[newIndex].GoBack()
            lastIndex = self.index
            Fish(self.ecosystem)
            return 0

        if str(self.ecosystem.river[newIndex]) == "Bear":
            print("\t[Fish to Bear]: Collided with " + str(self.index) + " and " + str(newIndex))
            self.Kill()
            return

            

        
    

    #Will go back to it's last index
    def GoBack(self):
        self.ecosystem.river[self.index] = None
        self.ecosystem.river[self.lastIndex] = self
        self.index = self.lastIndex
        return

    #Fish will die
    def Kill(self):
        self.ecosystem.river[self.index] = None
        self = None
        return

    def __str__(self):
        return "Fish"

class Bear:

    #Will be born in at a random point in the river where space allows
    def __init__(self, ecosystem):
        self.ecosystem = ecosystem
        self.lastIndex = -1
        self.index = ecosystem.ValidRandomIndex()
        self.ecosystem.river[self.index] = self
    
    #Will have three scenarios:
    #   It will move and will have no collisions.
    #   It will move and there will be a collision.
    #       It will collide into the same type
    #           Will tell other bear to move back to where they were
    #           Will not move, will birth a new bear.
    #       It will collide into other type
    #Returns how much it moved by
    def Move(self):
        newIndex = self.index + random.randint(-1,1)
        #If fish goes out of bounds
        if newIndex < 0 or newIndex > len(self.ecosystem.river):
            print("\t[Bear] Went out of bounds, did not move")
            lastIndex = self.index
            return 0
        
        if self.ecosystem.river[newIndex] == None or self.index == newIndex:
            print("\t[Bear] Moving from " + str(self.index) +" to " + str(newIndex)) 
            self.ecosystem.river[self.index] = None
            self.lastIndex = self.index
            self.index = newIndex
            self.ecosystem.river[newIndex] = self
             
            return (self.index - self.lastIndex)
         
        if str(self.ecosystem.river[newIndex]) == "Bear":
            print("\t[Bear to Bear]: Collided with " + str(self.index) + " and " + str(newIndex))
            self.ecosystem.river[newIndex].GoBack()
            self.lastIndex = self.index
            Fish(self.ecosystem)
            return 0

        if str(self.ecosystem.river[newIndex]) == "Fish":
            print("\t[Bear to Fish]: Collided with " + str(self.index) + " and " + str(newIndex))
            self.ecosystem.river[newIndex].Kill()
            self.lastIndex = self.index
            self.index = newIndex
            self.ecosystem.river[self.index] = self
            return (self.index - self.lastIndex)

            

        
    

    #Will go back to it's last index
    def GoBack(self):
        self.ecosystem.river[self.index] = None
        self.ecosystem.river[self.lastIndex] = self
        self.index = self.lastIndex
        return


    def __str__(self):
        return "Bear"

main()
