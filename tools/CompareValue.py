"""此函数用于对比新增的数据和查询时返回的数据的值"""


def compare_values(data, ss):
    data1 = data
    my_data = []
    for m in data.items():
        # 取出了所有的key,形式是字符串,存到my_data中，如['carNum', 'createdAt', 'endWeight', 'id']
        my_data.append(m[0])

    # 如[{'carNum': '', 'createdAt': 1611660907, 'endWeight': 0, 'id': 38}]
    ss1 = ss["data"]
    # my_ss现在是个字典了，如{'carNum': '', 'createdAt': 1611660907, 'endWeight': 0, 'id': 38}
    my_ss = ss1[0]
    for n in range(0, len(my_data)):
        # 防止传参时值为空
        if data1[my_data[n]] != "":
            # 判断值是否相等
            if data1[my_data[n]] == my_ss[my_data[n]]:
                print("传、返参数:{}和传、返回值的:{} 是一致的".format(my_data[n], my_ss[my_data[n]]))
            else:
                print("传、返参数为:{},传、返回值为:{}和{} 不一致！！！".format(my_data[n], data1[my_data[n]], my_ss[my_data[n]]))
        else:
            print("传入参数:{}是空的".format(my_data[n]))


# 再这个地方，可写可不写，防止执行两次
if __name__ == "__main__":
    compare_values(data, ss)
