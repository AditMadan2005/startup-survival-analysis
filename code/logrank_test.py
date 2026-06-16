import pandas as pd
from lifelines.statistics import multivariate_logrank_test

df = pd.read_csv("startup_survival_funded.csv")

df["funding_group"] = pd.qcut(
    df["funding_total_usd"],
    q=4,
    labels=["Low", "Medium-Low", "Medium-High", "High"]
)

results = multivariate_logrank_test(
    df["survival_time_days"],
    df["funding_group"],
    df["event"]
)

print(results.summary)