num_kol = int(input("Number count: "))
nums = []
for _ in range(num_kol):
    nums.append(int(input("Number ")))
ad_num = []
for i in range(len(nums)):
    this = nums[i:]
    if this == this[::-1]:
        ad_num = nums[:i][::-1]#урезанный полиндром
        break
print(f"Sequence: {nums}")
print(f"Numbers to add: {len(ad_num)}")
print(f"Nubers: {ad_num}")