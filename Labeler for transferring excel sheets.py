from xlrd import *
import xlrd
import xlwt
import xlutils.copy
path = 'C:\\Users\\username\\Py\\Storage\\storage files python.xls'

rb = xlrd.open_workbook(path, formatting_info=True)
r_sheet = rb.sheet_by_index(0) #read only copy to inspect file
wb = xlutils.copy.copy(rb)           #writable copy (Cant read, only write)
w_sheet = wb.get_sheet(0) #sheet to write to within writable copy 

f = open('selection.txt', 'r')
data = [line.rstrip('\n') for line in f]
f.close()
log = open('Logs.txt', 'w')



def FileCheck(x):
    parsed_number = 0
        
    for i in data:
        
        for r in range(1, r_sheet.nrows):
            parsed_number += 1
            
            if str(i).strip() == str(r_sheet.cell(r,1).value).strip() and str(i).strip() != "same as above" and str(i).strip() != "":
                w_sheet.write(r,4,str(x))
                
                print(str(i) + " [x]")
                
               
            elif r == r_sheet.nrows:
                log.write(str(i) + '/n')
                print(str(i) + " [ ]")
                
    print("---Parsed "+ str(parsed_number) + " times ---")
           
user_label = str(input("what would you like to label files as - ")

FileCheck(user_label)

wb.save(path)
log.close()

input("Finished...")








