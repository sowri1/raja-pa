import pyodbc
try:
	db_file = r'''C:\databases\mine.accdb'''
except FileError:
	print('File import error')
	quit()
user = 'admin'
password = ''

odbc_conn_str = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=SOWRI\SQLEXPRESS;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
try:
	conn = pyodbc.connect(odbc_conn_str)
except Exception as e:
	print("Eroor")
	print(e)