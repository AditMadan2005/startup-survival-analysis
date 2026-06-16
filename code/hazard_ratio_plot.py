import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lifelines import CoxPHFitter

# Load data
df = pd.read_csv("startup_survival_funded.csv")

# Log transform funding
df["log_funding"] = np.log(df["funding_total_usd"])

# Select variables
cox_df = df[
    [
        "survival_time_days",
        "event",
        "log_funding",
        "funding_rounds",
        "milestones",
        "relationships"
    ]
].dropna()

# Fit Cox model
cph = CoxPHFitter()

cph.fit(
    cox_df,
    duration_col="survival_time_days",
    event_col="event"
)

# Extract results
summary = cph.summary.copy()

variables = summary.index
hr = summary["exp(coef)"]
lower = summary["exp(coef) lower 95%"]
upper = summary["exp(coef) upper 95%"]

# Calculate error bars
lower_error = hr - lower
upper_error = upper - hr

# Plot
plt.figure(figsize=(10, 6))

plt.errorbar(
    hr,
    range(len(hr)),
    xerr=[lower_error, upper_error],
    fmt='o',
    capsize=5
)

plt.axvline(
    x=1,
    linestyle='--'
)

plt.yticks(
    range(len(hr)),
    variables
)

plt.xlabel("Hazard Ratio")
plt.title("Hazard Ratios from Cox Proportional Hazards Model")

plt.grid(True)

# Save plot
plt.savefig(
    "plots/hazard_ratios.png",
    dpi=300,
    bbox_inches="tight"
)

print("Saved: plots/hazard_ratios.png")

plt.show()