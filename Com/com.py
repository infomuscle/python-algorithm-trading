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

explore = win32com.client.Dispatch("InternetExplorer.Application")
explore.Visible = True

word = win32com.client.Dispatch("Word.Application")
word.Visible = True
