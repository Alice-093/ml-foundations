# Day 03 - Python 函数与模块基础

## 1. 函数定义 (def) 与 返回值 (return)

### 1.1 基本概念
def 用于定义函数，将一段可复用的逻辑封装起来。
return 用于将函数执行的结果返回给调用者，并立即结束当前函数的执行。
如果函数中没有 return，或者只写了 return，默认返回 None。
函数可以返回多个值（本质上返回的是一个元组 tuple）。

### 1.2 常用操作
使用 def 函数名(参数): 定义

使用 return 结果 返回数据

使用变量接收返回值

无返回值时，调用者得到 None

### 1.3 示例
```python
# 定义函数
def calculate_total_score(math, english):
    total = math + english
    return total # 返回计算结果，函数在此结束

# 调用函数并接收返回值
student_total = calculate_total_score(95, 88)
print(f"总分: {student_total}") # 输出: 总分: 183

# 返回多个值的情况 (实际上返回的是一个元组)
def get_student_info(name, score):
    level = "优秀" if score >= 90 else "良好"
    return name, score, level # 返回多个值

info = get_student_info("Alice", 95)
print(info) # 输出: ('Alice', 95, '优秀')

# 可以用解包的方式接收
s_name, s_score, s_level = get_student_info("Bob", 85)
print(s_name, s_score) # 输出: Bob 85
```
### 1.4 与 C++ 的区别
返回值类型：C++ 必须在函数声明时指定返回类型（如 int func()），且只能返回一个值（除非用 std::tuple 或结构体）。Python 是动态类型，不需要声明类型，且可以直接 return a, b, c 返回多个值。

返回机制：C++ 的 return 会进行拷贝/移动构造，Python 的 return 返回的是对象的引用。

### 1.5 今天遇到的问题
问题：定义函数时，如果不写 return 会怎样？
解决：如果不写 return，Python 会隐式返回 None。在调用时如果用变量接收，会得到 None。在写有分支的函数时，一定要确保所有分支都有 return，否则可能会意外得到 None。

## 2. 函数参数进阶（默认参数与可变参数）
### 2.1 基本概念
默认参数：在定义函数时给参数指定一个默认值。调用时如果不传该参数，就使用默认值。

可变参数：

*args：接收任意数量的位置参数，打包成一个元组 (tuple)。

**kwargs：接收任意数量的关键字参数，打包成一个字典 (dict)。

### 2.2 常用操作
定义默认参数：def func(a, b=10):

传入可变位置参数：func(1, 2, 3)

传入可变关键字参数：func(name="Alice", age=18)

解包操作：func(*list) 或 func(**dict)

### 2.3 示例
```python
# 默认参数：必须放在非默认参数之后
def print_score(name, score, passing_line=60):
    status = "及格" if score >= passing_line else "不及格"
    print(f"{name}的成绩是{score}，状态：{status}")

print_score("Alice", 75)            # 使用默认的及格线60 -> Alice的成绩是75，状态：及格
print_score("Bob", 50, passing_line=55) # 修改默认参数 -> Bob的成绩是50，状态：不及格

# 可变参数 *args (位置参数)
def sum_scores(*args):
    print(f"接收到的参数类型: {type(args)}") # <class 'tuple'>
    return sum(args)
print(sum_scores(80, 90, 100)) # 输出 270

# 可变参数 **kwargs (关键字参数)
def build_profile(name, **kwargs):
    print(f"接收到的参数类型: {type(kwargs)}") # <class 'dict'>
    profile = {"name": name}
    profile.update(kwargs) # 将kwargs字典合并进去
    return profile
print(build_profile("Alice", age=18, major="CS")) 
# 输出: {'name': 'Alice', 'age': 18, 'major': 'CS'}
```
### 2.4 与 C++ 的区别
默认参数：C++ 允许默认参数，但必须从右向左连续定义。Python 同样要求默认参数必须放在非默认参数后面。

可变参数：C++ 传统上使用 ... (va_list) 或 `std::initializer_list`，相对复杂。Python 的 `*args` 和 `**kwargs` 语法极其简洁，且直接打包成内置的 tuple 和 dict。

传参方式：C++ 有值传递、引用传递、指针传递。Python 只有“传对象引用”，对于不可变对象（如 int、str）函数内修改不影响外部，对于可变对象（如 list、dict）函数内修改会影响外部。

### 2.5 今天遇到的问题
问题：为什么 *args 必须写在 **kwargs 前面？如果默认参数放在普通参数前面会怎样？
解决：Python 规定参数的顺序必须是：位置参数 -> 默认参数 -> *args -> **kwargs。
如果默认参数放在普通参数前面（例如 def func(a=1, b)），Python 无法判断调用 func(2) 时，2 是传给 a 还是 b，会直接报语法错误（SyntaxError）。

## 3. 模块导入 (import)
### 3.1 基本概念
import 用于将其他 Python 文件（模块）或内置库引入到当前脚本中，以使用其中的函数、类或变量。可以将模块理解为 C++ 中的头文件或命名空间。

### 3.2 常用操作
import 模块名：导入整个模块，使用时需加 模块名.

from 模块名 import 函数名：导入特定函数，直接使用函数名

import 模块名 as 别名：给模块起别名（常用于第三方库，如 import numpy as np）

from 模块名 import *：导入模块中所有公开的名称（不推荐，容易引起命名冲突）

