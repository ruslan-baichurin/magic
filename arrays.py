# importing "array" for array operations
import array

# initializing array with signed integers
arr = array.array('i', [1, 2, 3])

print ("The new created array is: ", end=" ")
for item in arr:
    print(item, end=" ")
print('\r')

arr.append(4)
print("The appended array is: ", end="")
for item in arr:
    print(item, end=" ")
print('\r')

arr.insert(2, 5)
print ("The array after insertion is: ", end="")
for item in arr:
    print(item, end=" ")
print('\r')

print ("The popped element is: ", end="")
print(arr.pop(2))
print('\r')

print ("The array after popping is: ", end="")
for item in arr:
    print(item, end=" ")
print('\r')

arr.remove(1)
print ("The array after removing is: ", end="")
for item in arr:
    print(item, end=" ")
print('\r')

print ("The index of the first occurrence of three is: ", end="")
print(arr.index(3))
print('\r')

arr.reverse()

print("The array after reversing is: ", end="")
for item in arr:
    print(item, end=" ")
print('\r')