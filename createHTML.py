import webbrowser
globalmessage = ""

#Bepalen wat het ingevoerde cijfer nu is, belangrijk om de base waarde eronder te zetten
def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False


def is_oct(s):
    try:
       int(s, 8)
       return True
    except ValueError:
        return False

def whatis(input):
    if type(input) is int:
        #base 10 - integer
        return "(10)"
    elif is_oct(input):
        #base 8 - octaal
        return "(8)"
    elif is_hex(input):
        #base 16 - hexadecimaal
         return "(16)"
   

""" elif type(input) is bin:
        #base 2
        return "(2)" """

#Om de html te maken en samen te voegen, gebruikt bovenstaande functies om inhoud in te vullen
def html(array, bewerking, gate):
    global globalmessage
    message = ""
    for x in range(len(array[0])):
        if(x == 0 or x == len(array[0])):
            #first or last
            message += "<li class='number'>( %s )</li><li><p><sub class ='base'>%s</sub></p></li>" % (
            array[0][x], whatis(array[0][x]))
        elif(x % 2 == 0):
            #middelste getallen
            message += "<li class='gate'>%s</li><li class='number'>( %s )</li><li><p><sub class ='base'>%s</sub></p></li>" % (
            gate, array[0][x], whatis(array[0][x]))
        else:
            #middelste getallen
            message += "<li class='bewerking'>%s</li><li class='number'>( %s )</li><li><p><sub class ='base'>%s</sub></p></li>" % (
            bewerking, array[0][x], whatis(array[0][x]))
    globalmessage += "<ul id='row'>%s<li>= ____________</li><sub class='base'>(10)</sub><li class='total'>%d<sub class='basetotal'>(10)</sub></li></ul>" %(message, array[1])

#Gaat headers toevoegen aan de html en wanneer gedaan het bestand ook openen
def main(message):
    f = open('oefening.html', 'w')
    header = "<html><head><link rel='stylesheet' type='text/css' href='mystyle.css'></head><body>"
    footer = "</body></html>"
    f.write(str(header + message + footer))
    f.close()

    webbrowser.open_new_tab('oefening.html')
