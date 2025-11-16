
my_list = [1, 2, 3, "a", "b", "c"] # note: deliberately used a combination of numbers and letters as values to show that data types can be mixed in lists
# add an element to the end of the list
my_list.append(4)   # my_list becomes [1, 2, 3, ‘a’, ‘b’, ‘c’, 4]
# insert an item at index (note that inserting beyond the last index + 1 of the existing list will simply add the value as the last element in the list)
my_list.insert(6, "d")  # my_list becomes [1, 2, 3, ‘a’, ‘b’, ‘c’, ‘d’, 4]
# assign a new value to index
my_list[7] = "e"    # my_list  becomes [1, 2, 3, ‘a’, ‘b’, ‘c’, ‘d’, ‘e’]
# remove an element by value (note if multiple instances of value exist in the list, only the first instance is removed), if no instance of value exists, returns ValueError
my_list.remove("e") # my_list becomes [1, 2, 3, ‘a’, ‘b’, ‘c’, ‘d’]
# pop (remove) and return the last item, if list is empty return IndexError
popped_value = my_list.pop() # my_list becomes [1, 2, 3, ‘a’, ‘b’, ‘c’], and popped_value equals ‘d'
# pop (remove) and return item at index, and returns IndexError if index does not exist
popped_value = my_list.pop(2) # my_list becomes [1, 2, ‘a’, ‘b’, ‘c’], and popped_value equals 3
# delete element at index, and returns IndexError if index does not exist
del my_list[2] # my_list becomes [1, 2, ‘b’, ‘c’]

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] # first 10 numbers in the Fibonacci sequence, order matters
#print(fibonacci)
# append the 11th fibonacci number by calculating it based on the value at the 8th index + the value at the 9th index
fibonacci.append(fibonacci[len(fibonacci) - 2] + fibonacci[len(fibonacci) - 1]) # adds 55 at index 10 of the list
# get the 4th element in the Fibonacci sequence
value = fibonacci[3] # 3rd index is 4th value in the list. value equals 2


my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]
print(my_list[3:1:-1])

# define dictionary my_dict — note: I deliberately used a combination of numbers and letters as keys/values to show that data types can be mixed in dictionaries
my_dict = {"a": 1, 2: "b", "c": 3}
# add a new element by specifying a key that doesn’t exist yet in the dictionary and its corresponding value
my_dict["d"] = 10 # my_dict becomes {‘a’: 1, 2: ‘b’, ‘c’: 3, ‘d’: 10}
# update a value for a given key that does exist in the dictionary
my_dict["d"] = 4 # my_dict becomes {‘a’: 1, 2: ‘b’, ‘c’: 3, ‘d’: 4}
# pop element by key and return its value, and returns KeyError if that key does not exist
popped_value = my_dict.pop("c") # my_dict becomes {‘a’: 1, 2: ‘b’, ‘d’: 4}, and popped_value equals 3
# popitem to remove the last element from the dictionary and return a tuple with the key and value. If dictionary is empty return KeyError
popped_element = my_dict.popitem() # my_dict becomes {‘a’: 1, 2: ‘b’}, and popped_element equals (‘d’, 4)
# delete element at key, and returns KeyError if that key does not exist
del my_dict[2] # my_dict becomes {‘a’: 1}

high_temps = { "January": 5, "February": 7, "March": 12, "April": 18, "May": 22, "June": 27, "July": 30, "August": 29, "September": 24, "October": 17, "November": 10, "December": 6 }
# retrieve and print high temp for August
#print(f"High temp for August was: {high_temps['August']}")
# correct the data for February
high_temps['February'] = 9