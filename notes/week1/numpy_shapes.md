# Day 05 -  NumPy数组入门

## 1.数学对象 ↔ NumPy 对象 对照
数学对象            记号            NumPy 的 shape          ndim维度
实数（标量）          a                  ()                  0
向量             v=(v1,v2,...vn)         (n,)               1
m×n 矩阵      A=(aij),i=1..m, j=1..n    (m, n)              2
三维张量            T=(tijk)            (m,n,p)             3

维度 = 描述一个元素需要几个下标。
而 shape 就是每个下标能取多少个值，按顺序写下来：(m,n) 表示「第 1 个下标有 m 种取值，第 2 个下标有 n 种取值」。
所以 shape 元组里有几个数字，就对应几个下标，就是几维

## 2.np.array 从列表创建数组
 ```python
 A = np.array([[1, 2, 3],
              [4, 5, 6]])      # shape (2, 3)
              print(a.ndim)   # 1
print(A.shape)  # (2,3)
print(A.dtype)  # int64
```
数学上写一个 2×3 矩阵,NumPy 里就是按行照抄，外层方括号代表整个矩阵，内层每个方括号代表一行
外层方括号 = 矩阵本身; 内层方括号 = 每一行方括号; 嵌套几层，就对应几个下标，就是几维

## 3.shape的用法
shape 会生成一个元组，其长度就是向量的维度
A.shape → (2, 3) #A 是 2×3 矩阵
A.shape[0] → 2  #行数m=2
A.shape[1] → 3  #列数n=3

## 4.reshape：数学上的「同一组数，换个排法」
数学里，给定 12 个数，你可以把它们排成 3×4 矩阵，也可以排成 2×6 矩阵。元素还是那 12 个，只是行列结构变了。
NumPy 的规则：按行（从左到右、从上到下）把元素拉直，再按新形状逐行填回去。
```python
np.arange(1, 13).reshape(3, 4)   # 生成一个从 1 开始、到 13 之前结束、步长为 1 的整数数组，重排成 3×4 矩阵
np.arange(1, 13).reshape(2, 6)   #  2×6 矩阵
```
约束只有一条：元素总数必须相等，即 m×n 不变
reshape(-1, 1) 就是数学上的列向量,reshape(1, -1) 是行向量。

## 5.按行 / 列求和：NumPy 的 axis
```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])          # shape (2, 3)

A.sum(axis=1)   # 行和 → [ 6, 15]   shape (2,)
A.sum(axis=0)   # 列和 → [5,  7,  9] shape (3,)
```
axis=k 的意思是「把第 k 个下标消掉，对它求和」
axis=1：消掉列下标 j → 剩下行下标 i → 结果长度 = 行数 m → 这正是行和，其余以此类推
axis=1 消列，得行和；axis=0 消行，得列和。

## 6.布尔筛选：「从矩阵里挑出满足条件的元素」
```python
A > 3            # 得到一个同形的布尔矩阵（每个位置标记 True/False）
A[A > 3]         # 把所有 True 位置的元素挑出来，返回 1 维数组
```
这是一个集合，不再有行列结构。所以布尔筛选后 ndim 一定是 1

## 7.切片：数学上的「取子矩阵」
数学里假设A是3 x 3矩阵，从 A 里取第 1~2 行、第 2~3 列组成子矩阵。
```python
A[0:2, 1:3]     # 行取 [0,2)，列取 [1,3) → shape (2, 2)
```
切片不降维因为取的是「0≤i<2 且 1≤j<3 的所有元素」，下标 i,j 都还在，只是范围缩小了，所以还是 2 维。

A[0] 是「把第 1 个下标固定为 0」，i 被定死了，不再自由，只剩 j 自由 → 变成 1 维向量 
(a01,a02,a03)(a01,a02,a03 )。所以整数索引降维。

