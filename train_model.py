import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load the monitoring dataset
data = pd.read_csv("system_data.csv")

# Select system performance features
features = data[["cpu", "ram", "disk"]]

# Create the AI anomaly detection model
model = IsolationForest(
    contamination=0.05,
    random_state=42
)

# Train the model
model.fit(features)

# Detect anomalies
data["anomaly"] = model.predict(features)

# Save the results
data.to_csv("system_data_with_anomalies.csv", index=False)

# Save the trained model
joblib.dump(model, "anomaly_model.pkl")

print("AI model trained successfully!")
print()
print("Normal records:", (data["anomaly"] == 1).sum())
print("Anomalies:", (data["anomaly"] == -1).sum())
print()
print("Files created:")
print("1. system_data_with_anomalies.csv")
print("2. anomaly_model.pkl")