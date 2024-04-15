import win32com.client
from pypdf import PdfWriter
from os import listdir, remove
from os.path import isfile, join, exists, isdir
from typing import Union


# TODO: Прикрепить рс3 файл для другой машины

class DocumentACAD:
    def __init__(self):
        self.active_document = None
        self.doc = None
        self.app = win32com.client.Dispatch('AutoCAD.Application')

    def open_autocad_document(self, path: str) -> win32com.client.CDispatch:
        """Open Autocad Document and create Autocad Object
        :param path: path to the dwg file
        """
        try:
            if type(path) != str:
                raise TypeError("Path must be string type")
            if not isdir(path):
                raise FileNotFoundError("There is no such folder")
            self.doc = self.app.Documents.Open(path)
            self.active_document: win32com.client.CDispatch = self.app.ActiveDocument
            return self.active_document
        except Exception as e:
            print(f"###Error in open_autocad_document function###\n*****{e}*****")
        finally:
            pass

    def close_autocad_document(self):
        """Close Autocad Document
        """
        try:
            self.doc.Close()
        except Exception as e:
            print(f"###Error in close_autocad_document function###\n*****{e}*****")
        finally:
            pass

    @staticmethod
    def sheet_counting(active_document: win32com.client.CDispatch,
                       height: Union[int, str] = 220) -> int:
        """Counting of sheets from a table size
        :param height: table height (in mm)
        :param active_document: Autocad document object
        """
        try:
            if not isinstance(active_document, win32com.client.CDispatch):
                raise TypeError("Object doesn't belong to the win32com.client.CDispatch")
            if not type(height) not in (str, int):
                raise TypeError("height must be an integer")
            if type(height) == str:
                height = int(height)
            sheets_amount: int = 0
            for a_d in active_document.ModelSpace:
                if a_d.ObjectName == 'AcDbTable':
                    table = a_d
                    sheets_amount = int((int(table.Height) / height) + 1)
            return sheets_amount
        except Exception as e:
            print(f"###Error in sheet_counting function###\n*****{e}*****")
        finally:
            pass

    def save_file(self, path_to_save: str = None,
                  filename: str = None):
        """Save Autocad Document
        :param path_to_save: path to the folder for saving
        :param filename: name for saving file
        """
        try:
            if type(filename) not in (str, None):
                raise TypeError("Filename must be string type")
            if type(path_to_save) not in (str, None):
                raise TypeError("Path must be string type")
            if type(path_to_save) == str and not isdir(path_to_save):
                raise FileNotFoundError("There is no such folder")
            if set(filename).intersection(r'\\/:*?"<>|') and type(filename) == str:
                raise ValueError("Incorrect result file name")
            if type(path_to_save) == type(filename) is None:
                self.active_document.Save()
            else:
                result_file_name: str = join(path_to_save, f'{filename}.pdf')
                self.active_document.SaveAs(result_file_name)
        except Exception as e:
            print(f"###Error in merge_pdf_files function###\n*****{e}*****")
        finally:
            pass

    def print_sheets(self, path_to_print: str, amount: int):
        """Print opened AutoCAD file sheets
        :param path_to_print: destination folder to print document
        :param amount: amount of sheets to print
        """
        try:
            if type(path_to_print) != str:
                raise TypeError("Path_to_print must be string type")
            if type(amount) != int:
                raise TypeError("Amount must be int type")
            if not isdir(path_to_print):
                raise FileNotFoundError("There is no such folder")

            layouts_list = self.active_document.Layouts
            for i in range(1, amount):
                self.active_document.ActiveLayout = layouts_list[i]
                self.active_document.ActiveLayout.ConfigName = "DWG To PDF.pc3"
                self.active_document.Plot.PlotToFile(path_to_print)
        except Exception as e:
            print(f"###Error in merge_pdf_files function###\n*****{e}*****")
        finally:
            pass


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
        result_file_path = join(path, f'{project_code}.pdf')
        files = [join(path, f) for f in listdir(path) if (isfile(join(path, f)) and f.endswith('.pdf'))]
        if not files:
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
        print(f"###Error in merge_pdf_files function###\n*****{e}*****")
    finally:
        pass


# """Работа со свойствами"""
# print(act_doc.SummaryInfo.GetCustomByKey('ОбъектКороткий'))
# act_doc.SummaryInfo.SetCustomByKey('ОбъектКороткий', 'ЛОЛ_КЕК')
# print(act_doc.SummaryInfo.GetCustomByKey('ОбъектКороткий'))


# """Работа с таблицами (поиск добавление строк и вставка значений"""

# try:
#     for a in act_doc.ModelSpace:
#         if a.ObjectName == 'AcDbTable':
#             table = a
#             print(table.Rows, table.Columns)
#             table.SetCellValue(4, 4, "KU")
