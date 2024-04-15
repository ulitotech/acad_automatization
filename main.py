import win32com.client
from pypdf import PdfWriter
from os import listdir, remove
from os.path import isfile, join, exists, isdir

# app = win32com.client.Dispatch('AutoCAD.Application')
# doc = app.Documents.Open(r"C:\Users\IProkopyev\Desktop\Новая папка (2)\04_Адресный список.dwg")
# act_doc = app.ActiveDocument
# try:
#     pass
# except Exception as e:
#     print("Ошибка ", e)
# finally:
#     doc.Close()

# TODO: Прикрепить рс3 файл для другой машины

"""Открытие доков и создание приложения"""
# app = win32com.client.Dispatch('AutoCAD.Application')
# doc = app.Documents.Open(r"C:\Users\IProkopyev\Desktop\Новая папка (2)\ТП-121\01_Общие данные.dwg")
# act_doc = app.ActiveDocument
"""Сохранить как"""
# act_doc.SaveAs(r"C:\Users\IProkopyev\Desktop\Новая папка (2)\ТП-121\01_Общие данные_1.dwg")
"""Сохранить"""
# act_doc.Save()
"""Работа со свойствами"""
# print(act_doc.SummaryInfo.GetCustomByKey('ОбъектКороткий'))
# act_doc.SummaryInfo.SetCustomByKey('ОбъектКороткий', 'ЛОЛ_КЕК')
# print(act_doc.SummaryInfo.GetCustomByKey('ОбъектКороткий'))
"""Закрытие"""
# doc.Close()
"""Печать листов в документе"""
# layouts_list = act_doc.Layouts
# for i in range(1, len(layouts_list)):
#     print(i)
#     act_doc.ActiveLayout = layouts_list[i]
#     act_doc.ActiveLayout.ConfigName = "DWG To PDF.pc3"
#     act_doc.Plot.PlotToFile(fr"C:\Users\IProkopyev\Desktop\Новая папка (2)\ТП-121\тест{i}.pdf")
"""Работа с таблицами (поиск добавление строк и вставка значений"""
# try:
#     for a in act_doc.ModelSpace:
#         if a.ObjectName == 'AcDbTable':
#             table = a
#             print(table.Rows, table.Columns)
#             table.SetCellValue(4, 4, "KU")
"""Количество задействованных листов (220 - высота разбиения таблицы"""
# for a in act_doc.ModelSpace:
#     if a.ObjectName == 'AcDbTable':
#         table = a
#         print(table.Height)
#         print(round(int(table.Height) / 220) + 1)
"""Соединение PDF в один файл"""

def merge_pdf_files(path: str, project_code: str):
    """Merging files into a PDF file
    :param path: path to the PDF file
    :param project_code: name for result project
    """
    try:
        if type(project_code) != str:
            raise TypeError("Project code must be string type")
        if type(path) != str:
            raise TypeError("Path must be string type")
        if not isdir(path):
            raise FileNotFoundError("There is no such folder")
        if set(project_code).intersection(r'\\/:*?"<>|'):
            raise ValueError("Incorrect result file name")
        result_file_path = join(path,f'{project_code}.pdf')
        files = [join(path, f) for f in listdir(path) if (isfile(join(path, f)) and f.endswith('.pdf'))]
        if files == []:
            raise ValueError("File list is empty")
        if project_code in (None, ''):
            raise ValueError("There is no project code")
        merger = PdfWriter()
        if exists(result_file_path):
            remove(result_file_path)
        merger.write(result_file_path)
        for f in files:
            merger.append(f)
            merger.write(result_file_path)
            merger.close()
    except Exception as e:
        print(f"###Error in merge_pdf_files###\n*****{e}*****")
    finally:
        pass
