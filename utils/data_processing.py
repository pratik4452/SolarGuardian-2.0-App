import pandas as pd

def detect_faults(df):
    fault_log = []

    for i, row in df.iterrows():
        if row['string_current'] < 2:
            fault_log.append(f"String undercurrent at {row['timestamp']}")
        if row['inverter_status'] == 'OFF':
            fault_log.append(f"Inverter OFF at {row['timestamp']}")

    return fault_log
