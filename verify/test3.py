d = {"ss": 555}
data = '{'
for key in d.keys():
    data += f'\\"{key}\\":{d[key]}'
data += '}'
print(data)
