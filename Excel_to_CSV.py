import os
import pandas as pd

path = "D:\Projects\Excel to CSV"

files = os.listdir(path)
# print(files)

for excelfile in files:
    if excelfile.endswith(".xlsx"):
        clean_name = excelfile.replace(".xlsx", "")
        # print(excelfile)

        xlsx_file = pd.ExcelFile(excelfile)
        sheets = xlsx_file.sheet_names
        # print(sheets)

        for ind_sheet in sheets:
            sheet_data = xlsx_file.parse(ind_sheet)

            csv_file_name = clean_name + "-" + ind_sheet + ".csv"
            sheet_data.to_csv(csv_file_name, index = False)