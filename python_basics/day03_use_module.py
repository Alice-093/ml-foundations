import stats_utils

if __name__ == "__main__":
    numbers = [1,2,3,4,5]

    # 异常测试1：空列表
    try:
        stats_utils.mean([])
    except ValueError as e:
        print("空列表测试：", e)

    # 异常测试2：包含非数值元素
    try:
        stats_utils.mean([1, "abc", 3])
    except TypeError as e:
        print("非数值测试：", e)

    # 异常测试3：standard 参数不是数字
    try:
        stats_utils.count_above([1, 2, 3], "2")
    except TypeError as e:
        print("标准值类型测试：", e)

    # 异常测试4：nums 列表中包含非数值元素
    try:
        stats_utils.count_above([1, 2, "abc"], 2)
    except TypeError as e:
        print("列表元素类型测试：", e)

    means_num = stats_utils.mean(numbers)
    fangcha = stats_utils.variance(numbers)
    passing_num = stats_utils.count_above(numbers,means_num)
    print("平均值为：",means_num)
    print("方差为：",fangcha)
    print("超过平均值的数一共有：",passing_num)