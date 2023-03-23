text =input()
nums = []

for i in range(len(text)):
    for j in range(len(text)+1):
        nums.append(text[i:j])
only=set(nums)
print(len(only)-1)