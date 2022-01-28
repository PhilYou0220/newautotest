from tools.DB import db2, db3
from tools.parse_data import pd
from tools.auth_post import auth_request
import unittest
from tools.log import log
import datetime
import json


class Test1(unittest.TestCase):

    # 清空历史数据 真删除
    def setUp(self) -> None:
        del_sql = "DELETE from sand_factory WHERE `name`=\"游飞3测试砂石场\""
        db2.delete(del_sql)

    def test_process(self):
        global create_success, query_success, delete_success
        create_success = False
        query_success = False
        delete_success = False

        sql = "SELECT * FROM case_data where  id in (1,2,3,4)"
        result = db3.select(sql)
        for i in result:  # 对流程进行循环
            id, method, url, data, expect_return_data, username, password, status_code, *ig = pd.parse_data(i
                                                                                                            )  # ig是个list
            # print(id, method, url, return_data, username, password, status_code)
            real_return_data, real_status_code = auth_request.auth_post(username=username, password=password,
                                                                        data2=data, url=url)
            # print(real_r, real_status_code)

            # 砂石场 新增
            if id == 1:  # 砂石场 新增
                try:
                    str_expect_return_data = eval(json.dumps(expect_return_data, ensure_ascii=False))  # 转为字符串
                    str_real_return_data = str(real_return_data)  # 转为字符串
                    if status_code == real_status_code and str_expect_return_data == str_real_return_data:
                        create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        insert_sql = f"""INSERT INTO case_data_log VALUES (null,{id},\"success\",\"{real_return_data}\",\"{create_time}\")"""
                        db3.insert(insert_sql)
                        create_success = True
                    else:
                        create_time1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        log.error(
                            f"{url} 接口报错，预期返回值：{expect_return_data},实际返回值：{real_return_data},预期状态码：{status_code}，实际状态码：{real_status_code}")
                        insert_sql = f"""INSERT INTO case_data_log VALUES (null,{id},\"fail\",\"{real_return_data}\",\"{create_time1}\")"""
                        db3.insert(insert_sql)
                        self.assertEqual(first=1, second=2, msg="新增失败")  # 故意造错误用例 用于httptestrunner统计

                except:
                    create_time1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    log.error(
                        f"{url} 接口报错，预期返回值：{expect_return_data},实际返回值：{real_return_data},预期状态码：{status_code}，实际状态码：{real_status_code}")
                    insert_sql = f"""INSERT INTO case_data_log VALUES (null,{id},\"fail\",\"{real_return_data}\",\"{create_time1}\")"""
                    db3.insert(insert_sql)
                    self.assertEqual(first=1, second=2, msg="新增失败")  # 故意造错误用例 用于httptestrunner统计

            # 砂石场 查询 由于没有返回新增ID 所以直接去数据库查询最新的砂石场数据
            if id == 2 and create_success:
                db2_query_sql = f"""SELECT id FROM sand_factory  WHERE name=\"游飞3测试砂石场\" AND deleted=0 ORDER BY id DESC LIMIT 1"""

                try:
                    global db2_id
                    db2_id = db2.select_real(db2_query_sql)

                    # 更新获取到的ID值 更新第三条的用例的传参
                    template = {"id": 1}
                    case_data_data3 = '{'
                    for key in template.keys():
                        case_data_data3 += f'\\"{key}\\":{db2_id[0][0]}'
                    case_data_data3 += '}'
                    up_case_dataa_3 = f"""update case_data set data=\"{case_data_data3}\" where id=3"""
                    db3.update(up_case_dataa_3)

                    if db2_id and status_code == real_status_code:  # ((171,),) 没有查到就是()
                        if db2_id[0][0] == real_return_data["data"][0]["id"]:  # 比较ID值是否相同
                            create_time2_1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            insert_sql2_1 = f"""INSERT INTO case_data_log VALUES (null,{id},\"success\",\"{real_return_data}\",\"{create_time2_1}\")"""
                            db3.insert(insert_sql2_1)
                            query_success = True
                        else:
                            create_time2_2 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            log.error(
                                f"{url} 接口报错，预期返回值：{expect_return_data},实际返回值：{real_return_data},预期状态码：{status_code}，实际状态码：{real_status_code}")
                            insert_sql2_2 = f"""INSERT INTO case_data_log VALUES (null,{id},\"fail\",\"{real_return_data}\",\"{create_time2_2}\")"""
                            db3.insert(insert_sql2_2)
                            self.assertEqual(first=1, second=2, msg="查询失败")  # 故意造错误用例 用于httptestrunner统计

                except:
                    create_time2_2 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    log.error(
                        f"{url} 接口报错，预期返回值：{expect_return_data},实际返回值：{real_return_data},预期状态码：{status_code}，实际状态码：{real_status_code}")
                    insert_sql2_2 = f"""INSERT INTO case_data_log VALUES (null,{id},\"fail\",\"{real_return_data}\",\"{create_time2_2}\")"""
                    db3.insert(insert_sql2_2)
                    self.assertEqual(first=1, second=2, msg="查询失败")  # 故意造错误用例 用于httptestrunner统计
            # 砂石场 删除
            if id == 3 and create_success and query_success:

                # 由于在id=2时更新了最新的id id=3时重新查询
                sql3 = "SELECT * FROM case_data where  id=3"
                result3 = db3.select(sql3)
                for i3 in result3:  # 对流程进行循环
                    id, method, url3, data3, expect_return_data, username3, password3, status_code, *ig = pd.parse_data(
                        i3
                        )  # ig是个list
                    # print(id, method, url, return_data, username, password, status_code)
                    real_return_data, real_status_code = auth_request.auth_post(username=username3, password=password3,
                                                                                data2=data3, url=url3)

                try:
                    str_expect_return_data3 = eval(json.dumps(expect_return_data, ensure_ascii=False))  # 转为字符串
                    str_real_return_data3 = str(real_return_data)  # 转为字符串
                    if status_code == real_status_code and str_expect_return_data3 == str_real_return_data3:
                        create_time3_1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        insert_sql3_1 = f"""INSERT INTO case_data_log VALUES (null,{id},\"success\",\"{real_return_data}\",\"{create_time3_1}\")"""
                        db3.insert(insert_sql3_1)
                        delete_success = True
                    else:
                        create_time3_2 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        log.error(
                            f"{url} 接口报错，预期返回值：{expect_return_data},实际返回值：{real_return_data},预期状态码：{status_code}，实际状态码：{real_status_code}")
                        insert_sql3_2 = f"""INSERT INTO case_data_log VALUES (null,{id},\"fail\",\"{real_return_data}\",\"{create_time3_2}\")"""
                        db3.insert(insert_sql3_2)
                        self.assertEqual(first=1, second=2, msg="删除失败")  # 故意造错误用例 用于httptestrunner统计

                except:
                    create_time3_2 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    log.error(
                        f"{url} 接口报错，预期返回值：{expect_return_data},实际返回值：{real_return_data},预期状态码：{status_code}，实际状态码：{real_status_code}")
                    insert_sql3_2 = f"""INSERT INTO case_data_log VALUES (null,{id},\"fail\",\"{real_return_data}\",\"{create_time3_2}\")"""
                    db3.insert(insert_sql3_2)
                    self.assertEqual(first=1, second=2, msg="删除失败")  # 故意造错误用例 用于httptestrunner统计

            # 砂石场验证删除
            if id == 4 and create_success and query_success and delete_success:
                db4_query_sql = f"""SELECT id FROM sand_factory  WHERE name=\"游飞3测试砂石场\" AND deleted=1 ORDER BY id DESC LIMIT 1"""
                try:
                    str_expect_return_data4 = eval(json.dumps(expect_return_data, ensure_ascii=False))  # 转为字符串
                    str_real_return_data4 = str(real_return_data)  # 转为字符串
                    db4_id = db2.select_real(db4_query_sql)
                    if db4_id[0][
                        0] == db2_id[0][0] and status_code == real_status_code and str_expect_return_data4 == str_real_return_data4:  # ((171,),) 没有查到就是()
                        create_time4_1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        insert_sql4_1 = f"""INSERT INTO case_data_log VALUES (null,{id},\"success\",\"{real_return_data}\",\"{create_time4_1}\")"""
                        db3.insert(insert_sql4_1)
                    else:
                        create_time4_2 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        log.error(
                            f"{url} 接口报错，预期返回值：{expect_return_data},实际返回值：{real_return_data},预期状态码：{status_code}，实际状态码：{real_status_code}")
                        insert_sql4_2 = f"""INSERT INTO case_data_log VALUES (null,{id},\"fail\",\"{real_return_data}\",\"{create_time4_2}\")"""
                        db3.insert(insert_sql4_2)
                        self.assertEqual(first=1, second=2, msg="查询失败")  # 故意造错误用例 用于httptestrunner统计

                except:
                    create_time4_2 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    log.error(
                        f"{url} 接口报错，预期返回值：{expect_return_data},实际返回值：{real_return_data},预期状态码：{status_code}，实际状态码：{real_status_code}")
                    insert_sql4_2 = f"""INSERT INTO case_data_log VALUES (null,{id},\"fail\",\"{real_return_data}\",\"{create_time4_2}\")"""
                    db3.insert(insert_sql4_2)
                    self.assertEqual(first=1, second=2, msg="查询失败")  # 故意造错误用例 用于httptestrunner统计

    # 再次验证 是否删除成功
    def tearDown(self) -> None:
        print("结束")


if __name__ == '__main__':
    unittest.main()
