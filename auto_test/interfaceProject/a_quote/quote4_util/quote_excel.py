import xlrd


class ExcelOperation:

    def __init__(self, path, sheet_name):
        self.workbook = xlrd.open_workbook(path)
        self.sheet = self.workbook.sheet_by_name(sheet_name)

    # 获取某行的值
    def get_row_data(self, index=None):
        if index == None:
            index = 0
        return self.sheet.row_values(index)

    # 获取行数
    def get_row(self):
        return self.sheet.nrows

    # 获取列数
    def get_col(self):
        return self.sheet.ncols

    # 获取某个单元格的值
    def get_cell(self, row, col):
        cell_value = self.sheet.cell_value(row, col)
        if cell_value == 'null':
            cell_value = ''
        return cell_value

# if __name__ == '__main__':
#     open = ExcelOperation('D:\\Python\\auto_test\\interfaceProject\\a_quote\\quote3_config\\quote.xlsx','用例参数')
#     print(open.get_row())
#     print(open.get_col().real)
#     # for i in range(0,open.get_row()):
#     #     for v in range(0,open.get_col()):
#     #     #     value = sheet.cell_value(i, v)
#     #     #     print('[' + str(i + 1) + chr(int(v) + 65) + ']:' + value, end='\t\t\t')
#     #     # print()
#     open.get_cell(1,1)
#
#
