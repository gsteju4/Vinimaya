from  xlrd import open_workbook

def read_locators(sheetname):
    wb=open_workbook(r"D:\Selenium3\POM_Framework\excel_\Locators1.xls")
    ws=wb.sheet_by_name(sheetname)
    rows=ws.get_rows()
    headers=next(rows)
    return {row[0].value:(row[1].value,row[2].value) for row in rows }
    # used_rows = ws.nrows
    # data = {}
    #
    # for i in range(1, used_rows):
    #     rows = used_rows.values(i)
    #     data[rows[0]] = (rows[1], rows[2])
    #     print(data)
def read_headers(test_case_name,sheet_name):
    wb=open_workbook("../testdata.xls")
    ws=wb.sheet_by_name(sheet_name)
    used_rows=ws.nrows
    print(used_rows)
    for i in range(0,used_rows):
        print(ws.row_values(i))
        rows=ws.row_values(i)
        if rows[0]==test_case_name:
            _headers=ws.row_values(i-1)
            print(_headers)
            _headers=[_header for _header in _headers if _header.strip()]
            break
    return ','.join(_headers[2:])


def read_data(test_case_name,sheet_name):
    data=[]
    wb = open_workbook("../testdata.xls")
    ws = wb.sheet_by_name(sheet_name)
    used_rows = ws.nrows
    print(used_rows)
    for i in range(0, used_rows):
        print(ws.row_values(i))
        rows = ws.row_values(i)

        if rows[0] == test_case_name:
            temp_data=[item for item in rows if item.strip()]
            if temp_data[1].upper()=="YES":
                data.append(tuple(temp_data[2:]))
    return data