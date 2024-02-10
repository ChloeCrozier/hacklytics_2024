import pandas as pd
import numpy as np

# Generate sample first and last names
first_names = ['John', 'Jane', 'Alice', 'Bob', 'Emily', 'Michael', 'Olivia', 'David', 'Sophia', 'Daniel']
last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']

# Sample data
data = [
    {"latitude": 33.755671, "longitude": -84.388168, "escalation": 2},
        {"latitude": 33.785294, "longitude": -84.372491, "escalation": 3},
        {"latitude": 33.767912, "longitude": -84.360572, "escalation": 2},
        {"latitude": 33.752398, "longitude": -84.372829, "escalation": 3},
        {"latitude": 33.777536, "longitude": -84.401248, "escalation": 2},
        {"latitude": 33.741527, "longitude": -84.363420, "escalation": 3},
        {"latitude": 33.774611, "longitude": -84.388739, "escalation": 2},
        {"latitude": 33.780993, "longitude": -84.353287, "escalation": 3},
        {"latitude": 33.757120, "longitude": -84.370802, "escalation": 2},
        {"latitude": 33.769875, "longitude": -84.387544, "escalation": 3},
        {"latitude": 33.760944, "longitude": -84.372821, "escalation": 2},
        {"latitude": 33.788012, "longitude": -84.375049, "escalation": 3},
        {"latitude": 33.748509, "longitude": -84.380612, "escalation": 2},
        {"latitude": 33.776044, "longitude": -84.349819, "escalation": 3},
        {"latitude": 33.749849, "longitude": -84.392786, "escalation": 2},
        {"latitude": 33.772953, "longitude": -84.367248, "escalation": 3},
        {"latitude": 33.766482, "longitude": -84.360951, "escalation": 2},
        {"latitude": 33.785648, "longitude": -84.387152, "escalation": 3},
        {"latitude": 33.771891, "longitude": -84.375093, "escalation": 2},
        {"latitude": 33.761829, "longitude": -84.394625, "escalation": 3},
        {"latitude": 33.779612, "longitude": -84.360420, "escalation": 2},
        {"latitude": 33.747366, "longitude": -84.367109, "escalation": 3},
        {"latitude": 33.769201, "longitude": -84.374721, "escalation": 2},
        {"latitude": 33.782978, "longitude": -84.357289, "escalation": 3},
        {"latitude": 33.769515, "longitude": -84.394820, "escalation": 2},
        {"latitude": 33.754651, "longitude": -84.371612, "escalation": 3},
        {"latitude": 33.759895, "longitude": -84.363998, "escalation": 2},
        {"latitude": 33.782485, "longitude": -84.393070, "escalation": 3},
        {"latitude": 33.771212, "longitude": -84.392415, "escalation": 2},
        {"latitude": 33.754184, "longitude": -84.385801, "escalation": 3},
        {"latitude": 33.748237, "longitude": -84.388035, "escalation": 2},
        {"latitude": 33.784148, "longitude": -84.382874, "escalation": 3},
        {"latitude": 33.769743, "longitude": -84.383510, "escalation": 2},
        {"latitude": 33.748726, "longitude": -84.378821, "escalation": 3},
        {"latitude": 33.778056, "longitude": -84.355622, "escalation": 2},
        {"latitude": 33.786407, "longitude": -84.383722, "escalation": 3},
        {"latitude": 33.751768, "longitude": -84.359871, "escalation": 2},
        {"latitude": 33.767648, "longitude": -84.392812, "escalation": 3},
        {"latitude": 33.781186, "longitude": -84.373266, "escalation": 2},
        {"latitude": 33.770321, "longitude": -84.381499, "escalation": 3},
        {"latitude": 33.765246, "longitude": -84.374225, "escalation": 2},
        {"latitude": 33.758930, "longitude": -84.395369, "escalation": 3},
        {"latitude": 33.780694, "longitude": -84.368081, "escalation": 2},
        {"latitude": 33.757479, "longitude": -84.364467, "escalation": 3},
        {"latitude": 33.745712, "longitude": -84.382178, "escalation": 2},
        {"latitude": 33.773405, "longitude": -84.370024, "escalation": 3},
        {"latitude": 33.763327, "longitude": -84.384620, "escalation": 2},
        {"latitude": 33.778824, "longitude": -84.387274, "escalation": 3},
        {"latitude": 33.757103, "longitude": -84.377090, "escalation": 2},
        {"latitude": 33.765963, "longitude": -84.389287, "escalation": 3},
        {"latitude": 33.762319, "longitude": -84.358964, "escalation": 2},
        {"latitude": 33.770583, "longitude": -84.394315, "escalation": 3},
        {"latitude": 33.786238, "longitude": -84.360490, "escalation": 2},
        {"latitude": 33.762880, "longitude": -84.378544, "escalation": 3},
        {"latitude": 33.775648, "longitude": -84.382649, "escalation": 2},
        {"latitude": 33.771169, "longitude": -84.391106, "escalation": 3}
]

# Generate random first and last names
def generate_random_names():
    return np.random.choice(first_names), np.random.choice(last_names)

# Add first and last names to the data
for entry in data:
    entry['First Name'], entry['Last Name'] = generate_random_names()

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('hospital_patient_data.csv', index=False)