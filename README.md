# MISA code for sensitivity analysis
This repository contains the code used to perform the Moment Independent Sensitivity Analysis (MISA) presented in the paper:

"Anticipatory Life Cycle Assessment of an Industry-Operated CdTe Photovoltaic Recycling Process in the United States"

Authors: Aman Raj, Dwarakanath Ravikumar, and Meryl Winicov

# Purpose
The Moment Independent Sensitivity Analysis (MISA) quantifies the contribution of uncertainty in the life cycle inventory data as the MISA Delta Index. A higher MISA Delta Index value indicates that the given input is more sensitive to the total emissions for a given impact category (Global Warming, Eutrophication, etc).

# Repository Structure
- `MISA code.py`                                         → Main script for running MISA Delta Index

# Installation of Python Packages
These Python packages are required to run the MISA code:
```bash
pip install numpy pandas matplotlib scipy
```
# Real Space and log space
Real Space: This is the original distribution of the data. In environmental studies, such data is often assumed to follow a lognormal distribution, meaning its logarithm is normally distributed.

Log Space: Also referred to as the "underlying normal space," it is obtained by taking the natural logarithm of data points from real space. This transformation is used when the data is assumed to follow a lognormal distribution, so the log-transformed data becomes normally distributed.

The expected mean value for the amount of an input (AM_m) is derived from a combination of industry-supplied primary data for the recycling process and literature-based secondary data for downstream processes, including secondary processing of recovered material, virgin material production, and landfill operations in the U.S. (see SI Sections S4–S8). The geometric standard deviation (GSD) for this amount (AM_GSD) is derived using the Pedigree Matrix (refer to the SI section S10). These values, which are in real space, are converted to the mean and standard deviation in log space using Equations 1 and 2:
Equation 1: μ (mean) = ln(E(X)) − (1/2 × σ²)

where E(X) is the expected mean in real space and σ is the geometric standard deviation in real space

Equation 2: σ (standard deviation) = ln(e^GSD)

The expected mean and standard deviation for a given input in a specific impact category (e.g., GHG_m and GHG_sd) are obtained from uncertainty analysis using SimaPro. A Monte Carlo simulation with 4000 runs was conducted for each input across Series 4, Series 6 and Series 7 CdTe PV recycling in the US. These values, originally in real space, are converted to log space using Equations 3 and 4:
Equation 3: μ (mean) = ln((E(X))² / √((E(X))² + (SD(X))²))

Equation 4: σ (standard deviation) = √(ln(((E(X))² + (SD(X))²) / (E(X))²))

where, E(X) is the expected mean in real space and SD(X) is the expected standard deviation in real space

Note: For amounts, the conversion of GSD from real space to log space is different because GSD is not the same as an expected standard deviation. To convert GSD from real space to log space, take the natural logarithm of the GSD.
