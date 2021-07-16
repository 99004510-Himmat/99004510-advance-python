"""
Author- Himmat Singh
Project- Excel parsing into python
Date- 15 Jun 2021
PS_NO- 99004510
"""

import openpyxl
from functions import listPSno, diaplayOptions, getReqRow, semMarks, hobbies, cities, progLangs, domains


def main():
    object_to_be_loaded = openpyxl.load_workbook(
        "D:\\H\\Work\\Genesis\\99004510-advance python\\mini project\\resource\\raw_data.xlsx")
    sheet_to_be_loaded = object_to_be_loaded['Cities']

    row_data_list = []
    for i in range(2, 17):
        for j in range(1, 2):
            row_data_list.extend([sheet_to_be_loaded.cell(i, j).value])

    ps_no_list = listPSno.list_ps_no()
    print('List of PS numbers: \n')
    for nums in ps_no_list:
        print(nums)

    selected_row = 0
    entered_ps = int(input('\nEnter the PS no from the list: '))
    selected_row = getReqRow.find_data(row_data_list, entered_ps)

    diaplayOptions.display_options()
    try:
        entered_sheet_option = int(input('\nEnter the selection: '))
        print(selected_row)
        if entered_sheet_option == 1:
            data_received = semMarks.sem_marks(selected_row)
            if data_received is True:
                print('\nData retrieved')
        elif entered_sheet_option == 2:
            data_received = hobbies.hobbies(selected_row)
            if data_received is True:
                print('\nData retrieved')
        elif entered_sheet_option == 3:
            data_received = cities.cities(selected_row)
            if data_received is True:
                print('\nData retrieved')
        elif entered_sheet_option == 4:
            data_received = progLangs.programming_languages(selected_row)
            if data_received is True:
                print('\nData retrieved')
        elif entered_sheet_option == 5:
            data_received = domains.domains(selected_row)
            if data_received is True:
                print('\nData retrieved')

    except ValueError:
        print('\nEntered value is invalid.')


if __name__ == "__main__":
    main()
