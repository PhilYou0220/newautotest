from tools.log import log


class ParseData(object):
    def parse_data(self, case):
        try:
            url_prefix = 'https://ticketapitest.shomes.cn'  # 测试环境前缀
            id = case["id"]
            method = case["method"]
            url = url_prefix + case["url"]
            data = case["data"]
            expect_return_data = case["expect_return_data"]
            username = case["username"]
            password = case["password"]
            status_code = case["status_code"]
            name = case["name"]
            functionname = case["functionname"]
            return id, method, url, data, expect_return_data, username, password, status_code, name, functionname
        except Exception as e:
            log.error(e)


pd = ParseData()

if __name__ == '__main__':
    a = ParseData()
