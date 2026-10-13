import openpyxl, pandas as pd
def load(f):
    wb=openpyxl.load_workbook(f,read_only=True); out={}
    for ws in wb.worksheets:
        rows=[list(r) for r in ws.iter_rows(values_only=True)]
        hi=0 if ws.title[0] in '۰۸۹' or ws.title.startswith('۱۰') else 1
        out[ws.title]=(rows[0][0] if hi else None, pd.DataFrame(rows[hi+1:],columns=rows[hi]))
    return out
