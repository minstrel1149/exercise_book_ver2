import PyPDF2
import os
from pathlib import Path

p1 = Path.cwd() / 'attachments'
p2 = Path.cwd() / 'result_attachments'

pdfFiles = [file for file in p1.glob('*.pdf')]
pdfFiles.sort()

pdfWriter = PyPDF2.PdfFileWriter()

for file in pdfFiles:
    pdfFileObj = open(file, mode='rb')
    try:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        for pageNum in range(1, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
    except:
        print(f'{file.name} is encrypted')

outputFileObj = open(p2 / 'allPdfCombined.pdf', mode='wb')
pdfWriter.write(outputFileObj)

outputFileObj.close()

print('Process Done!')