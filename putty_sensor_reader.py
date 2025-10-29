import pandas as pd
import os

target_path = r"C:/cooling tests/excel_refinary"
os.chdir(target_path)
print('Current working direcory is: '+ os.getcwd())

# Load and parse the data with correct encoding
with open("peltier_clamped_yellow_heatsink_3.txt", "r", encoding="utf-8", errors="ignore") as file:
    lines = file.readlines()[1:]  # Skip the first row

# Prepare structured data
data = []
for i, line in enumerate(lines):
    parts = line.strip().split("\t")
    if len(parts) == 3:
        try:
            s1 = parts[0].split(":")[0].strip()
            v1 = float(parts[0].split(":")[1].replace("°C", "").replace("Â", "").strip())
            s2 = parts[1].split(":")[0].strip()
            v2 = float(parts[1].split(":")[1].replace("°C", "").replace("Â", "").strip())
            s3 = parts[2].split(":")[0].strip()
            v3 = float(parts[2].split(":")[1].replace("°C", "").replace("Â", "").strip())
            time = round(i * 1.2, 2)
            data.append([s1, v1, s2, v2, s3, v3, time])
        except ValueError:
            continue  # Skip malformed lines

# Create DataFrame
df = pd.DataFrame(data, columns=["Sensor1", "Value1", "Sensor2", "Value2", "Sensor3", "Value3", "Time (s)"])

# Export to Excel
df.to_excel("sensor_data_output.xlsx", index=False)