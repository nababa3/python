def recursive_search(number, nums):
if not nums:
return False
elif nums[0] == number:
return True
else:
return recursive_search(number, nums[1:])