## 8.六个shape示例
```python
import numpy as np

print("=" * 50)
print("【0】6 个形状示例 —— 记录 shape 与 ndim")
print("=" * 50)
examples = {
    "标量":            np.array(7),
    "1维向量":         np.array([1, 2, 3, 4, 5, 6]),
    "2维矩阵":         np.array([[1, 2, 3], [4, 5, 6]]),
    "列向量(3行1列)":  np.array([[1], [2], [3]]),
    "行向量(1行6列)":  np.array([[1, 2, 3, 4, 5, 6]]),
    "3维张量":         np.arange(24).reshape(2, 3, 4),
}
for name, arr in examples.items():
    print(f"{name:16s} ndim={arr.ndim}  shape={arr.shape}  dtype={arr.dtype}")


print("\n" + "=" * 50)
print("【1】创建一维 / 二维数组")
print("=" * 50)
a1 = np.array([1, 2, 3, 4, 5, 6])
print("a1  =", a1,        "| shape:", a1.shape, "| ndim:", a1.ndim)

a2 = np.array([[1, 2, 3], [4, 5, 6]])
print("a2  =\n", a2,     "\n| shape:", a2.shape, "| ndim:", a2.ndim)


print("\n" + "=" * 50)
print("【2】reshape：改形状不改数据")
print("=" * 50)
r = np.arange(12)
print("原始      shape:", r.shape, "| ndim:", r.ndim)

r_2_6 = r.reshape(2, 6)
print("2×6       shape:", r_2_6.shape, "| ndim:", r_2_6.ndim)

r_3_4 = r.reshape(3, 4)
print("3×4       shape:", r_3_4.shape, "| ndim:", r_3_4.ndim)

r_col = r.reshape(-1, 1)     # 变列向量
print("列向量    shape:", r_col.shape, "| ndim:", r_col.ndim)

r_row = r.reshape(1, -1)     # 变行向量
print("行向量    shape:", r_row.shape, "| ndim:", r_row.ndim)


print("\n" + "=" * 50)
print("【3】按行 / 列求和（重点看 axis 如何影响 shape）")
print("=" * 50)
m = np.arange(1, 13).reshape(3, 4)   # 3 行 4 列
print("m =\n", m, "\n| shape:", m.shape)

row_sum = m.sum(axis=1)      # 每行求和：压掉 axis=1
print("\n按行求和 m.sum(axis=1) =", row_sum,
      "| shape:", row_sum.shape, "← (3,4) 压掉第1轴 → (3,)")

col_sum = m.sum(axis=0)      # 每列求和：压掉 axis=0
print("按列求和 m.sum(axis=0) =", col_sum,
      "| shape:", col_sum.shape, "← (3,4) 压掉第0轴 → (4,)")

row_sum_keep = m.sum(axis=1, keepdims=True)
print("按行求和 keepdims   shape:", row_sum_keep.shape,
      "← keepdims 把被压的轴留成 1")


print("\n" + "=" * 50)
print("【4】布尔筛选")
print("=" * 50)
mask = m > 6
print("mask = m > 6 =\n", mask, "\n| shape:", mask.shape, "← 与原 m 同形")

filtered = m[mask]
print("m[mask] =", filtered,
      "| shape:", filtered.shape, "← 布尔筛选永远返回 1 维")


print("\n" + "=" * 50)
print("【5】切片：视图 vs 副本")
print("=" * 50)
sub_view = m[0:2, 1:3]                 # 切片是视图
print("sub_view  =\n", sub_view, "\n| shape:", sub_view.shape,
      "| ndim:", sub_view.ndim)

sub_view[0, 0] = 999                   # 改视图
print("改视图后 m =\n", m, "← 原数组也被改了，说明是视图")

# 重新拿干净数据演示 copy
m2 = np.arange(1, 13).reshape(3, 4)
sub_copy = m2[0:2, 1:3].copy()
sub_copy[0, 0] = 888
print("\nsub_copy  =\n", sub_copy, "\n| shape:", sub_copy.shape)
print("改副本后 m2 =\n", m2, "← 原数组没变，说明是副本")
```


# NumPy 学习笔记：数组加法与 reshape

## 1. Python 列表加法与 NumPy 数组加法

**Python 列表使用 `+` 时，执行的是列表拼接；NumPy 数组使用 `+` 时，通常执行的是对应位置元素相加。**

### 代码示例

```python
import numpy as np

# Python 列表加法
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)
# 输出：[1, 2, 3, 4, 5, 6]

# NumPy 数组加法
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print(A + B)
# 输出：[5 7 9]
```

### 我的理解

* Python 列表的 `+` 是把两个列表连接起来，元素数量增加。
* NumPy 数组的 `+` 是把对应位置的元素相加，例如 `1+4=5`。
* NumPy 数组进行这种加法时，形状需要兼容。如果形状不相同，有时可以通过广播机制完成计算。

## 2. 为什么 reshape 不会改变元素总数？

**`reshape()` 的作用是改变数组的形状，而不是增加或删除元素。**

### 代码示例

```python
A = np.array([1, 2, 3, 4, 5, 6])

print(A.shape)
# (6,)

B = A.reshape(2, 3)

print(B)
# [[1 2 3]
#  [4 5 6]]

print(B.shape)
# (2, 3)

C = A.reshape(3, 2)

print(C.shape)
# (3, 2)
```

### 我的理解

* 原数组 `A` 有 6 个元素，形状为 `(6,)`。
* `reshape(2,3)` 把 6 个元素排列成 2 行 3 列。
* `reshape(3,2)` 把 6 个元素排列成 3 行 2 列。
* 虽然数组形状改变了，但元素数量始终是 6。
* `reshape` 要求新形状的各维度大小相乘等于原数组元素总数（使用 `-1` 自动推断维度时也必须满足这个条件）。

例如：

* `reshape(2,3)`：2 × 3 = 6，可以。
* `reshape(3,2)`：3 × 2 = 6，可以。
* `reshape(2,4)`：2 × 4 = 8，不可以，会报错。

## 3. 今日总结

今天我理解了 Python 列表和 NumPy 数组在加法运算上的区别，也知道了 `reshape()` 只能改变数组的形状，不能改变元素总数。

以后使用 NumPy 时，我需要先观察数组的 `shape`，再决定如何进行计算或变形。
