# fruits = ["apple", "banana", "cherry"]
# print(fruits[0]) 


# # list1 = [i+1 for i in range(6)]
# # print(list1)

# #(a) Slicing
# nums = [10, 20, 30, 40, 50]
# print(nums[1:4])   # [20, 30, 40]
# print(nums[:3])    # [10, 20, 30]
# print(nums[::2])



# # (b) Iteration
# nums = [10, 20, 30, 40, 50]
# for item in nums:
#     print(item)

# # (c) Functions with Lists

# nums = [10, 20, 30, 40, 50]
# print(len(nums))     # 5
# print(max(nums))     # 50
# print(min(nums))     # 10
# nums.append(60)      
# print(nums)          # [10,20,30,40,50,60]


#List Comprehension, Problem Solving

# # Example 1: Square of numbers
# squares = [x**2 for x in range(1, 6)]
# print(squares)   # [1, 4, 9, 16, 25]

# # Example 2: Filter even numbers
# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)   # [0, 2, 4, 6, 8]

# # Example 3: Add prefix
# names = ["Kiran", "Ravi", "Meena"]
# hello = ["Hello " + name for name in names]
# print(hello)

# nums = [10, 20, 30, 60, 50]
# print(sorted(nums))
# nums.reverse()
# print(nums)
# # nums.pop(10)
# a=nums.pop(4)
# print(a)