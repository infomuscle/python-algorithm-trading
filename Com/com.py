import win32com.client

class CpStockCode:
    def __init__(self):
        self.stock = {'유한양행':'A000100'}
    def GetCount(self):
        return len(self.stock)
    def NameToCode(self, name):
        return self.stock[name]

instCpStockCode = CpStockCode()

print(instCpStockCode.GetCount())
print(instCpStockCode.NameToCode('유한양행'))

# explore = win32com.client.Dispatch("InternetExplorer.Application")
# explore.Visible = True
#
# word = win32com.client.Dispatch("Word.Application")
# word.Visible = True

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

# wb = excel.Workbooks.Add()
# ws = wb.Worksheets("Sheet1")
# ws.Cells(1,1).Value = "hello world"
# wb.SaveAs('C:\\bokeun\\pycharm\\python-algorithm-trading\\Com\\test.xlsx')

wb = excel.Workbooks.Open('C:\\bokeun\\pycharm\\python-algorithm-trading\\Com\\input.xlsx')
ws = wb.ActiveSheet
print(ws.Cells(1,1).Value)

excel.Quit()