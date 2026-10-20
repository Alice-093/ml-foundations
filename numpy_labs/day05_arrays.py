
import numpy as np

# 1. 创建一维数组
A = np.array([1, 2, 3, 4, 5, 6])
print("1. 一维数组:", A)
print("shape:", A.shape)

# 2. 创建二维数组
B = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2. 二维数组:\n", B)
print("shape:", B.shape)

# 3. 一维数组 reshape 成二维数组
A_1 = A.reshape(2, 3)
print("\n3. A reshape:\n", A_1)
print("shape:", A_1.shape)

# 4. 二维数组 reshape
B_1 = B.reshape(3, 2)
print("\n4. B reshape:\n", B_1)
print("shape:", B_1.shape)

# 5. 按行求和
row_sum = B.sum(axis=1)
print("\n5. 按行求和:", row_sum)
print("shape:", row_sum.shape)

# 6. 按列求和
col_sum = B.sum(axis=0)
print("\n6. 按列求和:", col_sum)
print("shape:", col_sum.shape)

# 7. 布尔筛选
C = A[A > 3]
print("\n7. 布尔筛选:", C)
print("shape:", C.shape)

# 8. 数组切片
A_2 = B[0:1, 1:3]
print("\n8. 数组切片:\n", A_2)
print("shape:", A_2.shape)

# 9. 切片复制
A_3 = B[0:1, 1:3].copy()
print("\n9. 切片复制:\n", A_3)
print("shape:", A_3.shape)

# 验证复制后不会影响原数组
A_3[0, 0] = 99
print("\n修改复制数组后:", A_3)
print("原数组 B 不变:\n", B)