from datetime import datetime

with open("doorbell.log", "a") as logFile:
    logFile.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S - Doorbell rang\n"))
