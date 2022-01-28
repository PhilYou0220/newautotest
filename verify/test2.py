from tools.DB import db2, db3
from tools.parse_data import pd
from tools.auth_post import auth_request
import unittest
from tools.log import log
import datetime
import json
import requests

db2_id = 183
b = {"id": db2_id}
c = json.dumps(b)
data = '{'
for key in b.keys():
    data += f'\\"{key}\\":{b[key]}'
data += '}'
# print(data)
a = f"""update case_data set data=\"{data}\" where id=3"""
db3.update(a)
sql = "select * from case_data where id=3"
result = db3.select(sql)
for i in result:  # 对流程进行循环
    id, method, url, data, expect_return_data, username, password, status_code, *ig = pd.parse_data(i
                                                                                                    )  # ig是个list
    # print(id, method, url, return_data, username, password, status_code)
    print(data)
    real_return_data, real_status_code = auth_request.auth_post(username=username, password=password,
                                                                data2=data, url=url)

u = 'https://ticketapitest.shomes.cn/-/point-sand-factory/delete'
h = {'content-type': 'application/json; charset=utf-8', 'shomes-user': '89089', 'shomes-type': 'web',
     'shomes-time': '1643354955', 'shomes-sign': 'ceb671cdcb9108db17b32129af8dca5a'}
d = '{"id": 181}'
real_return_data = requests.post(json=json.loads(d), url=u, headers=h).json()
r1 = real_return_data
