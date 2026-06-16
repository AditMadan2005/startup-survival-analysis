import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter

# Load data
df = pd.read_csv("startup_survival_clean.csv")

# Kaplan-Meier model
kmf = KaplanMeierFitter()

kmf.fit(
    durations=df["survival_time_days"],
    event_observed=df["event"]
)

# Create figure
plt.figure(figsize=(10, 6))

kmf.plot_survival_function()

plt.title("Startup Survival Curve")
plt.xlabel("Days")
plt.ylabel("Survival Probability")
plt.grid(True)

# Save plot
plt.savefig(
    "plots/kaplan_meier_overall.png",
    dpi=300,
    bbox_inches="tight"
)

print("Plot saved to plots/kaplan_meier_overall.png")

# Show plot
plt.show()