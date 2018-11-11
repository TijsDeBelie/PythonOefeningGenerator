import webbrowser
globalmessage = ""

#Bepalen wat het ingevoerde cijfer nu is, belangrijk om die base eronder te zetten


def whatis(input):
    if type(input) is int:
        #base 8 ??
        return "(int)"
    elif input[:2] == "0x" or input[:3] == "-0x":
        #base 16
         return "(hex)"
    else:
        #base 2
        return "(binair)"



#Om de html te maken en samen te voegen, gebruikt bovenstaande functies om inhoud in te vullen
def html(array, bewerking, gate):
    global globalmessage
    message = ""
    print("Bewerking " + bewerking)
    for x in range(len(array[0])):
        if(x == 0 or x == len(array[0])):
            #print("first or last")
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
    globalmessage += "<ul id='row'>%s<li>= ____________</li><li class='total'>%d</li></ul>" %(message, array[1])
    print (array)

#Gaat headers toevoegen aan de html en wanneer gedaan het bestand ook openen
def main(message):
    f = open('oefening.html', 'w')
    header = "<html><head><link rel='stylesheet' type='text/css' href='mystyle.css'></head><body>"
    footer = "</body></html>"
    f.write(str(header + message + footer))
    f.close()

    webbrowser.open_new_tab('oefening.html')
