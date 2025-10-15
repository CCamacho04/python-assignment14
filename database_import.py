import sqlite3
import pandas as pd
import os 

conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()

for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        table_name = file.replace('.csv', '')
        df = pd.read_csv(file)
        df.to_sql(table_name, conn, if_exists = 'replace', index = False)
        
conn.commit()
conn.close()
print('Database has been imported')