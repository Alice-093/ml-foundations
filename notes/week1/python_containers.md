
# Day 02 - Python 容器

## 1. 字典（dict）

### 1.1 基本概念

字典通过 key 查找对应的 value。可以把字典理解为 键值对 的集合，但字典的键必须是唯一的。
键值映射、可修改。常见用途：存储学生信息

### 1.2 常用操作

- 创建字典
- 通过 key 获取 value
- 添加、修改和删除元素
- 遍历 keys、values、items
- 根据 value 排序

### 1.3 示例（以1.2中常用操作为例）

```python
student = {'Alice': 100,'Bob': 96,'Pho': 34,'Scut': 0,'Python': 88,'C++':67,'Java':83}# 创建字典

print(student['Alice'])
print(student.get('Alice'))# 通过 key 获取 value，若 key 不存在，使用get（） 返回 None 不会报错中断

student['Mike']=90# 添加

student['C++']=97# 修改

del student['Scut']# 删除

for key in student.keys()# 遍历键
    print(key)

for value in student.values()# 遍历值
    print(value)

for key,value in student.items()# 遍历键和值
    print(f"{key}:{value}")

sorted_students = sorted(
    student.items(),# 要排序的数据
    key=lambda item: item[1],# lambda 就是用来定义一个简单的匿名函数
    reverse=True# reverse=True：降序，即从大到小；默认 False 为升序
)
print("排序结果:", sorted_student)
#这里 sorted() 返回的是元组组成的列表，并不是字典。如果希望得到保留这个排序顺序的字典，可以使用 dict(sorted_scores)
```

### 1.4 与 C++ 的区别

Python dict 和 C++ map 都可以通过键查找值，
但 C++ std::map 默认按键排序，
Python dict 保留插入顺序。

### 1.5 今天遇到的问题

问题：如何按照学生分数进行排序？

解决：使用 sorted() 的 key 参数指定排序依据。两种情况，一种是对字典列表排序，另一种是对字典排序。实例中的代码演示的是对字典排序


## 2.列表（list）

### 2.1 基本概念

有序、可修改。类似于Vector可变数组。常用于：存储学生列表

### 2.2 常见操作

- 创建列表
- 增删改查
- 计数
- 排序,翻转
- 遍历

### 2.3 示例
```python
# 创建列表
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruit_1 = ['cherry','peach']
lst=list()

# 增加元素
fruits.append('grape')# 在列表末尾添加元素
fruits.insert(0,'watermelon')# 在索引 0 处插入元素
fruits.extend(fruit_1)# 要求参数是**可迭代对象**（列表、元组、字符串、字典等都可以），它会遍历并逐个加入

# 删除元素
fruits.remove('apple') # 删除首次出现的那个指定元素
fruits.pop（）
# 移除列表中给定位置上的元素，并返回该元素，若未指定索引号，则 fruits.pop() 将移除并返回列表中最后一个元素
fruits.clear() #移除列表中的所有项,类似于 del fruits[:]

# 修改元素
fruits[0]='cherry'

# 查找元素
fruits[0] # 列表中首个元素
fruits.index('apple')# 返回列表中 apple 首次出现所在的从零开始的索引

# 计数
fruits.count('apple')# 返回列表中 apple 出现的次数

# 排序,翻转
fruits.sort()# 原地排序列表中的元素，默认升序
fruits.reverse() #翻转列表中的元素

# 遍历
for fruit in fruits:
    print(fruit)
```

### 2.4 和C++的区别
Python 的 list 约等于 C++ 的 vector，但更灵活（可存不同类型），牺牲了部分性能。



## 3.元组 (tuple)

### 3.1 基本概念
有序、不可修改（不可变）。类似于C++中的常量数组/元组。常用于：固定配置、函数多返回值、字典的键。

### 3.2 常见操作
- 创建元组
- 查找、计数、切片（不支持增删改）
- 遍历
- 拼接（生成新元组）

### 3.3 示例
```python
# 创建元组
fruits = ('orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana')
fruit_1 = ('cherry', 'peach')
t = tuple() # 空元组
t_single = ('single',) # 单元素元组，必须加逗号

# 可通过拼接生成新元组：
fruits = fruits + fruit_1

# 查找元素
fruits[0] # 元组中首个元素
fruits.index('apple') # 返回元组中 'apple' 首次出现所在的从零开始的索引
fruits[1:4] # 切片查找，返回新元组

# 计数
fruits.count('apple') # 返回元组中 'apple' 出现的次数

# 排序、翻转（不支持原地，可用内置函数返回新对象）
sorted(fruits) # 返回排序后的新列表
fruits[::-1] # 翻转，返回新元组

# 遍历
for fruit in fruits:
print(fruit)
```

### 3.4 和C++的区别
Python元组不可变，类比C++的 `std::tuple` 或 `const std::vector`；C++数组/Vector默认可变，Python列表更像 `std::vector`。


## 4.集合 (set)

### 4.1 基本概念
无序、不重复、可变（但元素必须不可变）。类似于C++中的 `unordered_set`。常用于：去重、集合运算（交集/并集/差集）。

