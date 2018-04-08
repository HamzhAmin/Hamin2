# Hamzah Amin 20178079
import urllib3
import chardet
from tabula import read_pdf
df=read_pdf("Name.pdf") # Read pdf table as 
df # Print to validate the results

import pandas as pd 
dff=pd.DataFrame(df)  #Convert the extracted pdf table to Panda DataFrame
dff # Print to validate the results

import pyodbc
import sqlalchemy
# My database is SQL Server 2014 Express
# I have created an empty table with the same DataFrame Structure
engine = sqlalchemy.create_engine("mssql+pyodbc://sa:123456@.\SQLEXPRESS/TestDB?driver=SQL+Server+Native+Client+10.0")
engine.connect()
dff.to_sql(name='T1',con=engine, if_exists='replace') # Insert my DataFrame content into SQL Server