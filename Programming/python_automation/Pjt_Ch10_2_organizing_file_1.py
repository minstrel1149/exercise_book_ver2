from pathlib import Path
import os
import zipfile
from zipfile import ZipFile
import time
import sys

zipPath = Path.cwd() / 'result_attachments'

def backupZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = f'{os.path.basename(folder)}_{number}.zip'
        if not os.path.exists(zipFilename):
            break
        else:
            number += 1
    print(f'Creating {zipFilename}..')
    time.sleep(1)

    backupZip = ZipFile(zipPath / zipFilename, mode='w')

    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}..')
        time.sleep(0.5)
        backupZip.write(foldername)
        for filename in filenames:
            newBase = f'{os.path.basename(folder)}_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    
    backupZip.close()
    print('Process Done!')

backupZip(zipPath / sys.argv[1])