### 4.2 常见操作
- 创建集合
- 增删元素
- 查找（成员判断）
- 集合运算（交并差）
- 遍历（无序）

### 4.3 示例
```python
# 创建集合
fruits = {'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'} # 自动去重
fruit_1 = {'cherry', 'peach'}
s = set() # 空集合（注意：{} 是字典）

# 增加元素
fruits.add('grape') # 添加单个元素
fruits.update(fruit_1) # 批量添加（参数需为可迭代对象）

# 删除元素
fruits.remove('apple') # 删除指定元素，不存在会报错
fruits.discard('apple') # 删除指定元素，不存在不报错
fruits.pop() # 随机移除并返回一个元素（因无序，不可指定索引）
fruits.clear() # 移除集合中的所有元素

# 修改元素（无直接修改，需先删后加）

# 查找元素（主要用于成员判断）
'apple' in fruits # 返回 True/False
fruits[0] # 报错，集合无序，不支持索引和切片

# 计数（无 count 方法，因元素天然唯一）
len(fruits) # 返回元素个数

# 排序、翻转（无序，无原生排序；可转列表排序）
sorted(fruits) # 返回排序后的列表

# 集合运算
fruits & fruit_1 # 交集
fruits | fruit_1 # 并集
fruits - fruit_1 # 差集，存在于 fruits 中但不存在于 fruit_1 中的字母
fruits ^ fruit_1 # 对称差集，存在于 fruits 或 fruit_1 中但非两者中皆有的字母

# 遍历
for fruit in fruits:
print(fruit)
```
### 4.4 和C++的区别
Python集合无序且自动去重，直接对应C++ `std::unordered_set`（底层哈希表）；C++ `set` 是有序红黑树，Python无内置有序集合（需用 `frozenset` 或第三方库）。Python集合运算符（`& | -`）比C++更直观。

## 5.for循环
### 5.1 基本概念
用于遍历序列（列表、元组、字符串、字典、集合等）
语法简洁，不需要下标变量
类似 C++ 的 范围 for（range-based for）

### 5.2 常见操作
遍历列表 / 元组 / 字符串
配合 range() 使用
遍历字典（keys / values / items）
break / continue / else 子句

### 5.3 示例
```python
# 遍历列表
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# 使用 range()
for i in range(5):        # 0 1 2 3 4
    print(i)

for i in range(1, 5):     # 1 2 3 4
    print(i)

for i in range(0, 10, 2): # 0 2 4 6 8
    print(i)

# 遍历字典
student = {'Alice': 100, 'Bob': 96}

for key in student:           # 默认遍历 key
    print(key)

for key, value in student.items():
    print(key, value)

# break 和 continue
for i in range(5):
    if i == 3:
        break
    print(i)

# for-else 结构
for i in range(3):
    print(i)
else:
    print("循环正常结束（未被 break）")
```
### 5.4 和 C++ 的区别
Python 的 for 基本等于 C++ 的 范围 for，但更简洁，且自带 else 语法

## 6. 切片（slice）
### 6.1 基本概念
用于从序列中截取子序列
适用于：列表、元组、字符串
语法：seq[start:stop:step]
左闭右开：包含 start，不包含 stop

### 6.2 常见操作
基本切片
步长切片
负数索引 / 负数步长
切片赋值（仅列表）

### 6.3 示例
```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 基本切片
lst[2:5]     # [2, 3, 4]
lst[:3]      # [0, 1, 2]
lst[5:]      # [5, 6, 7, 8, 9]
lst[:]       # 完整拷贝

# 步长
lst[::2]     # [0, 2, 4, 6, 8]
lst[1::2]    # [1, 3, 5, 7, 9]

# 负数索引
lst[-3:]     # [7, 8, 9]
lst[:-2]     # [0, 1, 2, 3, 4, 5, 6, 7]

# 负数步长（翻转）
lst[::-1]    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 切片赋值（仅列表支持）
lst[2:5] = [20, 30]
# lst → [0, 1, 20, 30, 5, 6, 7, 8, 9]

# 字符串切片
s = "HelloWorld"
s[0:5]       # "Hello"
s[::-1]      # "dlroWolleH"
```
### 6.4 和 C++ 的区别
Python 切片是极其高效、可读性极强的语法糖，C++ 没有对等原生功能，需要用迭代器或算法模拟。切片一定要记住：左闭右开 + 步长可负


## 易错点与尚未熟练的知识

### 1. 排序操作（重点复习）

**（1）普通列表排序**

对于数字列表 `scores = [85, 92, 78]`：

* `sorted(scores)`：升序排序，返回一个新列表。
* `sorted(scores, reverse=True)`：降序排序，返回一个新列表。
* `scores.sort()`：直接修改原列表，返回值为 `None`。
* `scores.sort(reverse=True)`：直接将原列表降序排列。

需要记住：`sorted()` 不修改原列表，`list.sort()` 修改原列表。

**（2）字典按照 value 排序**

例如：`scores = {"Alice": 85, "Bob": 92, "Charlie": 78}`

可以使用：

