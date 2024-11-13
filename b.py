import matplotlib.pyplot as plt

def read_temperatures(file_path, temp_column_index, delimiter=';'):
    temperatures = []
    with open(file_path, 'r', encoding='UTF8') as file:
        lines = file.readlines()
        for line in lines[1:]:  # Hopp over overskriftsraden
            columns = line.strip().split(delimiter)
            try:
                temperatures.append(float(columns[temp_column_index].replace(',', '.')))
            except ValueError:
                continue  
    return temperatures

# Lese temperaturdata fra begge filene
file1_path = 'øving6/temperatur_trykk_met_samme_rune_time_datasett.csv.txt'
file2_path = 'øving6/trykk_og_temperaturlogg_rune_time.csv.txt'
temps1 = read_temperatures(file1_path, 3) 
temps2 = read_temperatures(file2_path, 4)  

def plot_simple_histogram(temps1, temps2):
    plt.hist(temps1, bins=range(int(min(temps1)), int(max(temps1)) + 1), alpha=0.5, label='Fil 1')
    plt.hist(temps2, bins=range(int(min(temps2)), int(max(temps2)) + 1), alpha=0.5, label='Fil 2')
    plt.xlabel('Temperatur (°C)')
    plt.ylabel('Frekvens')
    plt.legend()
    plt.show()

plot_simple_histogram(temps1, temps2)