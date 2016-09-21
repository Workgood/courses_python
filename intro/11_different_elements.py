def AddandSort(from_list,to_list):#takes elements from first list and and adds to other
    for i in from_list:
       to_list.append(i)
    to_list.sort()
    return to_list

nums = []
num = input("Enter some nums: ").strip()
AddandSort(num, nums)

cur_seq = " ".join(nums)
print("Before manipulations: ",cur_seq)
new_nums = set(nums)
nums.clear()
AddandSort(new_nums,nums)

result = " ".join(nums)
print("After: ",result)