`sorted(scores.items(), key=lambda item: item[1], reverse=True)`

理解：

* `scores.items()` 提供字典中的键值对。
* `item[0]` 是姓名（key）。
* `item[1]` 是分数（value）。
* `key` 指定排序依据。
* `reverse=True` 表示降序。

注意：排序结果是由元组组成的列表，不是原来的字典。

**（3）字典列表按照指定字段排序（重点）**

例如，一个列表中存储多个学生字典，每个学生有 `"name"` 和 `"score"` 两个字段。

按照分数降序排序：

`sorted_students = sorted(students, key=lambda student: student["score"], reverse=True)`

理解：

* `students` 是整个学生列表。
* `student` 表示列表中的一个学生字典。
* `student["score"]` 获取该学生的分数。
* `lambda student: student["score"]` 指定排序使用的值。
* `sorted_students` 保存排序后的新列表。

**需要进一步理解：** `lambda` 的作用、`key` 为什么接收一个函数、`sorted()` 与 `sort()` 的区别。

### 2. print() 输出（重点复习）

目前会使用基础的 `print()`，还需要熟悉下面几种方式。

**（1）多个值输出**

`print("最高分为", highest_score)`

Python 默认使用空格分隔多个参数。

**（2）f-string 格式化输出**

`print(f"最高分为 {highest_score}")`

在字符串前添加 `f`，就可以在 `{}` 中使用变量或表达式。

**（3）控制小数位数**

`print(f"平均分为 {average_score:.2f}")`

其中 `:.2f` 表示以固定小数格式保留两位小数。例如，84.375 会显示成 84.38。

**（4）循环输出字典列表**

`for student in sorted_students:` 表示依次取出排序后的学生。

循环内部使用 `print(student["name"], student["score"])`，可以每行打印一名学生的姓名和分数。

**（5）换行和分隔符**

* `print()` 默认在末尾换行。
* `print("A", "B", sep="-")` 输出 `A-B`。
* `print("Hello", end=" ")` 可以把末尾的换行改为空格。

当前优先掌握普通输出、f-string 和循环输出，不需要深入复杂的格式控制。

### 3. 区分列表和字典（今天实际遇到过）

`students` 是包含多个字典的列表，`student` 是循环中单个学生的字典。

* `students[0]`：获取第一个学生字典。
* `students[0]["score"]`：获取第一个学生的分数。
* `students["score"]`：错误，不能用字符串作为列表索引。
* `student["score"]`：在遍历学生字典时获取当前学生的分数。

注意区分整体数据和单个元素。

### 4. for 循环与生成器表达式

今天计算平均分时使用了：

`sum(student["score"] for student in students)`

意思是遍历 `students` 中的每个 `student`，取出其分数，并通过 `sum()` 求和。

需要理解：

* `for student in students`：遍历整个学生列表。
* `student["score"]`：取得当前学生的分数。
* `sum()`：将得到的分数相加。
* `len(students)`：取得学生数量。

生成器表达式可以让简单的计算更加简洁，但应先掌握普通 `for` 循环，再练习简写。

### 5. lambda 匿名函数

例如：

`lambda student: student["score"]`

可以理解为一个接收 `student` 参数、返回 `student["score"]` 的简单函数。

与普通的 `def` 函数相比，`lambda` 适合编写简短、一次性使用的函数。

需要注意：`key=lambda ...` 传入的是一个函数，不能直接将其理解为把分数传给 `key`。

### 6. return 和 print() 的区别

* `return`：将函数的计算结果返回给调用者。
* `print()`：将内容显示在终端中。

例如，`calculate_average(students)` 使用 `return` 返回平均分，再由外部的 `print()` 输出结果。

函数通常负责计算，输出语句负责展示。不能将两者完全等同。

### 7. 变量与字典键名必须准确

今天出现过的错误：

* `stduents` 与 `students` 拼写不同，可能造成 `NameError`。
* `student["scorw"]` 与 `student["score"]` 不同，可能造成 `KeyError`。
* 对列表使用字符串索引，可能造成 `TypeError`。

遇到报错时，先看 Traceback 的最后一行，再检查对应文件、行号和变量类型。

### 8. 边界情况（后续需要掌握）

当前练习使用的是非空学生列表，后续还要考虑：

* 如果学生列表为空，`total / len(students)` 会出现除零错误。
* 如果学生列表为空，`students[0]` 会出现索引错误。
* 如果某个学生缺少 `"score"` 字段，直接访问可能出现 `KeyError`。

目前只需要知道这些情况可能导致错误，不要求今天就实现完整的异常处理。

---

## 今日总结

已经能够使用字典列表保存学生信息，通过函数计算平均分、最高分和及格人数，并按照成绩排序。

接下来需要重点巩固：

1. 普通列表、字典、字典列表的不同排序方法。
2. `sorted()` 中 `key` 和 `lambda` 的含义。
3. `print()` 的 f-string 格式化输出。
4. 列表与字典的访问方式。
5. `for` 循环与生成器表达式之间的关系。

**学习原则：** 对于尚未掌握的语法，先使用简单例子理解，再尝试不看笔记独立写出来。
