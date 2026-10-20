# Python 调试日志

## Day 02｜2026-10-13

**练习文件：** `python_basics/day02_containers.py`

**运行命令：**

`python python_basics/day02_containers.py`

### 错误 1：NameError

**错误信息：**

`NameError: name 'stduents' is not defined`

**原因：**

调用函数时，把变量 `students` 错写成了 `stduents`。Python 变量名必须与定义时一致。

**解决方法：**

将 `calculate_average(stduents)` 修改为 `calculate_average(students)`。

### 错误 2：TypeError

**错误信息：**

`TypeError: list indices must be integers or slices, not str`

**错误代码：**

`sum(students["score"] for student in students)`

**原因：**

`students` 是列表，不能直接使用字符串 `"score"` 作为索引。`for student in students` 中的 `student` 才是单个学生字典。

**解决方法：**

`sum(student["score"] for student in students)`

**理解：**

* `students`：整个学生列表。
* `student`：循环中的单个学生字典。
* `student["score"]`：读取当前学生的成绩。

### 错误 3：KeyError（代码检查中发现）

**问题代码：**

`student["scorw"]`

**原因：**

字典实际使用的键是 `"score"`，拼写不一致会导致 `KeyError`。

**解决方法：**

修改为 `student["score"]`。

### 其他问题

排序结果已经保存在 `sorted_students` 中，但还需要使用 `print()` 或 `for` 循环输出。

### 本次学习总结

1. 阅读 Traceback 时，先看最后一行的错误类型，再根据文件行号定位。
2. 区分列表 `students` 与列表中的单个字典 `student`。
3. 访问字典时，键名必须准确。
4. 计算结果正确保存到变量后，还需要根据任务要求输出。

### 运行验证

* [x] 修正变量拼写错误
* [x] 修正列表与字典索引错误
* [x] 修正字典键名拼写错误
* [x] 平均分：84.375
* [x] 最高分：100
* [x] 成绩排序：正确（降序）
* [x] 及格人数：8

**运行命令：**

`python python_basics/day02_containers.py`

**最终状态：** 已成功运行，四项统计结果正确，无报错。

**调试收获：** 学会通过 Traceback 定位错误，理解了列表与字典的区别，以及变量名和字典键名拼写准确的重要性。


## Day 03｜2026-10-14 函数、模块与异常处理

**涉及文件：**

* `python_basics/stats_utils.py`
* `python_basics/day03_use_module.py`

**运行命令：**

`python python_basics/day03_use_module.py`

### 一、实际遇到的错误

#### 1. NameError：函数未定义

**报错信息：**

`NameError: name 'mean' is not defined`

**问题代码：**

`means_num = mean(numbers)`

**原因：**

使用 `import stats_utils` 导入模块后，不能直接通过 `mean()` 调用模块中的函数。

**解决方法：**

修改为：

`means_num = stats_utils.mean(numbers)`

**收获：**

使用 `import 模块名` 时，需要通过 `模块名.函数名()` 调用函数。

#### 2. AttributeError：模块中找不到函数

**报错信息：**

`AttributeError: module 'stats_utils' has no attribute 'mean'`

**出现位置：**

`stats_utils.mean(numbers)`

**分析：**

Python 当时加载的 `stats_utils` 模块中没有找到 `mean` 属性。

可能与文件未保存、函数定义或导入模块的位置有关，但目前没有确认具体原因。

**最终结果：**

后续重新运行时，`stats_utils.mean()` 已能够正常调用，问题已消失。

**收获：**

遇到 `AttributeError` 时，应检查模块中的函数名称、文件保存状态，以及实际导入的是哪个模块。

### 二、主动进行的异常测试

本次使用 `raise` 抛出异常，通过 `try/except` 捕获异常，验证输入检查是否正常工作。

| 测试输入                          | 预期异常       | 实际结果 |
| ----------------------------- | ---------- | ---- |
| `mean([])`                    | ValueError | 成功捕获 |
| `mean([1, "abc", 3])`         | TypeError  | 成功捕获 |
| `count_above([1,2,3], "2")`   | TypeError  | 成功捕获 |
| `count_above([1,2,"abc"], 2)` | TypeError  | 成功捕获 |

**结论：**

四组异常测试均得到预期的错误提示，程序继续正常执行。

### 三、正常输入验证

测试数据：`[1, 2, 3, 4, 5]`

* 平均值：3.0
* 总体方差：2.0
* 严格大于平均值的元素数量：2

三项结果均符合预期。

### 四、本次调试总结

1. `NameError` 通常与变量或函数名未定义有关。
2. `AttributeError` 表示对象中找不到指定属性或方法。
3. `raise` 用于主动报告异常，`try/except` 用于捕获和处理异常。
4. 主动触发预期异常属于正常的测试过程，不代表程序出现 Bug。
5. 修改代码后，需要重新运行程序，确认问题是否真正解决。

**最终状态：** 代码运行成功，统计结果正确，四组异常测试通过。




### Day 04｜文件路径错误

**涉及文件：** `python_basics/day04_csv.py`

**问题位置：**

`csv_path = Path("date/students.csv")`

**原因分析：**

项目实际使用的文件夹名称是 `data`，但代码中误写为 `date`。

`Path.open("w")` 可以创建新文件，但不会自动创建不存在的父文件夹。

**解决方法：**

将路径修改为：

`csv_path = Path("data/students.csv")`

**学到的知识：**

