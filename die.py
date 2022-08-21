import numpy as np
import random


class Die:

    def __init__(self,sides):
        self.sides=sides

    def roll(self):
        return random.randint(1,self.sides)

class Yahtzee:

    def __init__(self,num_sides,num_dice):
        self.num_sides=num_sides
        self.dice=np.zeros(num_dice)

    def roll_dice(self):
        for die in range(len(self.dice)):
            self.dice[die]=Die(self.num_sides).roll()
        print(self.dice)
            
    
    def is_yahtzee(self):
        num=self.dice[0]
        count=0
        for die in self.dice:
            if die==num:
                count+=1
        if count==5:
            return True
        else:
            return False

def main(n):
    
            #play Yahtzee
    game=Yahtzee(6,5)
    yahtzee=0

    for i in range(n):
        game.roll_dice()
        if game.is_yahtzee()==True:
            yahtzee+=1
    print("got a yahtzee",yahtzee,"times")
    
##    die1=Die(6)
##
##    count=0
##    for i in range(n):
##        if die1.roll()==6:
##            count+=1
##
##    print("rolled a 6 "+str(count)+" times out of "+str(n)+" rolls")
##    print("The odds of getting a 6 was",count/n)

####################################
##    die1=Die(6)
##    die2=Die(6)
##
    
##    outcomes1=np.zeros(6)
##    outcomes2=np.zeros(6)
##    for i in range(n):
##        roll1=die1.roll()
##        roll2=die2.roll() 
##        outcomes1[roll1-1]+=1
##        outcomes2[roll2-1]+=1
##        
##    print("Outcomes for die 1:",outcomes1)
##    print("Outcomes for die 2:",outcomes2)
##
##    print(outcomes1+outcomes2)

    ####################################

    

if __name__=="__main__":
    main(1000)
