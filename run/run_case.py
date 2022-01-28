"""路径一致性 都是../ 父目录"""
import unittest
import time
from tools.HTMLTestRunner import HTMLTestRunner
from testcase.test_case1_vedio_cheak_area import TestVideoCheck


def my_case():
    # suite = unittest.TestSuite()  # 初始化一个测试套件
    # suite.addTest(TestVideoCheck("test_video_check_area"))  # 添加用例
    # print(suite)
    suite = unittest.TestLoader().discover("../testcase", pattern="test_case_sta*.py")
    # print(suite)
    return suite


def my_run():
    suite = my_case()
    with open("../report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S")), mode="wb") as f:  # pycharm时分秒之间别使用冒号
        runner = HTMLTestRunner(stream=f, verbosity=2, title='试运行', description='第一次生成测试报告')
        runner.run(suite)


if __name__ == '__main__':
    my_run()
