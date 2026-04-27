import subprocess
import schedule 
import time  

def run_pipeline():
    subprocess.run(["python","src/clean.py"])
    subprocess.run(["python","src/analyse.py"])

schedule.every().monday.at("09:00").do(run_pipeline)

while True: 
    schedule.run_pending()
    time.sleep(3600) 