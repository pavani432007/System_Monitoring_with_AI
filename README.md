# AI-Based Real-Time System Monitoring

## Project Description

AI-Based Real-Time System Monitoring is a Python-based application
that monitors CPU, RAM, and disk usage and detects unusual system
behavior using machine learning.

## Technologies Used

- Python
- Psutil
- Pandas
- Scikit-learn
- Isolation Forest
- Joblib
- Streamlit

## Features

- Real-time CPU monitoring
- Real-time RAM monitoring
- Disk usage monitoring
- Machine learning based anomaly detection
- Interactive Streamlit dashboard
- System performance visualization
- Anomaly status reporting

## Project Workflow

System
   ↓
Psutil
   ↓
CPU / RAM / Disk Data
   ↓
CSV Dataset
   ↓
Isolation Forest
   ↓
Anomaly Detection
   ↓
Streamlit Dashboard

## Machine Learning

The project uses the Isolation Forest algorithm for
unsupervised anomaly detection.

The model analyzes CPU, RAM, and disk usage and identifies
unusual system behavior without requiring manually labeled data.

## Project Files

- `monitor.py` - Collects CPU, RAM and disk usage data.
- `train_model.py` - Trains the Isolation Forest model.
- `dashboard.py` - Displays the monitoring dashboard.
- `anomaly_model.pkl` - Saved trained machine learning model.
- `requirements.txt` - Python dependencies.
- `.gitignore` - Files excluded from version control.

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt

**Step 3:** Below that, add:

```markdown
### 2. Start system monitoring

```bash
python monitor.py
### 2. Train the AI model

```bash
python train_model.py

Then below it:

### 3. Run the dashboard

Type:

```markdown
### 3. Run the dashboard

```bash
python -m streamlit run dashboard.py
