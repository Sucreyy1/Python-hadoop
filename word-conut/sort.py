# 排序基础
# sorted()会生成一个新的list,list.sort()不会生成新的list.这个需要注意,不要在循环里使用sorted,避免内存爆掉
lists = [1, 2, 3, 4, 5, 6]

lists.sort(reverse=True)
print(lists)

# key参数/函数
# 1.例子
lists = sorted('This is a test'.split(), key=str.lower)  # key参数的值是一个函数,此函数只有一个参数且返回一个值用来进行比较
print(lists)  # 相当于list中每个元素都会调用一次key传入的函数.然后进行比较

# 2.例子 根据年龄排序
student_tuple = [
    ('John', 'A', 15),
    ('Jane', "C", 22),
    ('James', 'B', 12),
]
student_tuple.sort(key=lambda student: student[2])
print(student_tuple)

# Operator 模块函数
from operator import itemgetter, attrgetter

student_tuple.sort(key=itemgetter(1))
print(student_tuple)
# 如果列表里是对象的话可以直接取属性名
# student_tuple.sort(key=itemgetter('age'))


# 多级排序 先以等级排序,然后再以年龄排序
student_tuple.sort(key=itemgetter(2, 1))
print(student_tuple)
