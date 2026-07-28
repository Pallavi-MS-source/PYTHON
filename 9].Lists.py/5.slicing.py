# #        0  1   2    3   4   5   6   7  8    9   10 
# #      -11 -10  -9  -8  -7  -6  -5  -4 -3   -2   -1
# lst = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 99, 100]
# # positive step

# lst1=lst[0:4]
# lst1=lst[3:9]
# lst1=lst[4:44]      # if stop is out of range then print till end of list
# lst1=lst[8:8]       # returns blank list
# lst1=lst[:4]        # from 0th index to 3rd index
# lst1=lst[7:]        # from 7th index to end of list
# lst1=lst[0:9:2]     # step 2
# lst1=lst[:9:2] 
# lst1=lst[0::2] 
# lst1=lst[::] 
# print(lst1)


#        0  1   2    3   4   5   6   7  8    9   10 
#      -11 -10  -9  -8  -7  -6  -5  -4 -3   -2   -1
lst = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 99, 100]
# negative step

lst1 = lst[9:3:-1]
lst1 = lst[6:0:-1]
lst1 = lst[::-1]


print(lst1)
