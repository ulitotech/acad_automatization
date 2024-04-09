from pyautocad import Autocad, APoint, ACAD
import win32com.client
import os, time

acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python\n")
# # acad.app.ActiveDocument.Plot.PlotToDevice()
# print('done')

# assm = acad.app.ActiveDocument.AcSmSheetSetMgr()
# acad.app.ActiveDocument.SaveAs(r'C:\Users\IProkopyev\Desktop\Новая папка (2)\lol.dwg', 12)

acad.doc.SendCommand('.ПОДШИВКА\n')
# acad.doc.Close()
# app = win32com.client.Dispatch('AutoCAD.Application')
# mng = win32com.client.Dispatch('AcSmSheetSetMgr.Application')
