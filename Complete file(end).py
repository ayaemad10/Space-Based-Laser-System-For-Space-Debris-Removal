import math
import numpy as np
from datetime import datetime
from datetime import timedelta
mu = 398600

filename='C:\\Users\\Aya\\Downloads\\yota_w\\ALL -project\\TLE-sat\\sat000044415.txt'
epoch_years = []
epoch_months = []
epoch_days = []
inclinations = []
right_ascensions = []
eccentricities = []
arg_perigees = []
mean_anomalies = []
mean_motions = []
semi_major_axi=[]
Arue_Anomalys= []

# Open the file
with open(filename, 'r') as file:
    # Read the lines from the file
    lines = file.readlines()[:625]
def solve_keplers_equation(mean_anomaly_deg, eccentricity):
    # Convert mean anomaly from degrees to radians
    mean_anomaly_rad = mean_anomaly_deg
    
    # Initial guess for eccentric anomaly (E)
    E = mean_anomaly_rad
    
    # Newton-Raphson iteration
    max_iter = 100
    tol = 1e-10
    for _ in range(max_iter):
        E_new = E - (E - eccentricity * math.sin(E) - mean_anomaly_rad) / (1 - eccentricity * math.cos(E))
        if abs(E_new - E) < tol:
            break
        E = E_new
    
    # Calculate true anomaly (ν)
    tan_half_nu = math.sqrt((1 + eccentricity) / (1 - eccentricity)) * math.tan(E / 2)
    nu = 2 * math.atan(tan_half_nu)
    
    # Convert true anomaly from radians to degrees
    # true_anomaly_deg = math.degrees(nu)
    
    return nu


# Process each line in the file
for i in range(0, len(lines), 2):
    if i + 1 < len(lines):
        line1 = lines[i].strip()
        line2 = lines[i + 1].strip()
    else:
        break
    # Extract the relevant values from line 1
    epoch_year = int(line1[18:20])
    julian_day_frac = float(line1[20:32])

    # Calculate the epoch date
    epoch_start = datetime(year=2000 + epoch_year - 1, month=12, day=31)
    epoch_date = epoch_start + timedelta(days=julian_day_frac)

    # Extract year, month, and day from the epoch date
    epoch_years.append(epoch_date.year)
    epoch_months.append(epoch_date.month)
    epoch_days.append(epoch_date.day)
    inclination = float(line2[8:16])* np.pi / 180
    right_ascension = float(line2[17:25])* np.pi / 180
    eccentricity = float(line2[26:33])*10**-7
    arg_perigee = float(line2[34:42])* np.pi / 180
    mean_anomaly = float(line2[43:51])* np.pi / 180
    mean_motion = float(line2[52:63])* np.pi / 180
    semi_major_axis = (mu**(1/3) / (2*float(line2[52:63])*math.pi/86400)**(2/3)) 
    true_anomaly=solve_keplers_equation(mean_anomaly, eccentricity)
    
    # Append the values to the respective lists
    inclinations.append(inclination)
    right_ascensions.append(right_ascension)
    eccentricities.append(eccentricity)
    arg_perigees.append(arg_perigee)
    mean_anomalies.append(mean_anomaly)
    mean_motions.append(mean_motion)
    semi_major_axi.append(semi_major_axis)
    Arue_Anomalys.append(true_anomaly)
# Print the extracted values for each line
for i in range(len(inclinations)):
    print(f"Line {i+1}:")
    print(f"Epoch Year: {epoch_years[i]}")
    print(f"Epoch Month: {epoch_months[i]}")
    print(f"Epoch Day: {epoch_days[i]}")
    print(f"Inclination: {inclinations[i]}")
    print(f"Right Ascension of the Ascending Node: {right_ascensions[i]}")
    print(f"Eccentricity: {eccentricities[i]}")
    print(f"Argument of Perigee: {arg_perigees[i]}")
    print(f"Mean Anomaly: {mean_anomalies[i]}")
    print(f"Mean Motion: {mean_motions[i]}")
    print(f"semi_major_axis: {semi_major_axi[i]}")
    print(f"True Anomaly :  {Arue_Anomalys[i]}")
    print()
    