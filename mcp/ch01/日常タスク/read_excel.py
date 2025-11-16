import openpyxl
import json

# Excelファイルを読み込む
wb = openpyxl.load_workbook('商品マスタ.xlsx')
ws = wb.active

# データを取得
data = []
for row in ws.iter_rows(values_only=True):
    data.append(list(row))

# JSON形式で出力
print(json.dumps(data, ensure_ascii=False, indent=2))
