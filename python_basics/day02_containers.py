# 在 python_basics/day02_containers.py 中创建包含 8 个字典的学生信息列表；
# 计算平均分、最高分、按分数排序，统计及格人数。至少封装 2 个函数。
# python_basics/day02_containers.py：运行后打印4种统计结果

students = [
    {"name": "Alice", "score": 100},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 95},
    {"name": "Eva", "score": 88},
    {"name": "SCUT", "score": 67},
    {"name": "Grace", "score": 74},
    {"name": "Hannah", "score": 81}
]
# 计算平均分
def calculate_average(stduents):
    total = sum(student["score"] for student in students)
    return total / len(students)

# 计算最高分
def calculate_highest(students):
    highest = students[0]
    for student in students:
        if student["score"] > highest["score"]:
            highest = student
    return highest["score"]

# 按分数排序
sorted_students = sorted(students , key = lambda student : student["score"] , reverse= True)

# 统计及格人数
def count_pass_student(students):
    count = 0
    for student in students:
        if student["score"] >= 60:
            count += 1
    return count

average_score = calculate_average(students)
highest_score = calculate_highest(students)
pass_student = count_pass_student(students)

print("平均分为",average_score)
print("最高分为",highest_score)
print("按成绩从高到低排序：")

for student in sorted_students:
    print(student["name"], student["score"])

print("通过人数为",pass_student)


