from datetime import datetime
import matplotlib.pyplot as plt

file_path = "C:/Users/uchen/Downloads/temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv.txt"
temperature_sirdal = []
timestamp_sirdal = []

with open(file_path, 'r') as file:
    for line in file:
        data = line.strip().split(";")
        if data[0] == "Sirdal - Sinnes": 
            if len(data[2]) == 16:
                data[2] = datetime.strptime(data[2], "%d.%m.%Y %H:%M")
                temperature_sirdal.append(float(data[3].replace(",", ".")))
                timestamp_sirdal.append(data[2])


        
        
temperature_sauda = []
timestamp_sauda = []

with open(file_path, 'r') as file:
    for line in file:
        data = line.strip().split(";")
        if data[0] == "Sauda": 
            if len(data[2]) == 16:
                data[2] = datetime.strptime(data[2], "%d.%m.%Y %H:%M")
                temperature_sauda.append(float(data[3].replace(",", ".")))
                timestamp_sauda.append(data[2])
                
                






from datetime import datetime
file_path = "C:/Users/uchen/Downloads/temperatur_trykk_met_samme_rune_time_datasett.csv.txt"

temperatur_sola = []
tidspunkt_sola = []

file = open(file_path, 'r')
for line in file:
    if line[0] == "S":
        data = line.strip().split(";")
        data[2] = datetime.strptime(data[2], "%d.%m.%Y %H:%M")
        
        temperatur_sola.append(data[3])
        tidspunkt_sola.append(data[2])



plt.plot(timestamp_sauda, temperature_sauda, linestyle ="-", color = "skyblue", label = "Temp Sauda")
plt.plot(tidspunkt_sola, temperatur_sola)
plt.plot(timestamp_sirdal, temperature_sirdal)
plt.show()


