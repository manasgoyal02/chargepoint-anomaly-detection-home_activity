# EV Charging Station Anomaly Detection using Isolation Forest

## 1. Problem Understanding

Electric Vehicle (EV) charging stations generate continuous telemetry data including power consumption, voltage, current, temperature, energy delivered, and session information. Ensuring reliable operation of charging infrastructure requires detecting abnormal behavior such as hardware faults, voltage instability, sensor errors, and abnormal charging patterns.

Traditional rule-based monitoring systems can detect known faults but struggle to identify unknown or emerging anomalies. Therefore, this project aims to develop an unsupervised machine learning–based anomaly detection system capable of identifying unusual charging behavior using telemetry data.

The objective is to build a scalable anomaly detection pipeline that can:

- Identify abnormal charging behavior
- Detect hardware faults and physical inconsistencies
- Operate without labeled anomaly data
- Provide an inference pipeline for real-time anomaly detection

## 2. Exploratory Data Analysis (EDA)

The dataset consists of EV charging session telemetry including:

- Power (kW)
- Voltage (V)
- Current (A)
- Temperature (°C)
- Energy delivered (kWh)
- Session duration (seconds)
- Error codes
- Timestamp and station identifiers

### Key Findings from EDA

**Data completeness:**The dataset contained minimal missing values and was generally well structured.

**Correlation Analysis**
Correlation analysis revealed important relationships between charging parameters.

A strong positive correlation (0.86) was observed between energy_kwh and duration_sec, which aligns with the physical relationship between energy delivered and charging duration.

A moderate correlation (0.41) was observed between current and power_kw, consistent with the electrical relationship between current and power.

Voltage showed weak correlation with power_kw, suggesting that voltage remains relatively stable during charging operations, while current contributes more significantly to power variation.

Temperature showed weak to moderate correlations with other variables, indicating gradual thermal changes during charging sessions.


**Feature distributions:**  
Power, voltage, and current showed expected ranges for EV charging stations, though several outliers were observed.

**Outliers and anomalies:**  
Several abnormal readings were observed, including:
- Voltage instability
- Negative or inconsistent values
- Hardware fault codes

**Error code analysis:**  
Error codes indicated hardware and operational faults that could serve as strong anomaly indicators.


These observations support the use of engineered features such as power deviation, rolling statistics, and delta features to capture abnormal behavior beyond simple linear relationships.

---

## 3. Feature Engineering

To improve anomaly detection performance, several categories of features were engineered:

### 3.1 Time-Based Features

- Hour of day
- Day of week
- Weekend indicator

These features capture temporal usage patterns and unusual charging times.

### 3.2 Physics-Based Features

Physical relationships between voltage, current, and power were used to create:

- Expected power
- Power deviation
- Expected energy
- Energy deviation

These features help detect violations of physical charging behavior.

### 3.3 Rolling Statistical Features

Rolling mean and standard deviation were calculated for:

- Power
- Temperature

These capture short-term trends and fluctuations.

### 3.4 Delta Features

Change between consecutive readings:

- Power delta
- Temperature delta
- Voltage delta

These detect sudden abnormal changes.

### 3.5 Station-Level Features

Deviation from station-specific averages was calculated to detect station-specific anomalies.

### 3.6 Session-Level Features

Total session energy and duration were calculated to detect abnormal charging sessions.

These engineered features significantly improved the model's ability to detect anomalous behavior.

---

## 4. Modeling Approach and Rationale

This project used the Isolation Forest algorithm, an unsupervised anomaly detection method.

Isolation Forest works by randomly partitioning data points. Anomalies require fewer splits to isolate compared to normal points.

### Reasons for choosing Isolation Forest:

- Works without labeled anomaly data
- Efficient for large datasets
- Handles high-dimensional feature spaces well
- Proven effectiveness in anomaly detection applications

The model was trained using engineered features after applying feature scaling using StandardScaler.

The contamination parameter was set to 2%, meaning the model assumes approximately 2% of observations are anomalous.

### Tradeoffs and Alternative Approaches

Other anomaly detection approaches were considered but not implemented in this project.

**One-Class SVM:**  
One-Class SVM is effective for anomaly detection but can be computationally expensive and less scalable for larger datasets. It also requires careful tuning of kernel parameters, which can be challenging without labeled validation data.

**Autoencoders:**  
Autoencoders are capable of detecting complex and nonlinear anomaly patterns. However, they require neural network training, which is more complex and computationally intensive. They also typically require larger datasets and careful architecture tuning.

**LSTM-based anomaly detection:**  
LSTM models can capture temporal dependencies and are useful for time-series anomaly detection. However, they require significant training effort, more computational resources, and more complex implementation compared to Isolation Forest.

**Statistical threshold methods:**  
Simple threshold-based approaches are easy to implement but are limited in detecting complex anomalies involving multiple features or nonlinear relationships.

---

## 5. Evaluation Methodology

Since labeled anomaly data was not available, evaluation was performed using:

- Visualization of anomalies in feature space
- Validation against physics-based inconsistencies

This qualitative evaluation confirmed the effectiveness of the anomaly detection system.

---

## 6. Results and Interpretation

The Isolation Forest model successfully identified anomalous charging behavior including:

- Hardware fault conditions
- Voltage instability
- Sudden abnormal power spikes
- Physics-inconsistent charging behavior
- Abnormal session energy patterns

Visualization of anomalies showed that anomalous points were clearly separated from normal operational clusters.

The model demonstrated strong capability in identifying both known and unknown anomaly patterns.

The inference pipeline was also implemented to allow anomaly detection on new incoming data.

---

## 7. Inference Pipeline

A prediction pipeline was developed to:

- Load trained model and scaler
- Apply preprocessing and feature engineering
- Detect anomalies
- Output anomaly labels

This enables practical deployment of the anomaly detection system for real-time monitoring.

---

## 8. Limitations and Future Improvements

One limitation observed during this project is that the Isolation Forest model occasionally treated certain abnormal values, such as negative or physically inconsistent readings, as part of small clusters rather than always identifying them as anomalies. This behavior occurs because Isolation Forest detects anomalies based on how easily points can be isolated, and some abnormal values may still form small clusters in the feature space.

In the future, I would like to explore other anomaly detection techniques such as One-Class SVM and LSTM-based anomaly detection models. These approaches may capture complex patterns and temporal dependencies more effectively, potentially improving anomaly detection performance.

Additionally, further experimentation with different feature engineering strategies and model parameter tuning could improve the robustness and accuracy of the anomaly detection system.

## 9. Conclusion

This project successfully developed a machine learning–based anomaly detection system for EV charging station telemetry using Isolation Forest.

The system combines:

- Statistical anomaly detection
- Physics-based validation
- Feature engineering based on domain knowledge

The model effectively detects abnormal charging behavior and provides a scalable solution for monitoring EV charging infrastructure.

This approach demonstrates the effectiveness of unsupervised machine learning techniques in real-world anomaly detection problems.