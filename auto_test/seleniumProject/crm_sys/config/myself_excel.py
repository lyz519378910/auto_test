import xlrd


class OperationExcel:

    def __init__(self,path,sheet_name):
        self.workbook = xlrd.open_workbook(path)
        self.sheet = self.workbook.sheet_by_name(sheet_name)

    def get_row(self):
        return self.sheet.nrows

    def get_col(self):
        return self.sheet.ncols

    def get_cell(self,row,col):
        cell_value = self.sheet.cell_value(row,col)
        if cell_value == 'null':
            cell_value = ''
        return cell_value

# if __name__ == '__main__':
#     open = OperationExcel('D:\\case.xlsx','Sheet1')
#
#     # for i in range(0,open.get_row()):
#     #     for v in range(0,open.get_col()):
#     #     #     value = sheet.cell_value(i, v)
#     #     #     print('[' + str(i + 1) + chr(int(v) + 65) + ']:' + value, end='\t\t\t')
#     #     # print()
#     open.get_cell(1,1)
#
#
