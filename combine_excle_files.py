import os
import pandas as pd

not os.path.exists("combined_by_py.xlsx") or os.remove('combined_by_py.xlsx')

cwd = os.path.abspath('') 
files = os.listdir(cwd)  

## Method 1 gets the first sheet of a given file
df = pd.DataFrame()
for file in files:
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel(file), 
            ignore_index=True,
            #sort = True
            ) 
        print(f"Reading excel file ==> {file}")
df = df.drop_duplicates()
print(f"{df}")
df.to_excel('combined_by_py.xlsx')
