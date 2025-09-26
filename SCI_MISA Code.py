# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 09:53:14 2025

@author: amanraj
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 09:49:20 2025

@author: amanraj
"""

import os
import numpy as np
import pandas as pd
from scipy.stats import wasserstein_distance

# === STEP 1: Read input from Excel ===
input_path = r"FSLR 7_Input_Sensitivity Analysis_Maricopa Ele.xlsx"                                    #CHANGE HERE!!!
df = pd.read_excel(input_path, sheet_name='FSLR 7_TRB_Smog')                  #CHANGE HERE!!!

# === STEP 2: Simulate lognormal variables ===
n = 10000
np.random.seed(0)

input_names = df['INPUT'].tolist()
input_values = {}
for _, row in df.iterrows():
    name = row['INPUT']
    mu1, sigma1 = row['IN_m'], row['IN_sd']
    mu2, sigma2 = row['Smog_m'], row['Smog_sd']    #CHANGE HERE!!!
    samples = np.exp(
        np.random.normal(mu1, sigma1, n) +
        np.random.normal(mu2, sigma2, n)
    )
    input_values[name] = samples

# === STEP 3 & 4: Compute total output Y based on serial number logic ===

# Add inputs from Serial Number 1 to 25 (i.e., rows 0 to 24)
# Chnage to 23 for FSLR 4 MISA analysis as it does not have heat and elcricuty for secondary frame production
# Chnage to 24 for FSLR 6 & FSLR 7 MISA analysis as it has heat and elcricuty for secondary frame production
X_add = np.column_stack([input_values[df.iloc[i]['INPUT']] for i in range(0, 24)])
sum_add = X_add.sum(axis=1)

# Subtract inputs from Serial Number 26 to 39 (i.e., rows 24 to 38)
# Change to 34 for FSLR 4 MISA analysis as it has two less inventory (Frames)
# Change to 38 for FSLR 6 MISA analysis as it has virgin Al production and electricity required for alloying
# Change to 37 for FSLR 7 MISA analysis as it has virgin steel production
X_sub = np.column_stack([input_values[df.iloc[i]['INPUT']] for i in range(24, 37)]) 
sum_sub = X_sub.sum(axis=1)

# Total output
Y = sum_add - sum_sub

# === STEP 5: Compute MISA Delta Index per input ===
quantiles = [10, 30, 50, 70, 90]
mean_deltas = []
for name in input_names:
    xi = input_values[name]  # get the sampled values for this input
    delta_vals = []
    for q in quantiles:
        val = np.percentile(xi, q)
        mask = np.abs(xi - val) < 0.05 * xi.ptp()  # 5% range around the percentile
        if mask.sum() > 200:
            delta = wasserstein_distance(Y, Y[mask])
            delta_vals.append(delta)
    mean_deltas.append(np.mean(delta_vals) if delta_vals else np.nan)

# print("Length of input_names:", len(input_names))
# print("Length of mean_deltas:", len(mean_deltas))


# === STEP 6: Write results to Excel ===
out_df = pd.DataFrame({
    'INPUT': input_names,
    'MISA Delta Index': mean_deltas
})

# your desired folder:
output_dir = r"FSLR 7_MISA Indices"                                         #CHANGE HERE!!!
os.makedirs(output_dir, exist_ok=True)                          

# desired filename (with .xlsx extension)
filename = "Marcopa Ele_FSLR 7_Smog MISA index.xlsx"                                       #CHANGE HERE!!!
output_path = os.path.join(output_dir, filename)

out_df.to_excel(output_path, index=False)
print(f"Results written to:\n{output_path}")