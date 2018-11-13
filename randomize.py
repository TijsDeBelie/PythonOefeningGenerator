# GERT VAN DER BREMPT
# MARGO ANCKAERT
# TIJS DE BELIE
try:
        import random
        import createHTML
        import operator
        from functools import reduce
        import time

except ImportError:
        print("\nEen import error zorgde ervoor dat het programma niet kan starten!\n")



#Hoeveel getallen er minstens in 1 oefening moeten staan
MinNumber = 2
#Hoeveel getallen er maximum in 1 oefening mogen staan
MaxNumber = 4

start = time.time()

try:
        print("DIT PROGRAMMA WERD GEMAAKT DOOR GERT VAN DER BREMPT, MARGO ANCKAERT EN TIJS DE BELIE")
        AmountOfExcercises = int(input('\n\n\n\n\n\nHoeveel oefeningen moeten er gemaakt worden?\n\n\n\n\n\n')) 
except: 
        print("\nGelieve een geldig getal op te geven, de standaard waarde is 10\n")
        AmountOfExcercises = 10

def randomnumber(min, max):
        return (random.randint(min, max))



#functie om getallen om te zetten naar binaire vorm
#NIET GEBRUIKT MOMENTEEL
ToBin = lambda x, count=8: "".join(map(lambda y:str((x>>y)&1), range(count-1, -1, -1)))

def tweeComplement(nummer):
        if (nummer < 0):
                nummer = (~nummer) ^ 1 * 0x3FF
        return nummer

#Converteert het opgegeven nummer in octale notatie
def convertOctaal(nummer):
        return "{0:o}".format(tweeComplement(nummer))



#logische gates
def AND(A, B):
        return A & B
def OR(A, B):
        return A | B
def XOR(A, B):
        return A ^ B


#Maakt een array van random nummers 
def makearray(termen, bewerkingenArray):
        array = list()
        total = 0
        for x in range(termen):
                generatednumber = randomnumber(-512, 511)
                array.append(generatednumber)

        if (termen == 2):
                total = bereken(array[0], array[1], bewerkingenArray[0])
        elif (termen == 3):
                total += bereken(array[0], array[1], bewerkingenArray[0])
                total += bereken(total, array[2], bewerkingenArray[1])
        elif (termen == 4):
                bew1 = bereken(array[0], array[1], bewerkingenArray[0])
                bew2 = bereken(array[2], array[3], bewerkingenArray[2])
                total = bereken(bew1, bew2, bewerkingenArray[1])

        for x in range(len(array)):
                rand = random.randint(1,3)
                if rand == 2:
                        array[x] = convertOctaal(array[x])
                elif rand == 3:
                        array[x] = '{:x}'.format(array[x])
        #range van 10 bit signed integer is -512, 512
        #indien out of range wordt de oefening weggegooid en wordt er een nieuwe gemaakt
        if(total in range(-512,511)):
                lijst = list()
                lijst.append(array)
                lijst.append(total)
                lijst.append(bewerkingenArray)
                createHTML.html(lijst)
                
        else:
                makearray(termen ,bewerkingenArray)
                
def bereken(A, B, bew):
                if (bew == "+"):
                        return A + B
                elif (bew == "-"):
                        return A - B
                elif (bew == "AND"):
                        return AND(A, B)
                elif (bew == "OR"):
                        return OR(A, B)
                elif (bew == "XOR"):
                        return XOR(A, B)

#Mogelijke bewerkingen (beperkt tot +, -, AND, OR, XOR)
bewerkingen = ["+", "-", "AND", "OR", "XOR"]


#Start van het programma, het aantal oefeningen dat gegenereerd moet worden, moet opgegeven worden bij het opstarten

for x in range(AmountOfExcercises):
        print("-------------------")
        print("oefening " + str(x +1 ))
        aantalTermen = random.randint(MinNumber,MaxNumber)
        bewerkingArray = list()
        for x in range(aantalTermen - 1):
                bewerkingArray.append(bewerkingen[random.randint(0,len(bewerkingen)-1)])
        makearray(aantalTermen, bewerkingArray)
createHTML.main(createHTML.globalmessage)


print ('It took', time.time()-start, 'seconds.')
