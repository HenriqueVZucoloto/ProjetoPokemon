while True:
    #Schüler1
    while True:
        Schüler1 = input("Ist Schüler1 da?")
        if Schüler1 == 'Stop':
            break
        elif Schüler1 == 'Ja':
            s1 = 1
        elif Schüler1 == 'Nein':
            s1 = 0
        else:
            print("Bitte Ja, Nein oder Stop eingeben!")

        Schüler2 = input("Ist Schüler2 da?")
        if Schüler2 == 'Stop':
            print("Programm wird beendet...")
            break
        elif Schüler2 == 'Ja':
            s2 = 1
        elif Schüler2 == 'Nein':
            s2 = 0
        else:
            print("Bitte Ja, Nein oder Stop eingeben!")
    #Ausgabe
    #Kein Schüler
        if s1 + s2 == 0:
            print ("Es sind heute keine Schüler anwesend.")
        #1 Schüler
        elif s1 + s2 == 1:
            print ("Es ist heute ein Schüler anwesend.")

        #Mehr als 1 Schüler
        elif s1 + s2 > 1:
            print ("Es sind heute " + str(s1) + str(s2) + " Schüler anwesend.")