import openpyxl


def list_ps_no():
    object_to_be_loaded = openpyxl.load_workbook("D:\\H\\Work\\Genesis\\99004510-advance python\\mini project\\resource\\raw_data.xlsx")
    sheet_to_be_loaded = object_to_be_loaded['Cities']

    ps_no = []
    for row in sheet_to_be_loaded.iter_rows(min_row=1, max_col=1, max_row=16, values_only=True):
        ps_no.append(list(row))
    return ps_no
