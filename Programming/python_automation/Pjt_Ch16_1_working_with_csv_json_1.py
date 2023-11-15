import csv
import os
from pathlib import Path

p1 = Path.cwd() / 'attachments'
p2 = Path.cwd() / 'result_attachments'

for csvFile in p1.glob('*csv'):
    csvRows = []
    fileObj = open(csvFile, mode='r')
    readerObj = csv.reader(fileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    fileObj.close()
    
    outputFileObj = open(p2 / 'walnut' / 'waffles' / csvFile.name, mode='w', newline='')
    writerObj = csv.writer(outputFileObj)
    writerObj.writerows(csvRows)
    outputFileObj.close()

print('Process Done!')