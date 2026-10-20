import csv

import stats_utils

from pathlib import Path

csv_path = Path("data/students.csv")

with csv_path.open("w",newline="",encoding= "utf-8") as f:
#"w",以写入模式打开文件，文件存在时会清空原内容
#newline="",让 CSV 模块自行处理换行
#encoding="utf-8",使用 UTF-8 编码
    writer = csv.DictWriter(#csv.DictWriter(),将字典格式的数据写入 CSV
        f,
        fieldnames=["name","score"]#写入列名
    )
    writer.writeheader()
    writer.writerows([{"name":"Alice","score":100},
                     {"name":"Bob","score":97},
                     {"name":"Jelly","score":85},
                     {"name":"Mike","score":67},
                     {"name":"Char","score":78},
                     {"name":"Ray","score":93},
                     {"name":"Smith","score":12},
                     {"name":"PaPa","score":59}]
                     )#writerow(),写入一条记录
    #writerows(),写入多个字典组成的可迭代对象

students = list()

with csv_path.open("r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
#从 CSV 读取出来的分数，默认是字符串，而不是整数。
    for row in reader:
        score = int(row["score"])
        students.append(score)
        print(row)

avg = stats_utils.mean(students)
fangcha = stats_utils.variance(students)
count = stats_utils.count_above(students,85)

print(avg)
print(fangcha)
print(count)