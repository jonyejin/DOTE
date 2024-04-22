import os
import pandas as pd
import matplotlib.pyplot as plt

# Define temporal fluctuations
temporal_fluctuations = (1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2)

def extract_satisfied_demand(file_path):
    # Read the .opt file into a DataFrame
    df = pd.read_csv(file_path, sep='\s+', header=None, names=['Time', 'Satisfied_Demand'])

    # Return satisfied demand data
    return df['Satisfied_Demand'].values

# Directories containing .opt files
directories = [
    '/Users/franc/Documents/ideas/TEBench/.conda/DOTE/networking_envs/data/Abilene/opts_test',
    '/Users/franc/Documents/ideas/TEBench/.conda/DOTE/networking_envs/data/GEANT/opts_test',
    # Add more directories as needed
]

# Initialize data list to store satisfied demand data for each dataset
data = []

# Iterate over each directory
for directory in directories:
    # Initialize temporary list to store satisfied demand data for the current directory
    temp_data = []
    # Iterate over each .opt file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.opt'):
            file_path = os.path.join(directory, filename)
            # Extract satisfied demand data and append to the temporary data list
            temp_data.extend(extract_satisfied_demand(file_path))
    # Append the temporary data list to the main data list
    data.append(temp_data)

# Plotting
plt.figure(figsize=(10, 6))

# Plotting for each dataset
for i in range(len(directories)):
    plt.plot(temporal_fluctuations, data[i], label=f'Satisfied Demand ({os.path.basename(directories[i])})')

plt.xlabel('Time')
plt.ylabel('Satisfied Demand')
plt.title('Temporal Fluctuations vs. Satisfied Demand')
plt.legend()
plt.grid(True)
plt.show()
