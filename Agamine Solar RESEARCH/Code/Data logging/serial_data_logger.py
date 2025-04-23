import serial
import time
import csv
from datetime import datetime
import os
import shutil

# === Configuration ===
SERIAL_PORT = 'COM3'  # Update to match your system
BAUD_RATE = 19200
CSV_DIR = './data_logs'
CSV_FILENAME = 'led_data_log.csv'
LOG_INTERVAL_SECONDS = 600  # 10 minutes
HISTORY_DIR = './history'
SCRIPT_NAME = 'serial_data_logger.py'

# === Data Headers (based on original structure) ===
HEADERS = [
    'Charge current', 'Load current', 'Day length', 'Remaining grid charge capacity',
    'Remaining battery capacity', 'PV Voltage', 'PV Voltage goal', 'PWM duty cycle',
    'Recharged by AC grid', 'MPP statemachine event', 'CWR statemachine state',
    'Firmware Version', 'Load 1 State', 'Charge State', 'Battery Voltage',
    'Battery Voltage Threshold', 'Battery SOC', 'Internal Temperature',
    'External Temperature', 'FET Temperature', 'MPP State', 'HVD active',
    'PWM State', 'Load 2 State', 'Night length', 'Average Night length',
    'Time Counter'
]

def auto_backup():
    os.makedirs(HISTORY_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"{SCRIPT_NAME.replace('.py', '')}_{timestamp}.py"
    shutil.copyfile(SCRIPT_NAME, os.path.join(HISTORY_DIR, backup_name))
    print(f"[Auto-backup created → {backup_name}]")

def read_serial_data():
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=5) as ser:
        ser.write(b' ')
        time.sleep(2)
        raw = ser.read(143)
        return raw.decode('utf-8', errors='ignore')

def parse_data(raw_data):
    parts = raw_data.strip().split(';')
    if len(parts) < 3:
        return None
    parts[0] = parts[0][3:]
    parts = parts[:-1]
    try:
        return list(map(int, parts))
    except ValueError:
        return None

def write_to_csv(data_row):
    os.makedirs(CSV_DIR, exist_ok=True)
    file_path = os.path.join(CSV_DIR, CSV_FILENAME)
    file_exists = os.path.isfile(file_path)
    with open(file_path, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Timestamp'] + HEADERS)
        writer.writerow([datetime.now().isoformat()] + data_row)

def main():
    auto_backup()
    print("Starting data logger...")
    while True:
        raw = read_serial_data()
        parsed = parse_data(raw)
        if parsed:
            write_to_csv(parsed)
            print(f"Logged data at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("Failed to parse data")
        time.sleep(LOG_INTERVAL_SECONDS)

if __name__ == '__main__':
    main()