from openpyxl import load_workbook
import tkinter as tk

root = tk.Tk()

file = "demo.xlsx"
wb = load_workbook(file, data_only=True)
ws = wb.active

r = 1
for row in ws:
    c = 1
    for cell in row:
        tk.Label(root,text=cell.value).grid(row=r,column=c)
        c+=1
    r+=1

root.mainloop()