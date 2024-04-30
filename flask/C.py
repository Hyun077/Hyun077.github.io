from pathlib import Path
import xlwings as xw
app = xw.App(visible=False, add_book=False)
folder = Path('C:/Users/eic/Desktop/TEST/temp')
file_lists = folder.glob('*.xls')
for file in file_lists:
    print(file)
    new_file_path = str(file.with_suffix('.xlsx'))
    workbook = app.books.open(file)
    workbook.save(new_file_path)
    workbook.close()
app.quit()