# 🌱 IoT Soil Moisture Monitoring & Alert System

An end-to-end IoT system for **real-time soil moisture monitoring**, built using Arduino, Python, InfluxDB, and Grafana. It provides **live dashboards** and **email alerts** when soil moisture drops below a specified threshold — ideal for smart farming and gardening applications.

## 🔧 Components Used

- **Arduino Uno** with soil moisture sensor  
- **pymata4** library for Arduino-Python communication  
- **InfluxDB** (via Docker) to store time-series data  
- **Grafana** for live dashboard and alert configuration  
- **Python scripts** to collect and forward sensor data  
- **SMTP (Grafana alert rule)** for automated email notifications  

## 🧠 Key Features

- 📊 **Real-Time Monitoring**: Sensor values are collected via Arduino and sent to InfluxDB every second.  
- 📈 **Grafana Dashboard**: Live visualization of moisture trends over time.  
- 📬 **Email Alerts**: Configured in Grafana to trigger alerts when values fall below a threshold.  
- 🗃️ **MySQL Support**: Optional integration to store sensor readings in a relational DB.  
- 🖥️ **GUI Console**: A Tkinter-based interface to visualize sensor data and water need status.  

## 🚀 Workflow

1. **Arduino reads** moisture values through analog pin.  
2. **Python (pymata4)** reads and processes values.  
3. **Data is pushed** to **InfluxDB** using `influxdb_client`.  
4. **Grafana** connects to InfluxDB and displays live metrics.  
5. **Alert Rule** in Grafana sends an email if moisture < defined threshold.  
6. **Optional**: Data is also saved into **MySQL** (`moisture_level_values` table).  

## 🗂️ Repository Structure

├── integrated_final_project.py # Main InfluxDB integration + sensor loop
├── soil.py # Alternative: Save to MySQL DB
├── database.py # SQLAlchemy-based DB handler
├── gui_consol.py # Tkinter GUI for local visualization
├── influxdb_setup.py # Sample InfluxDB write script
├── docker_compose.yml # Deploys InfluxDB container


## 🖼️ Grafana Dashboard & Alerts

- Dashboard was connected to **InfluxDB 1.8** (via Docker).  
- Real-time graphs plot soil moisture.  
- Alert rule: Sends email if moisture level is too low.  
- Adjust threshold in Grafana Alert settings.  

## 📚 Course Context

This project was developed as part of a university-level **IoT course**, focused on applying data acquisition, cloud monitoring and real-time alerting in smart agriculture.

📅 **Completed:** *December, 2021*  
