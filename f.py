import matplotlib.pyplot as plt
import numpy as np

# Funksjon for å lese temperaturdata fra fil uten å bruke csv
def read_temperatures(file_path, temp_column_index, delimiter=';'):
    temperatures = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines[1:]:  # Hopp over overskriftsraden
            columns = line.strip().split(delimiter)
            try:
                temperatures.append(float(columns[temp_column_index].replace(',', '.')))
            except ValueError:
                continue  # Hopp over rader med ugyldige data
    return temperatures

# Lese temperaturdata fra den første filen
file1_path = 'øving6/temperatur_trykk_met_samme_rune_time_datasett.csv.txt'
temps1 = read_temperatures(file1_path, 3)  # Antar at temperaturen er i den 4. kolonnen (indeks 3)

# Beregne gjennomsnitt og standardavvik
n = len(temps1)
mean_temps = np.mean(temps1)
std_devs = np.std(temps1, ddof=1)

# Funksjon for å plotte temperaturer med standardavvik
def plot_with_std_deviation(times, temps, std_devs, errorevery=30, capsize=5):
    plt.errorbar(times, temps, yerr=std_devs, errorevery=errorevery, capsize=capsize, label='Temperatur med standardavvik')
    plt.xlabel('Tid')
    plt.ylabel('Temperatur (°C)')
    plt.title('Temperatur med standardavvik')
    plt.legend()
    plt.show()

# Generere tidspunkter for x-aksen (for enkelhetens skyld bruker vi indekser som tidspunkter)
times = list(range(n))

# Plotting av temperaturer med standardavvik
plot_with_std_deviation(times, temps1, std_devs)