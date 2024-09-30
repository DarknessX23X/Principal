import csv
import os
import pyodbc
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.worksheet.table import Table
from openpyxl.utils import range_boundaries
from datetime import datetime

os.system('cls' if os.name == 'nt' else 'clear')
with open('X:\\BI\\CONFIG\\PLOTTER.CSV', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    for row in csvreader:
     #print(row[0])     
     #print(row[1])
     if "X:" not in row[1]:
        conn_str = r'Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={};PWD={};'.format(row[1], "sinajet")
        sql_query = 'SELECT * FROM PlotHistory'        
     else:
        conn_str = r'Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={};'.format(row[1])
        sql_query = 'SELECT * FROM PrintRecord'        
     conn = pyodbc.connect(conn_str)
     cursor = conn.cursor()     
     cursor.execute(sql_query)
     df = pd.read_sql_query(sql_query, conn)
     conn.close()
     path =os.path.join('X:\\BI\\DADOS\\',row[0]) +".CSV"
     df.to_csv(path, index=False, sep=';')

