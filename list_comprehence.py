
num_list = [0,1,2,3,4,5,6,7,8,9]
fruits=["orange","apple","banana","mango"]
def square_list(num_list):
    append_list=[]
    for i in range(0,len(num_list)):
        if i%2 ==0 :
            append_list.append(num_list[i] ** 2)

    return append_list
print(square_list(num_list))
print([num_list[x]**2 for x  in range(0,len(num_list)) if x%2==0])
name ="daniel"

print([name[i] for i in range(0,len(name))])
print([fruits[i].upper() for i in range(0,len(fruits))])
print([len(fruits[i]) for i in range(0, len(fruits))])
print([fruits[i][::-1] for i  in range(0, len(fruits))])
sentence = "the sun rises in the east"
print([sentence[i] for i in range(0,len(sentence)) if sentence[i] in "aeiou"])