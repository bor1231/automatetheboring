import openpyxl
import pandas as pd
import matplotlib.pyplot as plt
import os

target_path = r"C:/cooling tests/excel_refinary"
os.chdir(target_path)
print('Current working direcory is: '+ os.getcwd())

# Step 1: Rename the sheet using openpyxl
wb = openpyxl.load_workbook('sensor_data_output.xlsx')
sheet = wb.active
sheet.title = 'SensorData'
wb.save('sensor_data_output.xlsx')

# Step 2: Load data using pandas
df = pd.read_excel('sensor_data_output.xlsx', sheet_name='SensorData')

# Step 3: Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df["Time (s)"], df["Value1"], label="Cold Side", color="blue")
plt.plot(df["Time (s)"], df["Value2"], label="Environment", color="green")
plt.plot(df["Time (s)"], df["Value3"], label="Hot Side", color="red")

plt.title("Yellow_HS_with room AC_ON")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()