
from datetime import datetime
import matplotlib.pylab as plt
import numpy as np


# Leser inn UIS filen

file1_path= "/Users/murvaridkhire/Documents/Ingeniør/DAT120/gruppeprosjekter/GitHub/gruppeoppgave-/trykk_og_temperaturlogg_rune_time.csv.txt"

#Lage lister 
temperatur_uis = []
tidspunkt_uis = []
trykk_absolutt_uis = []
trykk_barometrisk_uis = []
tid_barometrisk_uis = []


fil_uis = open(file1_path, 'r')
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

# Leser inn SOLA filen

file2_path = "/Users/murvaridkhire/Documents/Ingeniør/DAT120/gruppeprosjekter/GitHub/gruppeoppgave-/temperatur_trykk_met_samme_rune_time_datasett.csv.txt"


#Lage lister
temperatur_sola = []
tidspunkt_sola = []
trykk_absolutt_sola = []

fil_met = open(file2_path, 'r')

for linje in fil_met:
    if linje[0] == "S":
        data = linje.strip().split(";")                     # samme som på uis fil 
        data[2] = datetime.strptime(data[2], "%d.%m.%Y %H:%M")
        tidspunkt_sola.append(data[2])
        temperatur_sola.append(float(data[3].replace(",", ".")))
        trykk_absolutt_sola.append(float(data[4].replace(",", ".")))
   


#oppgave a)
#temp fall uis
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

#temp fall Sola

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


#oppgave c)
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

plt.subplot(2,1,1)
plt.plot(x_liste, y_liste, linestyle = "-", color = "skyblue", label="UIS temp fall")
plt.plot(x_liste_sola, y_liste_sola, linestyle = "-", color = "purple", label="SOLA temp fall")
plt.xlabel("Tid")
plt.ylabel("Temperatur")
plt.title("Temperaturfall")
plt.legend()
plt.subplot(2,1,2)
#plt.plot(tid_barometrisk_uis, differanse, label="Differansen")   trenger vi dette?
plt.plot(gyldige_tidspunkter, gjennomsnittsverdiene, linestyle = "-", color = "pink", label="Gjennomsnitt/Differanse")
plt.xlabel("Tid")
plt.ylabel("Temperatur")
plt.title("Sammenlinging mellom absolutt og barometrisk trykk")
plt.legend()
plt.tight_layout()
plt.show()


#oppgave b)
plt.hist(temperatur_uis, bins=range(int(min(temperatur_uis)), int(max(temperatur_uis)) + 1), alpha=0.3, label='Fil UIS')
plt.hist(temperatur_sola, bins=range(int(min(temperatur_sola)), int(max(temperatur_sola)) + 1), alpha=1, label='Fil SOLA')
plt.xlabel('Temperatur (°C)')
plt.ylabel('Frekvens')
plt.legend()
plt.tight_layout
plt.show()


#oppgave d) 
file3_path = "/Users/murvaridkhire/Documents/Ingeniør/DAT120/ovingsoppgaver/oving_10/temperatur_trykk_sauda_sinnes_samme_tidsperiode 2.csv.txt"
temperatur_sirdal = []
tid_sirdal = []

with open(file3_path, 'r') as file:
    for line in file:
        data = line.strip().split(";")
        if data[0] == "Sirdal - Sinnes": 
            if len(data[2]) == 16:
                data[2] = datetime.strptime(data[2], "%d.%m.%Y %H:%M")
                temperatur_sirdal.append(float(data[3].replace(",", ".")))
                tid_sirdal.append(data[2])

        
temperatur_sauda = []
tid_sauda = []

with open(file3_path, 'r') as file:
    for line in file:
        data = line.strip().split(";")
        if data[0] == "Sauda": 
            if len(data[2]) == 16:
                data[2] = datetime.strptime(data[2], "%d.%m.%Y %H:%M")
                temperatur_sauda.append(float(data[3].replace(",", ".")))
                tid_sauda.append(data[2])
                
gyldige_tidspunkter_uis, gjennomsnittsverdiene_uis = gjennomsnitt(tidspunkt_uis, temperatur_uis, 30)

plt.plot(tid_sauda, temperatur_sauda, linestyle ="-", color = "blue", label = "Temp Sauda")
plt.plot(tidspunkt_sola, temperatur_sola, linestyle ="-", color = "brown", label = "Temp Sola")
plt.plot(tid_sirdal, temperatur_sirdal, linestyle ="-", color = "green", label = "Temp sirdal")
plt.plot(gyldige_tidspunkter_uis, gjennomsnittsverdiene_uis, linestyle="-", color="orange", label="Glattete Temp UIS")
plt.title("Temperatur av ulike plasser")
plt.xlabel("Tid")
plt.ylabel("Temperatur")
plt.legend()
plt.tight_layout()
plt.show()


#oppgave e)

# Finne felles tidspunkter og beregne forskjeller
common_times = set(tidspunkt_sola)
# print(f"Lengde på mengde 1: {len(common_times)}")
times2 = set(tidspunkt_uis)
# print(f"Lengde på mengde 2: {len(times2)}")

common_times = common_times.intersection(set(tidspunkt_uis))
print(f"Antall felles tidspunkter: {len(common_times)}")
common_times = list(common_times)
common_times.sort()


temp_diffs = []
pressure_diffs = []

for time in common_times:
    temp1 = temperatur_sola[tidspunkt_sola.index(time)]
    temp2 = temperatur_uis[tidspunkt_uis.index(time)]
    pressure1 = trykk_absolutt_sola[tidspunkt_sola.index(time)]
    pressure2 = trykk_absolutt_uis[tidspunkt_uis.index(time)]
    
    temp_diffs.append(abs(temp1 - temp2))
    pressure_diffs.append(abs(pressure1 - pressure2))


# Beregne gjennomsnittlige forskjeller
snitt_temp_diff = sum(temp_diffs) / len(temp_diffs)
snitt_pressure_diff = sum(pressure_diffs) / len(pressure_diffs)

# Finne tidspunkter med lavest og høyest forskjeller
min_temp_diff_time = list(common_times)[temp_diffs.index(min(temp_diffs))]
max_temp_diff_time = list(common_times)[temp_diffs.index(max(temp_diffs))]
min_pressure_diff_time = list(common_times)[pressure_diffs.index(min(pressure_diffs))]
max_pressure_diff_time = list(common_times)[pressure_diffs.index(max(pressure_diffs))]

print(f"Gjennomsnittlig temperaturforskjell: {snitt_temp_diff}")
print(f"Gjennomsnittlig trykkforskjell: {snitt_pressure_diff}")
print(f"Tidspunkt med lavest temperaturforskjell: {min_temp_diff_time}")
print(f"Tidspunkt med høyest temperaturforskjell: {max_temp_diff_time}")
print(f"Tidspunkt med lavest trykkforskjell: {min_pressure_diff_time}")
print(f"Tidspunkt med høyest trykkforskjell: {max_pressure_diff_time}")


#oppgave f)

# Beregne gjennomsnitt og standardavvik
n = len(temperatur_sola)
std_devs = np.std(temperatur_sola, ddof=1)

# Plotting av temperaturer med standardavvik
plt.errorbar(tidspunkt_sola, temperatur_sola, yerr=std_devs, errorevery=30, capsize=5, label='Temp SOLA')
plt.xlabel('Tid')
plt.ylabel('Temperatur (°C)')
plt.title('Temperatur med standardavvik')
plt.legend()
plt.show()


