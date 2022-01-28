"""
每个用例需要配置用例路径case_path 如 case_path = "video_check/vc_area.json"
然后解析用例为可直接使用的模式 如 case = GetData().more_get_data(case_path)
"""
import unittest
from tools.auth_post import AuthPost
from tools.get_data import GetData
from parameterized import parameterized
from tools.log import log


class TestStationPointSandFactory(unittest.TestCase):
    case_path1 = "stationary_point/sand_factory_add.json"
    case1 = GetData().more_get_data(case_path1)
    case_path2 = "stationary_point/sand_factory_query.json"
    case2 = GetData().more_get_data(case_path2)

    # log.error(e)
    # log.error("用例数据解析异常")

    def setUp(self) -> None:
        print("开始")

    # 格式 parameterized.expand列表里嵌套元组 [()]一个元组算一条用例
    @parameterized.expand(case1)
    def test_stationary_point_sand_factory_add(self, url, data, username, password, status_code):

        real_r, real_status_code = AuthPost().auth_post(url, data, username, password)  # 接收两个参数
        # self.area_id = real_r["area_id"]
        # self.user_name = real_r["user_name"]
        try:
            self.assertEqual(status_code, real_status_code)  # 断言状态码，不一致将报错
        except:
            log.error(f"断言状态码错误，状态码应为：{status_code},实际为：{real_status_code}，返回值为{real_r}")

    @parameterized.expand(case2)
    def test_stationary_point_sand_factory_query(self, url, data, username, password, status_code):
        real_r, real_status_code = AuthPost().auth_post(url, data, username, password)  # 接收两个参数
        try:
            self.assertEqual(status_code, real_status_code)  # 断言状态码，不一致将报错
        except:
            log.error(f"断言状态码错误，状态码应为：{status_code},实际为：{real_status_code}，返回值为{real_r}")

    def tearDown(self) -> None:
        print("结束")


if __name__ == '__main__':
    unittest.main()
