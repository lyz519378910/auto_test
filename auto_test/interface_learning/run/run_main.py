import openpyxl
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
import unittest
from interface_learning.util.handle_excel import excel_data

class RunMain:

    def run_case(self):
        rows = excel_data.get_rows()
        for i in range(rows):
            data = excel_data.get_rows_value(i+2)
            print(data)

if __name__ == '__main__':
    rm = RunMain()
    rm.run_case()