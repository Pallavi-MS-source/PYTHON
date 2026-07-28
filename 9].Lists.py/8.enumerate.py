nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 99, 100 ]
for index,value in enumerate (nums):
    print(f"Index = {index} and Value = {value}")

for index,value in enumerate (nums):
    if value % 2 != 0:
        print(index)