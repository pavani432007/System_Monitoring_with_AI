import psutil
import pandas as pd
import time
from datetime import datetime

data = []

print("System Monitoring Started...")
print("Collecting data. Press Ctrl+C to stop.")

try:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        data.append({
            "timestamp": datetime.now(),
            "cpu": cpu,
            "ram": ram,
            "disk": disk
        })

        print(f"CPU: {cpu}% | RAM: {ram}% | Disk: {disk}%")

        time.sleep(5)

except KeyboardInterrupt:
    df = pd.DataFrame(data)
    df.to_csv("system_data.csv", index=False)

    print("\nMonitoring stopped.")
    print("Dataset saved as system_data.csv")