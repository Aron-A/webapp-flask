import pyodbc


class DbModel():
   def __init__(self):
       self.db = ''
       super().__init__()

    def execute(self):
        print('')



cnxn = pyodbc.connect('DRIVER = SQL Server; SERVER = conspiracy; DATABASE = illuminati; UID='+username+';PWD='+password)