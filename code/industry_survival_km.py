import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines.statistics import multivariate_logrank_test

# Load data
df = pd.read_csv("startup_survival_funded.csv")

# Top industries
top_industries = [
    "software",
    "web",
    "biotech",
    "mobile",
    "enterprise",
    "ecommerce"
]

df = df[df["category_code"].isin(top_industries)].copy()

print("Dataset shape:", df.shape)

# Kaplan-Meier plot
plt.figure(figsize=(12, 8))

kmf = KaplanMeierFitter()

for industry in top_industries:

    subset = df[df["category_code"] == industry]

    kmf.fit(
        subset["survival_time_days"],
        subset["event"],
        label=industry
    )

    kmf.plot_survival_function()

plt.title("Startup Survival by Industry")
plt.xlabel("Days")
plt.ylabel("Survival Probability")
plt.grid(True)

plt.savefig(
    "plots/industry_survival_km.png",
    dpi=300,
    bbox_inches="tight"
)

print("Saved: plots/industry_survival_km.png")

# Log-rank test
results = multivariate_logrank_test(
    df["survival_time_days"],
    df["category_code"],
    df["event"]
)

print("\nLog-Rank Test")
print(results.summary)

plt.show()