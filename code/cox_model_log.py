import pandas as pd
import numpy as np
from lifelines import CoxPHFitter

df = pd.read_csv("startup_survival_funded.csv")

# Log transform funding
df["log_funding"] = np.log(df["funding_total_usd"])

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

print("Dataset shape:", cox_df.shape)

cph = CoxPHFitter()

cph.fit(
    cox_df,
    duration_col="survival_time_days",
    event_col="event"
)

cph.print_summary()

cph.summary.to_csv("cox_results_log.csv")

print("Saved: cox_results_log.csv")