### 3.3 示例
```python
import math # 导入整个模块
print(math.sqrt(16)) # 输出 4.0

from math import pi, pow # 导入特定属性/函数
print(pi) # 输出 3.141592653589793
print(pow(2, 3)) # 输出 8.0

import random as rd # 给模块起别名
print(rd.randint(1, 10)) # 输出 1到10之间的随机整数
```
### 3.4 与 C++ 的区别
C++ 使用 `#include <iostream>`，在预处理阶段将文件内容直接复制粘贴到源文件中，容易导致编译时间变长和符号冲突。

Python 的 import 是在运行时执行的。导入时，Python 会执行模块顶层的代码，并创建一个模块对象（命名空间）。Python 有模块缓存机制（sys.modules），多次导入同一模块不会重复执行。

### 3.5 今天遇到的问题
问题：import math 和 from math import sqrt 有什么区别？
解决：import math 会将整个 math 模块加载，并绑定名字 math 到当前命名空间，调用时需写 math.sqrt()。from math import sqrt 只把 sqrt 这个函数绑定到当前命名空间，调用时直接写 sqrt()。后者更简洁，但如果函数名和当前文件里的变量重名，会发生覆盖（冲突）。

## 4. 程序入口 (if __name__ == "__main__":)
### 4.1 基本概念
在 Python 中，一个 .py 文件既可以被直接运行，也可以被当作模块导入到其他文件中。

当文件被直接运行时，Python 解释器会将该文件的 __name__ 属性设为 "__main__"。

当文件被作为模块导入时，__name__ 属性会被设为该文件的模块名（即文件名去掉 .py）。
if __name__ == "__main__": 用于判断当前脚本是否是被直接运行的。它相当于 C++ 中的 int main() 函数。

### 4.2 常用操作
将测试代码、主执行逻辑放在这个判断语句下面

避免在被导入时执行不必要的代码

### 4.3 示例
创建一个名为 score_utils.py 的文件：

```python
# score_utils.py
def get_level(score):
    if score >= 90:
        return "优秀"
    return "合格"

# 测试代码放在这里
if __name__ == "__main__":
    # 只有直接运行 python score_utils.py 时，以下代码才会执行
    print("这是作为主程序运行，开始测试...")
    print(get_level(95)) 
如果在另一个文件 main.py 中导入：

python
# main.py
import score_utils
# 此时不会打印 "这是作为主程序运行..."，因为 score_utils 的 __name__ 是 "score_utils"，不是 "__main__"
print(score_utils.get_level(85)) 
```
### 4.4 与 C++ 的区别
C++ 编译时会寻找 main() 函数作为唯一入口。

Python 没有强制规定的入口。if __name__ == "__main__": 只是一个约定俗成的惯用法。如果不写这个判断，模块被导入时，顶层的测试代码也会被执行。

### 4.5 今天遇到的问题
问题：为什么我写好了一个工具函数，别人导入我的模块后，我的测试代码也跑起来了？
解决：因为测试代码写在了全局作用域。解决办法是把所有的测试逻辑封装在一个 main() 函数里，然后使用 if __name__ == "__main__": main() 来调用。这样不仅逻辑清晰，还能防止模块被导入时产生副作用。


## 5输入验证与异常处理

### 5.1 核心概念

- 输入验证：检查函数参数是否符合要求。
- raise：主动抛出异常。
- try/except：捕获并处理异常。

### 5.2 常见异常

| 异常 | 含义 |
|---|---|
| ValueError | 参数的值不符合要求 |
| TypeError | 数据类型不符合要求 |
| ZeroDivisionError | 除以零 |

### 5.3. 关键语法

#### 5.3.1判断空列表

```python
if not nums:
    raise ValueError("列表不能为空")
```

#### 5.3.2判断输入类型

```python
if not isinstance(num, (int, float)):
    raise TypeError("元素必须是数字")
```

#### 5.3.3捕获异常

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(e)
```

### 5.4 我的理解和易错点

- raise 和 except 的作用不同。
- return 是返回正常结果，raise 是报告异常。
- 不要把所有报错都直接忽略。
- 不同函数对空列表的处理可以不同。

# Day 03 输入错误处理实践总结

本次在 `stats_utils.py` 中为统计函数增加了输入验证，并通过 `day03_use_module.py` 测试。

**实际测试结果：**

* `mean([])`：成功抛出 `ValueError`。
* `mean([1, "abc", 3])`：成功抛出 `TypeError`。
* `mean([1, 2, 3, 4, 5])`：返回 `3.0`。
* `variance([1, 2, 3, 4, 5])`：返回 `2.0`。
* `count_above([1, 2, 3, 4, 5], 3)`：返回 `2`。

**我的理解：**

1. `raise` 用于主动报告输入错误。
2. `try/except` 用于捕获和处理指定异常。
3. `isinstance()` 可以检查变量类型。
4. `return` 用于返回正常计算结果，`raise` 则会中断当前正常执行流程。
5. 方差函数通过调用平均值函数，复用了已有的输入验证逻辑。
6. 异常测试得到预期的错误提示，也属于测试成功。

**还需要注意：**

输入验证应该根据函数的数学意义设计，例如空列表无法计算平均值，但统计满足条件的元素数量时可以返回 0。
count_above([] , 3) 返回 0 是合理的；但 mean([]) 抛出异常也是合理的。
