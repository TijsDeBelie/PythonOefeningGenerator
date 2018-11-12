
try:
        import random
        import createHTML
        import operator
        from functools import reduce
except ImportError:
        print("\nEen import error zorgde ervoor dat het programma niet kan starten!\n")

#Hoeveel getallen er minstens in 1 oefening moeten staan
MinNumber = 2
#Hoeveel getallen er maximum in 1 oefening mogen staan
MaxNumber = 4



try:
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
def makearray(number, bewerking, gate):
        array = list()
        total = 0
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
                


#Mogelijke bewerkingen (beperkt tot + en -)
bewerkingen = ["+", "-"]
#Mogelijke Gates, (Beperkt tot AND, OR, XOR)
gates = ["AND", "OR", "XOR"]




#Start van het programma, het aantal oefeningen dat gegenereerd moet worden, moet opgegeven worden bij het opstarten
for x in range(AmountOfExcercises):
        print("-------------------")
        print("oefening " + str(x +1 ))
        bewerking = bewerkingen[random.randint(0,len(bewerkingen)-1)]
        gate = gates[random.randint(0,len(gates)-1)]
        makearray(random.randint(MinNumber,MaxNumber),bewerking, gate)
createHTML.main(createHTML.globalmessage)
