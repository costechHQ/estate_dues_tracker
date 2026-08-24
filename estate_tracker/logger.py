from datetime import datetime

LOG_FILE = "activity.log"

def log_event(message):
    """gets current date and time"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp} - {message}\n")