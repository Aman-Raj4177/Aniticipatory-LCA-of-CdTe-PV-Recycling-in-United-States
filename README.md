# MISA code for sensitivity analysis
This repository contains the code used to perform the Moment Independent Sensitivity Analysis (MISA) presented in the paper:

"Anticipatory Life Cycle Assessment of an Industry-Operated CdTe Photovoltaic Recycling Process in the United States"

Authors: Aman Raj, Dwarakanath Ravikumar, and Meryl Winicov

# Purpose
The Moment Independent Sensitivity Analysis (MISA) quantifies the contribution of uncertainty in the life cycle inventory data as the MISA Delta Index. A higher MISA Delta Index value indicates that the given input is more sensitive to the total emissions for a given impact category (Global Warming, Eutrophication, etc).

# Repository Structure
- `MISA code.py`                                         → Main script for running MISA Delta Index

# Required Python Packages
Follwing Packages are required to run the MISA code:
numpy
pandas
matplotlib
scipy

The python packages can be downloaded using the follwing commmands:
→ Spyder's Console: !pip install numpy pandas matplotlib scipy
→ Anaconda Prompt: conda install numpy pandas matplotlib scipy
