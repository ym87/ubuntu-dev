
# %%
import json
import csv

json_list = []

# CSV ファイルの読み込み
with open('input_data.csv', 'r') as f:
    for row in csv.DictReader(f):
        json_list.append(row)

# JSON ファイルへの書き込み
with open('output.json', 'w') as f:
    json.dump(json_list, f)

# JSONファイルのロード
with open('output.json', 'r') as f:
    json_output = json.load(f)

# %%
