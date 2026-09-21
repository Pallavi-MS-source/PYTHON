fruits={'banana', 'mango', 'apple', 'kiwi', 'grapes'}
#remove (if element does not exist,gives error msg)
fruits.remove("banana")
print(fruits)

#discard (if element does not exist,doesn't give error msg)
fruits.discard("bananaaa")
print(fruits)

#pop (removes random element)
removed=fruits.pop()
print(f"removed element is {removed}")

#clear (removes all elements)
fruits.clear()
print(fruits)