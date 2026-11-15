
import pandas as pd
from evidently import Report
from evidently.presets import DataSummaryPreset

# Sample addition input data
data = pd.DataFrame({
    "number1": [10, 20, 30, 40, 50],
    "number2": [5, 10, 15, 20, 25],
    "result": [15, 30, 45, 60, 75]
})

# Create Evidently report
report = Report([
    DataSummaryPreset()
])

# Generate report
snapshot = report.run(data, None)

# Save report
snapshot.save_html("evidently_report.html")

print("Evidently report generated successfully!")
