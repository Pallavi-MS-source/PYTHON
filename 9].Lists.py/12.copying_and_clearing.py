original_list = ['mango','orange','banana','apple','strawberry']

#Copy
      # when need to return new list without affecting original list
new_list = original_list.copy()
print(new_list)
new_list.append(420)
print(new_list)
print(original_list)

# Clear
# returns empty list
original_list.clear()
print(original_list)