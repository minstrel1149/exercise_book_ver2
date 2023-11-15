import time
import subprocess
from pathlib import Path
import pyautogui as pag

p1 = Path.cwd() / 'attachments'

timeleft = 3
while timeleft > 0:
    print(timeleft, end='\t')
    time.sleep(1)
    timeleft -= 1

try:
    subprocess.Popen(['start', p1 / 'alarm.wav'], shell=True)
    time.sleep(3)
    alarm = pag.getWindowsWithTitle('alarm')[0]
    alarm.close()
except:
    print('There is no file.')

print('Process Done!')