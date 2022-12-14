# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list

# count()	Returns the number of elements with the specified value
this_list = [1, 3, 7, 8, 7, 5, 4, 6, 8, 5]
print(this_list.count(5)) # returns number of times 5 appears in this_list
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list





# complexities
# Append : O(1)
# Extend : O(k) - k is the length of the extension
# Index : O(1)
# Slice : O(k)
# Sort : O(n log n) - n is the length of the list
# Len : O(1)
# Pop : O(1) - pop from end
# Insert : O(n) - n is the length of the list
# Del : O(n) - n is the length of the list
# In : O(n) - n is the length of the list
# + : O(m + n) - m & n are the length of the lists - this creates a new list object
# += : O(n) - n is the length of the list being added - list is extended.
