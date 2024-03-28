# data_analysis_reporting.py

import pandas as pd

# Sample data (replace with actual data)
construction_data = pd.read_csv("construction_data.csv")

# Analyze construction materials data
material_stats = construction_data.groupby("material_type").agg({
    "quantity_used": "sum",
    "cost": "mean",
    "availability": "mean"
}).reset_index()

# Generate report
material_stats.to_csv("material_stats_report.csv", index=False)
print("Material statistics report generated successfully.")
