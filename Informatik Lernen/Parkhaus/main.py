from myClasses import *
#Generiert Parkhaus mit 10 Parkplätzen
PH = Parkhaus(10)



PH.zeige_freie_plaetze()


#Simuliert Autos
PH.einparken()
PH.einparken()
PH.einparken()

PH.zeige_freie_plaetze()

PH.ausparken(2)

PH.zeige_freie_plaetze()