1. 相对路径会基于当前工作目录解析。
2. 文件路径和文件夹名称必须准确。
3. `"w"` 模式可以创建文件，但不能自动创建父目录。
4. 遇到文件路径问题，可以使用 `Path.cwd()`、`Path.resolve()` 和 `Path.exists()` 辅助排查。

**验证状态：** 修改路径后重新运行成功。

### 错误 2：TypeError（writerows 参数传递错误）

**错误信息：**

`TypeError: DictWriter.writerows() takes 2 positional arguments but 9 were given`

**原因：**

调用 `writerows()` 时，直接传入了 8 个独立字典，而该方法要求将多条记录作为一个可迭代对象传入。

**解决方法：**

把 8 个字典放入一个列表，再将列表传给 `writerows()`。

**学到的知识：**

* `writerow()`：写入一条记录，传入一个字典。
* `writerows()`：写入多条记录，通常传入字典列表。
* 函数参数之间的逗号与列表元素之间的逗号，虽然写法相似，但含义不同。

**验证状态：** 修复后重新运行成功。

# Day 04 - VS Code 断点调试

## 1. 调试目标

**日期：** 2026-10-15

**调试文件：** `python_basics/day04_csv.py`

**运行命令：**

`python python_basics/day04_csv.py`

本次主要学习使用 VS Code 的断点调试功能，观察 CSV 文件读取、数据类型转换以及循环执行的过程。

## 2. 断点位置

建议记录的主要断点：

```python
for row in reader:
    score = int(row["score"])
    students.append(score)
    print(row)
```

**设置断点的目的：**

* 观察 `row` 如何依次读取每个学生的数据。
* 检查 CSV 中的 `score` 是什么数据类型。
* 观察 `int()` 转换前后的区别。
* 观察 `students` 列表如何逐渐增加元素。

## 3. 观察的变量

以下是根据当前代码与 CSV 数据得到的预期变化。

| 变量             | 预期值或变化                              | 说明                   |
| -------------- | ----------------------------------- | -------------------- |
| `csv_path`     | `data/students.csv`                 | 保存 CSV 文件路径的 Path 对象 |
| `row`          | `{'name': 'Alice', 'score': '100'}` | 第一轮循环读取的字典           |
| `row["score"]` | `'100'`                             | 字符串类型 str            |
| `score`        | `100`                               | 通过 int() 转换后的整数      |
| `students`     | `[]` → `[100]` → `[100, 97]` ...    | 逐次保存读取到的成绩           |

需要注意：变量的显示结果与程序暂停的位置有关。例如，如果断点设置在 `score = int(row["score"])`，程序刚暂停时，这一行尚未执行，本轮的 `score` 可能还没有赋值。

## 4. 调试操作

本次学习的主要调试功能：

* **F5（Continue）：** 启动调试，或让暂停的程序继续运行。
* **F10（Step Over）：** 执行当前语句，不进入被调用函数内部。
* **F11（Step Into）：** 进入被调用的 Python 函数内部，观察其执行过程。
* **Variables 面板：** 查看当前作用域内变量的值。
* **断点（Breakpoint）：** 让程序执行到指定位置时暂停。

在循环中设置断点后，可以通过单步执行观察每一行代码的作用。

## 5. 本次调试中需要理解的现象

### （1）CSV 数据类型转换

使用 `csv.DictReader()` 读取 CSV 时，`row["score"]` 得到的是字符串。

例如：

`row["score"]` → `"100"`（str）

执行：

`score = int(row["score"])`

之后：

`score` → `100`（int）

因此，在调用统计函数之前，需要先将分数字符串转换成整数。

### （2）列表逐步变化

执行：

`students.append(score)`

会将当前学生的成绩添加到列表末尾。

随着循环进行，列表逐渐增加元素，最终包含 8 名学生的成绩。

### （3）函数调用

在程序后面调用：

`stats_utils.mean(students)`

可以使用调试器观察函数执行过程。如果通过 Step Into 进入 `mean()`，就能够进一步查看循环中 `total` 的变化以及函数最终的返回值。

## 6. 与 print() 调试的区别

**print() 调试：**

通过在代码中添加输出语句观察变量的值，简单直接，但需要修改代码，而且不方便检查复杂的执行过程。

**断点调试：**

可以让程序在指定位置暂停，通过 Variables 面板观察变量状态，并使用单步执行功能分析程序运行过程。

相较于大量添加 `print()`，断点调试更适合分析循环、函数调用和较复杂的代码。

## 7. 本次学习总结

1. 学习了 VS Code 中设置断点和启动调试的方法。
2. 理解了如何使用 Variables 面板查看变量。
3. 理解了单步执行可以帮助观察程序执行顺序。
4. 进一步理解了 CSV 读取过程中字符串与整数的区别。
5. 理解了通过断点可以观察列表在循环中逐渐变化的过程。

**调试结论：** `day04_csv.py` 已能够正常运行并完成 CSV 读写与成绩统计。通过断点调试，可以更清楚地理解数据在程序中的处理流程。

## Day 05｜NumPy数组入门
**涉及文件：numpy_labs/day05_arrays.py
**运行命令：python numpy_labs/day05_arrays.py

无报错，记录执行命令

## Day 06｜NumPy矩阵运算与广播
**涉及文件：numpy_labs/day06_matrix_ops.py
**运行命令：python numpy_labs/day06_matrix_ops.py

无报错，记录执行命令

## Day XX｜日期与学习主题

**涉及文件：
**运行命令：**

### 1. 遇到的错误

**错误信息：**

**出错位置：**

**原因分析：**

**解决方法：**

**修复结果：**

### 2. 学到的知识

用自己的话总结 1～3 句话。