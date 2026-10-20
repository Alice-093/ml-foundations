
import numpy as np

# 1. 创建矩阵
# A 的预期 shape：(2, 3)
A = np.array([[1, 2, 3],
              [4, 5, 6]])
print("A:\n", A)
print("A shape:", A.shape)

# B 的预期 shape：(3, 2)
B = np.array([[1, 2],
              [3, 4],
              [5, 6]])
print("B shape:", B.shape)

# 2. 逐元素乘法 *
# D 与 A 的 shape 都是 (2, 3)
D = np.array([[10, 20, 30],
              [40, 50, 60]])

# 预期 shape：(2, 3)
elementwise = A * D
print("\n逐元素乘法 A * D:\n", elementwise)
print("shape:", elementwise.shape)

# 3. 矩阵乘法 @
# (2, 3) @ (3, 2) -> (2, 2)
C = A @ B
print("\n矩阵乘法 A @ B:\n", C)
print("shape:", C.shape)

# 4. 矩阵转置 .T
# (2, 3) -> (3, 2)
A_T = A.T
print("\nA 的转置:\n", A_T)
print("shape:", A_T.shape)

# 5. 按列求均值
# axis=0，(2, 3) -> (3,)
col_mean = np.mean(A, axis=0)
print("\n列均值:", col_mean)
print("shape:", col_mean.shape)

# 6. 广播：每一列减去该列的均值
# (2, 3) - (3,) -> (2, 3)
# 向量化运算，不需要逐元素编写 for 循环
A_centered = A - col_mean
print("\n中心化后的矩阵:\n", A_centered)
print("shape:", A_centered.shape)

# 7. 按行求均值
# axis=1，(2, 3) -> (2,)
row_mean = np.mean(A, axis=1)
print("\n行均值:", row_mean)
print("shape:", row_mean.shape)

# 8. 欧氏距离
# 两个向量的 shape 都是 (3,)
v1 = np.array([1, 2, 3])
v2 = np.array([4, 6, 8])

# (3,) - (3,) -> (3,)
diff = v1 - v2
print("\n向量差:", diff)
print("shape:", diff.shape)

# 对差值平方、求和、开平方，得到一个标量
dist = np.sqrt(np.sum(diff ** 2))
print("欧氏距离:", dist)
print("shape:", np.shape(dist))