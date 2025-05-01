# IoT Moisture Monitoring & Alert System 🌱📡

This project is an IoT-based system that monitors soil moisture levels using a sensor connected to an Arduino. The data is visualized in real-time on Grafana and is used to trigger automatic email alerts when the moisture level drops below a defined threshold.

## 🔧 Components Used

- Arduino Uno
- Soil moisture sensor
- Wi-Fi module / Serial connection to server (based on your setup)
- Grafana (data visualization)
- InfluxDB (or similar time-series DB, if used)
- Email alerting system (SMTP or Grafana alert rule)

## 🧠 Features

- Real-time moisture level monitoring
- Live dashboard using Grafana
- Alert system that emails the user when moisture drops too low
- Queries for historical and real-time analysis
- Scalable for agricultural or gardening applications

## 🚀 Project Workflow

1. Arduino reads soil moisture data.
2. Data is sent to a backend (e.g., via serial or MQTT).
3. Data is stored and processed (e.g., in InfluxDB or another backend).
4. Grafana visualizes the data and triggers alerts.
5. Email sent if moisture is below the threshold.

## 📚 Course Context

This project was developed as part of an IoT course to apply real-world sensing, data processing and alerting workflows in smart agriculture systems.

📅 Completed: [Decemeber, 2021]
