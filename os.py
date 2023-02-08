import shutil
import time
import os
def run_on_startup():
    while True:
        time.sleep(5)
        shutil.copy2('/home/rajaul/Documents/Raja/Open CV/test.py','/home/rajaul/Documents/Raja/Open CV/Resources/Faces')
        time.sleep(10)
        os.remove("/home/rajaul/Documents/Raja/Open CV/Resources/Faces/test.py")
if __name__=="__main__":
    run_on_startup()