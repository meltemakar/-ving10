#oppgave a)
from datetime import datetime
import matplotlib.pylab as plt

# Leser inn UIS filen

file_path= "trykk_og_temperaturlogg_rune_time.csv.txt"

#Lage lister for temp, tid, trykk og baro_trykk for UIS
temperatur_uis = []
tidspunkt_uis = []
trykk_absolutt_uis = []
trykk_barometrisk_uis = []
tid_barometrisk_uis = []


fil_uis = open(file_path, 'r')
for linje in fil_uis:
    if linje[0] != "D" :
        data = linje.strip().split(";")         #deler strengen i biter/ indeks for å kunne lage lister med hver av bitenene 
        if len(data[0]) == 16:        
            data[0] = datetime.strptime(data[0], "%m.%d.%Y %H:%M") 
            tidspunkt_uis.append(data[0])
            temperatur_uis.append(float(data[4].replace(",", ".")))         #lager linja til float slik at den kan lageres i liste 
            trykk_desimal = float(data[3].replace(",", "."))
            trykk_absolutt_uis.append(trykk_desimal * 10)                     #fra bar til hpa 

            if data[2] == "":                                                   #lager liste for bar. trykk 
                continue                                                         # må ha samme mengde x, y verdier så vi må lag eny liste med tidspunkt                                              
            else:
                trykk_bar_desimal = float(data[2].replace(",", "."))
                trykk_barometrisk_uis.append(trykk_bar_desimal * 10)
                tid_barometrisk_uis.append(data[0])

        else:
            data[0] = data[0].replace("00:", "12:")                  # filå endre stil halveis gjømnom så vi å tilpasse for den delen av filå
            data[0] = datetime.strptime(data[0], "%m/%d/%Y %I:%M:%S %p") 
            tidspunkt_uis.append(data[0])
            temperatur_uis.append(float(data[4].replace(",", ".")))
            trykk_desimal = float(data[3].replace(",", "."))
            trykk_absolutt_uis.append(trykk_desimal * 10)
            if data[2] == "":
                continue
            else:
                trykk_bar_desimal = float(data[2].replace(",", "."))
                trykk_barometrisk_uis.append(trykk_bar_desimal * 10)
                tid_barometrisk_uis.append(data[0])


#temp.fall uis
natt12_temp = temperatur_uis[1128:4575]    #slice temp_uis og tid_uis lista til det vi trenger 
natt12_tid = tidspunkt_uis[1128:4575]      # for å lage plot for temp natt 12 

temp_høyest_natt = max(natt12_temp)
natt12_temp.index(temp_høyest_natt)       # finner index for å finne tiden
                                            

punkt_1_x = natt12_tid[2]  
punkt_1_y = temp_høyest_natt

temp_lavest_natt = min(natt12_temp)
natt12_temp.index(temp_lavest_natt)

punkt_2_x = natt12_tid[3442]
punkt_2_y = temp_lavest_natt

x_liste = []                        #lagde liste for x min/max og y min/max for plotten 
x_liste.append(punkt_1_x)
x_liste.append(punkt_2_x)

y_liste = []
y_liste.append(punkt_1_y)
y_liste.append(punkt_2_y)




# Leser inn SOLA filen

file_path = "temperatur_trykk_met_samme_rune_time_datasett.csv.txt"


#Lage lister for temp, tid, trykk for SOLA
temperatur_sola = []
tidspunkt_sola = []
trykk_absolutt_sola = []



fil_met = open(file_path, 'r')

for linje in fil_met:
    if linje[0] == "S":
        data = linje.strip().split(";")                     # samme som på uis fil 
        data[2] = datetime.strptime(data[2], "%d.%m.%Y %H:%M")
        tidspunkt_sola.append(data[2])
        temperatur_sola.append(float(data[3].replace(",", ".")))
        trykk_absolutt_sola.append(float(data[4].replace(",", ".")))
   

file_path = "temperatur_trykk_met_samme_rune_time_datasett.csv.txt"


#Lage lister for temp, tid, trykk for SOLA
temperatur_sola = []
tidspunkt_sola = []
trykk_absolutt_sola = []

fil_met = open(file_path, 'r')

for linje in fil_met:
    if linje[0] == "S":
        data = linje.strip().split(";")                     # samme som på uis fil 
        data[2] = datetime.strptime(data[2], "%d.%m.%Y %H:%M")
        tidspunkt_sola.append(data[2])
        temperatur_sola.append(float(data[3].replace(",", ".")))
        trykk_absolutt_sola.append(float(data[4].replace(",", ".")))
   
#a)
natt12_temp_sola = temperatur_sola[17:27]    #slice temp_uis og tid_uis lista til det vi trenger 
natt12_tid_sola = tidspunkt_sola[17:27]      # for å lage plot for temp natt 12 

temp_høyest_natt_sola = max(natt12_temp_sola)
natt12_temp_sola.index(temp_høyest_natt_sola)       # finner index for å finne tiden                                   


punkt_1_x_sola = natt12_tid_sola[0]  
punkt_1_y_sola = temp_høyest_natt_sola

temp_lavest_natt_sola = min(natt12_temp_sola)
natt12_temp_sola.index(temp_lavest_natt_sola)


punkt_2_x_sola = natt12_tid_sola[9]
punkt_2_y_sola = temp_lavest_natt_sola

x_liste_sola = []                        #lagde liste for x min/max og y min/max for plotten 
x_liste_sola.append(punkt_1_x_sola)
x_liste_sola.append(punkt_2_x_sola)

y_liste_sola = []
y_liste_sola.append(punkt_1_y_sola)
y_liste_sola.append(punkt_2_y_sola)

#b)






#c)
differanse = []
for i in range(len(trykk_barometrisk_uis)):
    differanse.append(trykk_absolutt_uis[i] - trykk_barometrisk_uis[i])

def gjennomsnitt(tid, differanse, n):
    gyldige_tidspunkter = []
    gjennomsnittsverdiene = []

    for i in range(n, (len(differanse)-n)):                                 # lengden temp - 30 da får vi de linjene 30 nedefra og 30 overfra 
        gyldige_tidspunkter.append(tid[i])                                  #setter inn i gyd.tid verdier 
        n_forrige_neste = differanse[i-n:i+(n+1)]                           #finner indeksenne som passer til n-verdien  for temperatur 
        gjennomsnittsverdiene.append((sum(n_forrige_neste)) / ((2*n)+1))    # finner gjennomsnittet 

    return gyldige_tidspunkter, gjennomsnittsverdiene

gyldige_tidspunkter, gjennomsnittsverdiene = gjennomsnitt(tidspunkt_uis, differanse, 10) 




#d) 





#e)






#f)








plt.subplot(2,1,1)
plt.plot(x_liste, y_liste, linestyle = "-", color = "skyblue")
plt.plot(x_liste_sola, y_liste_sola, linestyle = "-", color = "purple")
plt.xlabel("tid")
plt.ylabel("temperatur")
plt.title("temperaturfall")
plt.subplot(2,1,2)
plt.plot(gyldige_tidspunkter, gjennomsnittsverdiene, linestyle = "-", color = "pink")
plt.xlabel("tid")
plt.ylabel("differanse")
plt.title("differansen mellom absolutt og barometrisk trykk")
plt.show()
