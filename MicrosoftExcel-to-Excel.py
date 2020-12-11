import xlrd
import difflib

print ("Checking updates for Microsoft: \n")

#Otwieramy dwa excele na 1 arkuszu.
workbook = xlrd.open_workbook("TestowyArkusz.xls")
worksheet = workbook.sheet_by_index(0) 
workbook2 = xlrd.open_workbook("Security Updates 2020-11-18-085759am.xls")
worksheet2 = workbook.sheet_by_index(0) 


for x in range(len(worksheet.col(0))):  
    File1value1 = worksheet.cell(x, 0).value 
    File1value2 = worksheet.cell(x, 1).value
    print (File1value1, File1value2)
    for y in range(len(worksheet2.col(0))):
        print (x, y)
        if (File1value1 in worksheet2.cell(y, 0).value) and (File1value2 in worksheet2.cell(y, 1).value):
            print (File1value1, File1value2, "Znaleziono")
        else:
            print (File1value1, File1value2, "nie znaleziono")

    
    
    #openpyxl i jest funka iter_rows