import xlrd
class  ExcelUtil:
    def read_excel(self, excel_path, sheet_name):
        xls = xlrd.open_workbook(excel_path)
        sheet = xls.sheet_by_name(sheet_name)
        dataList = []
        for line in range(1, sheet.nrows):
            tempList = []
            tempList.append(sheet.cell_value(line, 1))
            tempList.append(sheet.cell_value(line, 2))
            dataList.append(tempList)
        return dataList
if __name__ == '__main__':
    data = ExcelUtil().read_excel("/Users/shiying/testdata.xlsx")
    print(data)
