import xlrd


class OperationExcel:

    def __init__(self,path,sheet_name):
        self.workbook = xlrd.open_workbook(path)
        self.sheet = self.workbook.sheet_by_name(sheet_name)

    def get_nrow(self):
        return self.sheet.nrows

    def get_ncol(self):
        return self.sheet.ncols

    def get_cell(self,row,col):
        cell_v=self.sheet.cell_value(row,col)
        if cell_v=='null':
            cell_v=''
        return cell_v

# if __name__=='__main__':
#     op=OperationExcel('D:\\io\\test_case.xlsx','用例参数')
#     print(op.get_cell(1,1))