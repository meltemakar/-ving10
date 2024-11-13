import datetime

def read_data(file_path, delimiter=';'):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines[1:]:  # overksriften!!!!!!!
            columns = line.strip().split(delimiter)
            data.append(columns)
    return data

file1_path = 'øving6/temperatur_trykk_met_samme_rune_time_datasett.csv.txt'
file2_path = 'øving6/trykk_og_temperaturlogg_rune_time.csv.txt'
data1 = read_data(file1_path)
data2 = read_data(file2_path)

def convert_to_datetime(date_str, time_format='%d.%m.%Y %H:%M'):
    try:
        return datetime.datetime.strptime(date_str, time_format)
    except ValueError:
        return None

# Ekstrahere relevante kolonner og konvertere til datetime
data1_times = [convert_to_datetime(row[2]) for row in data1 if convert_to_datetime(row[2])]
data1_temps = [float(row[3].replace(',', '.')) for row in data1 if row[3] and convert_to_datetime(row[2])]
data1_pressures = [float(row[4].replace(',', '.')) for row in data1 if row[4] and convert_to_datetime(row[2])]

data2_times = [convert_to_datetime(row[0], '%m.%d.%Y %H:%M') for row in data2 if row[2] and convert_to_datetime(row[0], '%m.%d.%Y %H:%M')]
data2_temps = [float(row[4].replace(',', '.')) for row in data2 if row[4] and convert_to_datetime(row[0], '%m.%d.%Y %H:%M')]
data2_pressures = [float(row[2].replace(',', '.')) for row in data2 if row[2] and convert_to_datetime(row[0], '%m.%d.%Y %H:%M')]

# Finne felles tidspunkter og beregne forskjeller
common_times = set(data1_times)
# print(f"Lengde på mengde 1: {len(common_times)}")
times2 = set(data2_times)
# print(f"Lengde på mengde 2: {len(times2)}")

common_times = common_times.intersection(set(data2_times))
print(f"Antall felles tidspunkter: {len(common_times)}")
common_times = list(common_times)
common_times.sort()

print(data1_times[0])
print(data2_times[0])
print(len(data2_times))
print(len(data2_pressures))


temp_diffs = []
pressure_diffs = []

for time in common_times:
    temp1 = data1_temps[data1_times.index(time)]
    temp2 = data2_temps[data2_times.index(time)]
    pressure1 = data1_pressures[data1_times.index(time)]
    pressure2 = data2_pressures[data2_times.index(time)]
    
    temp_diffs.append(abs(temp1 - temp2))
    pressure_diffs.append(abs(pressure1 - pressure2))

# Sjekk om listene er tomme før beregning
if temp_diffs and pressure_diffs:
    # Beregne gjennomsnittlige forskjeller
    avg_temp_diff = sum(temp_diffs) / len(temp_diffs)
    avg_pressure_diff = sum(pressure_diffs) / len(pressure_diffs)

    # Finne tidspunkter med lavest og høyest forskjeller
    min_temp_diff_time = list(common_times)[temp_diffs.index(min(temp_diffs))]
    max_temp_diff_time = list(common_times)[temp_diffs.index(max(temp_diffs))]
    min_pressure_diff_time = list(common_times)[pressure_diffs.index(min(pressure_diffs))]
    max_pressure_diff_time = list(common_times)[pressure_diffs.index(max(pressure_diffs))]

    print(f"Gjennomsnittlig temperaturforskjell: {avg_temp_diff}")
    print(f"Gjennomsnittlig trykkforskjell: {avg_pressure_diff}")
    print(f"Tidspunkt med lavest temperaturforskjell: {min_temp_diff_time}")
    print(f"Tidspunkt med høyest temperaturforskjell: {max_temp_diff_time}")
    print(f"Tidspunkt med lavest trykkforskjell: {min_pressure_diff_time}")
    print(f"Tidspunkt med høyest trykkforskjell: {max_pressure_diff_time}")
else:
    print("Ingen felles tidspunkter funnet eller ingen gyldige data for beregning.")