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

#Om de html te maken en samen te voegen, gebruikt bovenstaande functies om inhoud in te vullen
def html(array):
    global globalmessage
    message = ""
    if (len(array[0]) == 2):
        message += "<li class='number'>%s</li><li><p><sub class ='base'>%s</sub></p></li>" %(array[0][0], array[3][0])
        message += "<li class='bewerking'>%s</li>" %(array[2][0])
        message += "<li class='number'>%s</li><li><p><sub class ='base'>%s</sub></p></li>" %(array[0][1], array[3][1])
    elif (len(array[0]) == 3):
        message += "<li class='number'>(%s</li><li><p><sub class ='base'>%s</sub></p></li>" %(array[0][0], array[3][0])
        message += "<li class='bewerking'>%s</li>" % (array[2][0])
        message += "<li class='number'>%s</li><li><p><sub class ='base'>%s</sub></p></li><li class='number'>)</li>" %(array[0][1], array[3][1])
        message += "<li class='bewerking'>%s</li>" %(array[2][1])
        message += "<li class='number'>%s</li><li><p><sub class ='base'>%s</sub></p></li>" %(array[0][2], array[3][2])
    elif (len(array[0]) == 4):
        message += "<li class='number'>(%s</li><li><p><sub class ='base'>%s</sub></p></li>" %(array[0][0], array[3][0])
        message += "<li class='bewerking'>%s</li>" %(array[2][0])
        message += "<li class='number'>%s</li><li><p><sub class ='base'>%s</sub></p></li><li class='number'>)</li>" %(array[0][1], array[3][1])
        message += "<li class='bewerking'>%s</li>" %(array[2][1])
        message += "<li class='number'>(%s</li><li><p><sub class ='base'>%s</sub></p></li>" %(array[0][2], array[3][2])
        message += "<li class='bewerking'>%s</li>" %(array[2][2])
        message += "<li class='number'>%s</li><li><p><sub class ='base'>%s</sub></p></li><li class='number'>)</li>" %(array[0][3], array[3][3])
    globalmessage += "<ul id='row'>%s<li>= ____________</li><p><sub class='base'>(10)</sub><p><li class='total'>%d<sub class='basetotal'>(10)</sub></li></ul>" %(message, array[1])

#Gaat headers toevoegen aan de html en wanneer gedaan het bestand ook openen
def main(message):
    f = open('oefening.html', 'w')
    header = "<html><head><link rel='stylesheet' type='text/css' href='mystyle.css'></head><body><h1>OefeningGenerator voor rekenen met hexadecimale, octale en decimale getallen.<br></h1>"
    footer = "</body></html>"
    f.write(str(header + message + footer))
    f.close()

    webbrowser.open_new_tab('oefening.html')
