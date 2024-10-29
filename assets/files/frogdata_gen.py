import pandas as pd
import numpy as np
from random import randint, choice, uniform

# Seed for reproducibility
np.random.seed(42)

# Parameters
num_frogs = 100
frog_ids = [3001 + i for i in range(num_frogs)]

# Qualitative features
types_of_species = ["Dart Frog", "Bullfrog", "Tree Frog", "Leopard Frog"]
habitat_options = ["Rainforest", "Swamp", "Pond", "Forest"]
sex_options = ["Male", "Female"]
sex_weights = [0.40, 0.60]
health_status_options = ["Healthy", "Sick", "Injured"]
health_status_weights = [0.80, 0.15, 0.05]

# Numerical features initialization
weights = []
age = []
body_sizes = []
max_hop_distances = []
upper_thermal_limits = []
call_frequencies = []

# Generate data
for species in range(num_frogs):
    species_type = choice(types_of_species)
    if species_type == "Dart Frog":
        weight = uniform(0.1, 0.2)
        body_size = uniform(2.0, 3.0)
        call_frequency = uniform(500, 800)
        max_hop_distance = uniform(1.0, 1.5)
        upper_thermal_limit = uniform(30, 35)
    elif species_type == "Bullfrog":
        weight = uniform(0.5, 1.0)
        body_size = uniform(5.0, 8.0)
        call_frequency = uniform(300, 500)
        max_hop_distance = uniform(2.5, 3.5)
        upper_thermal_limit = uniform(25, 30)
    elif species_type == "Tree Frog":
        weight = uniform(0.2, 0.4)
        body_size = uniform(3.0, 5.0)
        call_frequency = uniform(400, 600)
        max_hop_distance = uniform(1.5, 2.5)
        upper_thermal_limit = uniform(28, 32)
    else:  # Leopard Frog
        weight = uniform(0.4, 0.6)
        body_size = uniform(4.0, 6.0)
        call_frequency = uniform(350, 450)
        max_hop_distance = uniform(2.0, 3.0)
        upper_thermal_limit = uniform(27, 29)

    # Append generated values
    weights.append(round(weight * 1000, 1))
    age.append(randint(1, 10))  # Age between 1 to 10 years
    body_sizes.append(round(body_size, 2))
    max_hop_distances.append(round(max_hop_distance, 2))
    upper_thermal_limits.append(round(upper_thermal_limit, 2))
    call_frequencies.append(round(call_frequency, 2))

# Qualitative data
species_choices = [choice(types_of_species) for _ in range(num_frogs)]
sex_choices = np.random.choice(sex_options, num_frogs, p=sex_weights)
habitat_choices = [choice(habitat_options) for _ in range(num_frogs)]
health_choices = np.random.choice(
    health_status_options, num_frogs, p=health_status_weights
)

# Creating DataFrame
frog_data = pd.DataFrame(
    {
        "frog_id": frog_ids,
        "species": species_choices,
        "sex": sex_choices,
        "habitat": habitat_choices,
        "health": health_choices,
        "weight": weights,
        "size": body_sizes,
        "age": age,
        "max_hop": max_hop_distances,
        "thermal_limit": upper_thermal_limits,
        "call_freq": call_frequencies,
    }
)

frog_data.to_csv("frog_full_data.csv", index=False)

# Create new_arrivals dataset
frog_new_arrivals = frog_data.tail(23).copy()
frog_new_arrivals.loc[:, "arrival_date"] = pd.date_range(start='2023-01-01', periods=23, freq='D')
frog_new_arrivals.to_csv("frog_new_arrivals.csv", index=False)
frog_data = frog_data.iloc[:-23]

# Create baseline dataset with duplicate row and missing data
dataset_a = frog_data[['frog_id', 'species', 'sex', 'weight', 'age', 'size']]

duplicate_row = dataset_a.iloc[-1]
dataset_a = pd.concat([dataset_a, pd.DataFrame([duplicate_row])], ignore_index=True)

missing_data_row = {'frog_id': frog_ids[-1]+100, 'species': np.nan, 'sex': 'Male', 'weight': np.nan, 'age': 5, 'size': 10}
dataset_a = pd.concat([dataset_a, pd.DataFrame([missing_data_row])], ignore_index=True)

# Create baseline_update dataset with inconsistent data and unmatched frog_id
dataset_b = frog_data[['frog_id', 'habitat', 'health', 'max_hop', 'thermal_limit', 'call_freq']].copy()

inconsistent_data_row = {'frog_id': 'abc', 'habitat': 'Forest', 'health': 'good', 'max_hop': '1', 'thermal_limit': 35, 'call_freq': 20}
dataset_b = pd.concat([dataset_b, pd.DataFrame([inconsistent_data_row])], ignore_index=True)

new_frog_id_row = {'frog_id': 9999, 'habitat': 'Pond', 'health': 'Healthy', 'max_hop': 1.5, 'thermal_limit': 40, 'call_freq': 25}
dataset_b = pd.concat([dataset_b, pd.DataFrame([new_frog_id_row])], ignore_index=True)

# Save the datasets to new CSV files for further use
dataset_a.to_csv('frog_baseline.csv', index=False)
dataset_b.to_csv('frog_baseline_update.csv', index=False)