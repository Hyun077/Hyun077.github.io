from pathlib import Path
import xlwings as xw

def change(filename):
    app = xw.App(visible=False, add_book=False)
    folder = Path('C:/Users/eic/Desktop/TEST/temp')
    file_lists = folder.glob(filename)
    for file in file_lists:
        new_file_path = str(file.with_suffix('.xlsx'))
        workbook = app.books.open(file)
        workbook.save(new_file_path)
        workbook.close()
    app.quit()
    return new_file_path

if __name__ == '__main__':
    change("123.xls")