fruits=["orange","apple","banana","mango"]
print(fruits)

for i in range(0,len(fruits)):
    print(fruits[i])

print(fruits[::-1])

#fruits.append("strawberry")
print(fruits)
fruits.reverse()
print(fruits)

number_list=[]
for i in range(1,10+1):
  number_list.append(i)
print(number_list)

number_list2 = list(range(1,10+1))
print(number_list2)
number_list2.sort(reverse = True)
print(number_list2)
number_list3 = number_list2.copy()

for number,fruit in enumerate(fruits):

    print(number+1, fruit)
fruit2 = ["blueberry", "raspberry"]
# for i in fruit2:
#     fruits.append(i)
# print(fruits)
fruits+=fruit2
print(fruits)