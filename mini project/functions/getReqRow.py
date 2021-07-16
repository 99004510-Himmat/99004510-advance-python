"""
Function to get the required row from the source file
"""
import openpyxl


def get_row():
    object_to_be_loaded = openpyxl.load_workbook("D:\\H\\Work\\Genesis\\99004510-advance python\\mini project\\resource\\raw_data.xlsx")
    sheet_to_be_loaded = object_to_be_loaded['Sem Marks']

    row_data_list = []
    for i in range(2, 17):
        for j in range(1, 2):
            row_data_list.extend([sheet_to_be_loaded.cell(i, j).value])


def find_data(row_list1, ps1):
    print(ps1)
    print(row_list1)
    for k in range(len(row_list1)):
        if row_list1[k] == ps1:
            return k + 2
