
# Day 04 - 文件与路径

## 1. 绝对路径和相对路径
- 定义及区别
绝对路径，是明确指出文件在电脑中的位置。
相对路径，是对于"当前工作目录"的路径
- Windows 路径示例
比如 CSV 文件最终保存在`D:\AI_Learning\ml-foundations\data\students.csv`，这是绝对路径
如果项目根目录执行程序，也可以使用：`"data/students.csv"`，这是相对路径，要结合当前工作目录才能确定文件位置

## 2. 项目根目录与当前工作目录
- 什么是项目根目录
整个项目最外层的那个文件夹，

- Path.cwd() 的作用
运行 python 命令时，终端所在的目录，即当前工作目录。是运行时决定的，你在不同目录运行同一个脚本，它的值就不同。调试路径问题时第一件事就是 print(Path.cwd())，看看 Python 到底从哪开始找文件。

- __file__ 的作用
当前这个 .py 文件在硬盘上的真实路径，Path(__file__).resolve() 获取当前 Python 文件的绝对路径。

## 3. pathlib.Path
- Path() 创建路径对象
把字符串路径包成一个 Path 对象，可以使用path的各种方法

- / 拼接路径
用 / 把文件夹名和文件名拼起来，像写普通路径一样自然。自动处理 Windows 和 Mac/Linux 的分隔符差异。
比如`p = Path("data") / "raw" / "input.csv"`

- .exists() 检查文件是否存在
返回 True 或 False，判断路径是否存在（文件或目录都算）
```python
if Path("data/raw/input.csv").exists():
    print("文件在！")
else:
    print("文件不在！")
```
- .parent 获取上一级目录
```python
p = Path("/home/alice/my_project/data/raw/input.csv")
print(p.parent)    # /home/alice/my_project/data/raw
print(p.parent.parent)  # /home/alice/my_project/data
```

## 4. with open 文件操作
open() 的三个核心参数
open(file, mode, encoding)
file:     文件路径（字符串或 Path 对象）
mode:     打开模式（见下面）
encoding: 编码方式（文本文件必填，推荐 UTF-8）

- r：读取
'r' = read      读取，文件不存在会报错

- w：写入
'w' = write     写入，文件存在就清空重写，不存在就创建

- a：追加
'a' = append    追加，在文件末尾写，不存在就创建

- with 的作用
```python
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
```
当代码执行到 with 块外面时，Python 自动调用 f.close()
即使 with 块里面报错了，文件也会被正确关闭

## 5. UTF-8 编码
- 为什么读取文本需要指定编码
计算机只认 0 和 1，文字要变成 0/1 需要编码
UTF-8 是目前全球通用的编码，能表示所有语言的字符

- encoding="utf-8"
如果不指定 encoding 会怎样？ 
```python
with open("hello.txt", "r") as f:  # 没指定 encoding
     content = f.read()
```
Windows 上默认用 GBK 编码去读
如果文件是 UTF-8 写的，中文就会乱码或报错

二进制模式（'rb', 'wb'）不涉及文字，不需要编码

## 6. 易错点与个人理解
CSV 文件读写常用模板
```python
import csv
from pathlib import Path

path = Path("data/students.csv")

# 写入 CSV
with path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f, fieldnames=["name", "score"]
    )
    writer.writeheader()
    writer.writerows(records)

# 读取 CSV
with path.open("r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)
```
易错点：

writerows() 接收一个包含多条记录的可迭代对象，而不是多个独立字典参数。

DictReader() 读取 CSV 时，字段值通常是字符串，需要按用途转换类型。

"w" 模式会覆盖文件原有内容；相对路径则取决于当前工作目录。