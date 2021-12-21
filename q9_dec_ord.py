nums=[]
print("Enter the Numbers:")
for i in range(5):
    ival=int(input())
    nums.append(ival)

nums.sort(reverse=True)

print(nums)
