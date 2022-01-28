from tools.DB import db2, db3
from tools.parse_data import pd
from tools.auth_post import auth_request
import unittest
from tools.log import log
import datetime
import json

create_success = False
query_success = False
delete_success = False

sql = "SELECT * FROM case_data where  id in (1,2,3)"
result = db3.select(sql)
for i in result:  # 对流程进行循环
    id, method, url, data, expect_return_data, username, password, status_code, *ig = pd.parse_data(i)  # ig是个list
    # print(id, method, url, return_data, username, password, status_code)
    real_return_data, real_status_code = auth_request.auth_post(username=username, password=password,
                                                                data2=data, url=url)
    # print(real_r, real_status_code)

    # 砂石场 新增
    if id == 1:  # 砂石场 新增
        try:
            if status_code == real_status_code and expect_return_data == json.loads(real_return_data):
                create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                insert_sql = f"""INSERT INTO case_data_log VALUES (null,{id},\'success\',\'{real_return_data}\',\'{create_time}\')"""
                db3.insert(insert_sql)
                create_success = True
        except:
            create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.error(
                f"{url} 接口报错，预期返回值：{expect_return_data},实际返回值：{real_return_data},预期状态码：{status_code}，实际状态码：{real_status_code}")
            insert_sql = f"""INSERT INTO case_data_log VALUES (null,{id},\'fail\',\'{real_return_data}\',\'{create_time}\')"""
            db3.insert(insert_sql)
            self.assertEqual(first=1, second=2, msg="新增失败")  # 故意造错误用例 用于httptestrunner统计
