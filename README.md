# Python_Repo

Data Structures:
================
1.List
2.Tuple
3.set
4.dictionary

1.List:
=======
- Ordered collection of items
- changebale
- allows duplicates

1.1 Read & Access:
==================
lst = ['a','b','c','d','e']
print(lst[0]) # Accessing first element
print(lst[-1]) # Accessing last element
print(lst[-2]) # Accessing second to last element

1.2 Slicing:
===========
>> Slicing is used to extract a portion of a sequence such as a string, list, tuple, or range.
matrix = [['a','b','c'], ['d','e','f'], ['g','h','i']]
print(matrix[2][:2]) # Accessing elements from index 1 to end in the third row

 1.3 UnPacking
=============
>> Unpacking means taking values from a collection (like a list, tuple, or dictionary) and assigning them to multiple variables at once.

person = ['John', 25, 'Engineer', 'john@example.com', 'New York']

#name, age, profession, email, city = person
#name, *details, city = person
#name, *details = person
*details, city = person

#Unpacking with skipping the value using '_'
#name, _, profession, _, city = person
#name, *_, city = person

print(details) # Output: [25, 'Engineer', 'john@example.com']
print(city)    # Output: 'New York'

1.4 Explore & Analyze
=====================
numbers = [1,5,2,4,3]

print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
print("length:", len(numbers))
print("all:", all(numbers)) # Check if all elements are True (non-zero )
print("any:", any(numbers)) # Check if any element is True (non-zero )

print("count:", numbers.count(5)) # Count occurrences of 5
print("index:", numbers.index(5)) # Find index of 4
print("sorted:", sorted(numbers)) # Sort the list in ascending order
print("reversed:", list(reversed(numbers))) # Reverse the list
print("sorted in reverse:", sorted(numbers, reverse=True)) # Sort the list in descending order

print("in", 5 in numbers) # Check if 5 is in the list
print("not in", 6 not in numbers) # Check if 6 is not in the list
print("is", numbers is numbers) # Check if two lists are the same object
print("==", numbers == [1,5,2,4,3]) # Check if two lists are equal
print(">", numbers > [1,5,2,4,2]) # Check if one list is greater than another

1.5 Adding/Removing from List:
==============================
1.5.1 Adding
============
#2 Dimension
letters = ['a', 'b', 'c', 'd', 'e']

letters.append('f') # Add 'f' to the end of the list
letters.insert(2, 'z') # Insert 'z' at index 2

print(letters) # Output: ['a', 'b', 'c', 'd', 'e']

#3 Dimension
matrix = [[1,2,3],[4,5,6],[7,8,9]]

matrix.append([10,11,12]) # Add a new row to the matrix
matrix.insert(0,[0,0,0]) # Insert a new row at the beginning of the matrix

matrix[1].append(99) # Add 99 to the second row of the matrix
matrix[0].insert(0, 88) # Insert 88 at index 1 of the third row
print(matrix) 

1.5.2 Removing
==============
#2 Dimension
letters = ['a', 'b', 'c', 'd', 'e']

#letters.clear() # Clear all elements from the list
letters.remove('c') # Remove 'c' from the list
popletter = letters.pop(1) # Remove the element at index 1 ('b')
lastletter = letters.pop() # Remove the last element from the list

print(popletter)
print(lastletter)
print(letters) 

#3 Dimension
matrix = [['a','b','c'],['d','e','f'],['g','h','i']]

#matrix.clear() # Clear all rows from the matrix
#matrix.remove(['d','e','f']) # Remove the row ['d','e','f'] from the matrix
#matrix.pop(0) # Remove the first row from the matrix
matrix[1].remove('e') # Remove 'e' from the second row
matrix[0].pop() # Remove the last element from the first row

print(matrix)

1.6 Updating
============
#2D
letters = ['a', 'b', 'c', 'd', 'e']

letters[0] = 'z' # Change the first element to 'z'
print(letters)

#3D
matrix = [['a','b','c'],['d','e','f'],['g','h','i']]

matrix[0][0] = 'z' # Change the element at row 0, column 0 to 'z'
matrix[1][-1] = '-' # Change the last element of the second row to 'y'

print(matrix)

1.7 Sorting/Reverse
====================
1.7.1 Sorting
============
#2D
letters = ['a', 'c', 'b', 'd', 'e']
#letters.sort() # Sort the list in ascending order
#letters.sort(reverse=True) # Reverse the list

#new_list = sorted(letters) # Create a new sorted list without modifying the original
new_list = sorted(letters, reverse=True) # Create a new sorted list in descending order

print('original list:', letters)
print('sorted list:', new_list) 

1.7.2 Reverse
=============
letters = ['a', 'c', 'b', 'd', 'e']
#letters.sort() # Sort the list in ascending order
#letters.sort(reverse=True) # Reverse the list

#new_list = sorted(letters) # Create a new sorted list without modifying the original
#new_list = sorted(letters, reverse=True) # Create a new sorted list in descending order

#print('original list:', letters)
#print('sorted list:', new_list) 

#letters.reverse() # Reverse the list in place

new_list = list(reversed(letters)) # Create a new reversed list without modifying the original

print('original list:', letters)
print('reversed list:', new_list)

1.8 Copy
========
letters = ['a', 'b', 'c', 'd', 'e']

#letters_copy = letters # Create a reference to the same list
#letters_copy.append('f') # Add 'f' to the copied list

letters_copy = letters.copy() # Create a shallow copy of the list
letters_copy.append('f') # Add 'f' to the copied list

print('original list:', letters)
print('copied list:', letters_copy)

