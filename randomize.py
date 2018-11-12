import random
import createHTML
import operator
from functools import reduce


MinNumber = 2
MaxNumber = 4
AmountOfExcercises = 10

def randomnumber(min, max):
        return (random.randint(min, max))


#Maakt een array van random nummers 
#TODO verwijder som als laatste cijfer van array, heeft implicaties in createhtml.py

# FORMAT, ENKEL VOOR POSITIEVE GETALLEN
# AND &
# OR |
# XOR ^
# NEGATIEVE GETALLEN (Beschouw het als een positief getal)
# 000101001 --> alle nullen naar 1 en 1 naar 0 --> 111010110 + 1 --> 111010111 (2 complement systeem)
# XOR is 1111111111 vergelijken (geen verschil is 0, wel verschil is 1)
# 001101101
# 111111111
# 001101101
# 
#  --> 512
# 110010010


# (~500)^ 0x3FF

ToBin = lambda x, count=8: "".join(map(lambda y:str((x>>y)&1), range(count-1, -1, -1)))


def makearray(number, bewerking, gate):
        array = list()
        total = 0
        #TODO totalen berekenen nog niet in orde
        for x in range(number):
                generatednumber = randomnumber(-512, 512)
                array.append(generatednumber)

        if(bewerking =="+"):
                total = reduce(operator.add, array)
                
        elif(bewerking =="-"):
                total = reduce(operator.sub, array)

        for x in range(len(array)):
                rand = random.randint(1,3)
                if rand == 2:
                        array[x] = convertOctaal(array[x])
                elif rand == 3:
                        array[x] = '{:x}'.format(array[x])
        
        if(total in range(-512,512)):
                lijst = list()
                lijst.append(array)
                lijst.append(total)
                lijst.append(gate)
                createHTML.html(lijst, bewerking, gate)
                
        else:
                makearray(random.randint(MinNumber,MaxNumber),bewerking, gate)
                
def tweeComplement(nummer):
        if (nummer < 0):
                nummer = (~nummer) ^ 1 * 0x3FF
        return nummer

def convertOctaal(nummer):
        return "{0:o}".format(tweeComplement(nummer))


bewerkingen = ["+", "-"]
gates = ["AND", "OR", "XOR"]

for x in range(AmountOfExcercises):
        print("-------------------")
        print("oefening " + str(x))
        bewerking = bewerkingen[random.randint(0,len(bewerkingen)-1)]
        gate = gates[random.randint(0,len(gates)-1)]
        makearray(random.randint(MinNumber,MaxNumber),bewerking, gate)
createHTML.main(createHTML.globalmessage)

#createHTML.html(([10,5,8]), "-", "AND"],"-","AND")

#wat is octaal? 10 --> 12
""" print(convertOctaal(12))



def AND(A, B):
        return A & B
def OR(A, B):
        return A | B
def XOR(A, B):
        return A ^ B

print(AND(245, 18))
print(OR(245, 18))
print(XOR(245, 18)) """