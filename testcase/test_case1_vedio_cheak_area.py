"""
每个用例需要配置用例路径case_path 如 case_path = "video_check/vc_area.json"
然后解析用例为可直接使用的模式 如 case = GetData().more_get_data(case_path)

"""
import requests
import unittest
from tools.auth_post import AuthPost
from tools.get_data import GetData
from tools.read_json import ReadJson
from parameterized import parameterized


# def get_data():
#     data = ReadJson("video_check/vc_area.json").read_json()
#     test_data = []
#     real_test_data = []  # 承载[()]格式
#     for i in data.items():
#         test_data.append(i[1])
#     test_data = tuple(test_data)
#     real_test_data.append(test_data)
#     return real_test_data  # [('https://ticketapi.shomes.cn/-/select-option/area', {}, 'youfei', '1')]


class TestVideoCheck(unittest.TestCase):
    case_path = "video_check/vc_area.json"
    case = GetData().more_get_data(case_path)

    def setUp(self) -> None:
        print("开始")

    # 格式 parameterized.expand列表里嵌套元组 [()]一个元组算一条用例
    @parameterized.expand(case)
    def test_video_check_area(self, url, data, username, password, status_code):
        real_r, real_status_code = AuthPost().auth_post(url, data, username, password)  # 接收两个参数
        self.assertEqual(status_code, real_status_code)  # 断言状态码，不一致将报错
        # print(real_r)

    def tearDown(self) -> None:
        print("结束")


if __name__ == '__main__':
    unittest.main()
# r = AuthPost().auth_post2(a[0], a[1], a[2], a[3])
# print(r)
