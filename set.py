my_set =set()
my_set.add("water")
my_set.add("water")
my_set.add("coffee")
print(my_set)
if "milk" in my_set:
    print("milk is there in the set")
else:
    print("milk is not there")

a ={1,2,3,4,5,6}
b={1,2,35,23,0,8}
print(b.union(a))
print(a.intersection(b))

list1 = [5,6,7,9]
list2 = [9,8,1,2]
set1 = set(list1)
set2 = set(list2)
print(set1.intersection(set2))
print(set2.difference(set1))
print(set1.symmetric_difference(set2))


# A university maintains student enrollment records for two courses: Mathematics and Computer Science. Each student is assigned a unique ID. You are given two sets:
#
# math_students: Contains student IDs of students enrolled in Mathematics.
# cs_students: Contains student IDs of students enrolled in Computer Science.
# Your task is to perform the following operations using set methods:
#
# Find students who are enrolled in both courses (Intersection).
# Find students who are enrolled in at least one course (Union).
# Find students who are enrolled only in Mathematics and not in Computer Science (Difference).
# Find students who are enrolled in only one of the two courses (Symmetric_Difference).
# math_students = {101, 102, 103, 104, 105, 106}
# cs_students = {104, 105, 106,107,108,109}
math_students = {101, 102, 103, 104, 105, 106}
cs_students = {104, 105, 106,107,108,109}
print(f"the student id of the people enrolled in both courses are: {math_students.intersection(cs_students)}")
print(f"the student id of the people enrolled in at least one course are: {math_students.union(cs_students)}")
print(f"the student id of the people enrolled in mathematics and not computer science  are: {math_students.difference(cs_students)}")
print(f"the student id of the people enrolled in one of the 2 courses are: {math_students.symmetric_difference(cs_students)}")
