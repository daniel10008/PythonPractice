empty_tuple =tuple()
print(type(empty_tuple))
num_list=[1,2,3,4]
nums = tuple(num_list)
hetero_tuple = ("orange","apple","banana", 0.12345,23,True, 'a', num_list)
print(type(nums))
print(hetero_tuple[7])
print(hetero_tuple[::])
for i in range(0,len(hetero_tuple)):
    print(hetero_tuple[i])
friend_tuple =[("harry", 20183851834), ("john", 2341029523)]
print([friend_tuple[i][0] for i in range(0,len(friend_tuple))])
lottery_number =[16, 4, 9, 12, 80, 7, 23]
def high_low (list_high_low):
    return max(list_high_low),min(list_high_low)
high, low= high_low(lottery_number)
print(f"the max number in the function is {high} and the minimum lottery number is {low}")