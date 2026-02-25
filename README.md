# Chargepoint-anomaly-detection-home_activity
# EV ChargePoint Anomaly Detection

Unsupervised anomaly detection in EV charging data using isolation trees.

This project detects anomalous EV charging events using an Isolation Forest model combined with strict domain-rule overrides. The system analyzes voltage, current, power, temperature, and temporal session behavior to identify hidden hardware faults, sensor degradation, and physics inconsistencies (such as negative power readings).

---

## ⚙️ Installation

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## 🚀 How to Run
### Step 1: Prepare your data
Ensure your input CSV file is placed in the root project folder (e.g., charging_logs.csv). 
The dataset must contain the following columns:
* station_id
* session_id
* timestamp
* voltage
* current
* power_kw
* temperature_c
* duration_sec
* energy_kwh
* error_code
* message

## Step 2: Navigate to the project directory
Open your terminal and navigate to the folder containing the script:
```bash
cd path/to/your/project_folder
```

## Step 3: Execute the prediction script
```bash
python predict.py your_file.csv
```

##  Output
The script automatically generates a new file named charging_logs_output.csv. This file retains all your original columns and appends one final column:
* is_anomaly: 0 (Normal event) or 1 (Anomaly detected)


## 👨‍💻 Author
Manas Goyal B.E. Computer Engineering

Thapar Institute of Engineering and Technology
