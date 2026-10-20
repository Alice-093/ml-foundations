# 求平均值
def mean(nums):
    # 检查1，列表不能为空
    if not nums:
        raise ValueError("输入列表不能为空")

    # 检查2，列表中的元素必须是数字
    for num in nums:
        if not isinstance(num,(int,float)):# isinstance(num, (int, float))判断变量 num 是否属于指定类型
            raise TypeError("列表元素必须是数字")
    
    total = 0
    for num in nums:
        total += num
    return total / len(nums)

# 求方差
def variance(nums):
    ans = 0
    avg = mean(nums)
    for num in nums:
        ans += (avg - num)**2
    return ans / len(nums)

# 计数

def count_above(nums,standard):
    
    if not isinstance(standard,(int,float)):
        raise TypeError("标准类型必须是整数或浮点数")
    
    for num in nums:
        if not isinstance(num,(int,float)):
            raise TypeError("列表中元素类型必须是整数或浮点数")
        
    count = 0
    for num in nums:
        if num > standard:
            count += 1
    return count

