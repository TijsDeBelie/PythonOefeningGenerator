import random
import createHTML



MinNumber = 2
MaxNumber = 4
AmountOfExcercises = 5

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
# 111111111 --> 512
# 110010010


# (~500)^ 0x3FF

def intToBin(n):
    nums = [n]
    while n > 1:
        n = n // 2
        nums.append(n)

    bits = []
    for i in nums:
        bits.append(str(0 if i%2 == 0 else 1))
    bits.reverse()
    return ''.join(bits)

def makearray(number, bewerking, gate):
        array = list()
        total = 0
        for x in range(number):
                print("Cijfer " + str(x + 1))
                randnumber = randomnumber(-128, 128)
                array.append(randnumber)
                if(bewerking =="+"):
                        total+=randnumber
                elif(bewerking =="-"):
                        total-=randnumber
        for x in range(len(array)):
                rand = random.randint(1,3)
                if rand == 1:
                        print("do nothing")
                elif rand == 2:
                        array[x] = intToBin(array[x])
                elif rand == 3:
                        array[x] = hex(array[x])
        print(array)
        
        if(total in range(-128,128)):
                lijst = list()
                lijst.append(array)
                lijst.append(total)
                lijst.append(gate)
                createHTML.html(lijst, bewerking, gate)
                
        else:
                makearray(random.randint(MinNumber,MaxNumber),bewerking, gate)
                


bewerkingen = ["+", "-"]
gates = ["AND", "OR", "XOR"]

for x in range(AmountOfExcercises):
        print("-------------------")
        print("oefening " + str(x))
        bewerking = bewerkingen[random.randint(0,len(bewerkingen)-1)]
        gate = gates[random.randint(0,len(gates)-1)]
        makearray(random.randint(MinNumber,MaxNumber),bewerking, gate)

createHTML.main(createHTML.globalmessage)