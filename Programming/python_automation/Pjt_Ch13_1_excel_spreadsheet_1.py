import openpyxl
import pandas as pd
from pathlib import Path

p1 = Path.cwd() / 'attachments'
p2 = Path.cwd() / 'result_attachments'

censusDf = pd.read_excel(p1 / 'censuspopdata.xlsx')

resultDf = (censusDf
            .assign(POP2010=lambda df: df['POP2010'].astype('int'))
            .groupby(['State', 'County'], as_index=False)[['POP2010']].sum()
)

xlsx = pd.ExcelWriter(p2 / 'resultcensuspopdata.xlsx', engine='openpyxl')
resultDf.to_excel(xlsx, sheet_name='Sheet1', index=False)
xlsx.close()

print('Process Done!')