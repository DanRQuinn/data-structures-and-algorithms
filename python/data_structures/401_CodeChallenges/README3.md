## Challenge 3

Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.

Dan Quinn
Sarah Glass

[Source for code](https://www.geekforgeeks.org/python-program-forbinary-for-binary-search/)

[Source for code/visual](https://ww.programiz.com/dsa/binary-search)

Big O info: BARD

## Whiteboard Process

![Challenge 3](./Screenshot%202023-06-14%20at%206.39.14%20PM.png)

## Approach & Efficiency

This uses a if else statment that uses low high and mid and depending on if x is low high or mid to continue the loop until it finds the correct index

Big O include a time complexity of 0(1) and space complexity

## Solution

def BinarySearch(arr, x):

		low = 0

		high = len(arr) - 1

		mid = 0

		while low <= high:

				mid = (high + low) // 2

				if arr[mid] < x:

						low = mid + 1

				elif arr[mid] > x:

						high = mid - 1

				else:

						return mid

		return -1

arr = [2, 3 ,4 ,10, 40]

x = 10

result = binary_search(arr, x)

if result != -1:

		print("Element is present at index", str(result))

else:

		print("Element is not present in array")

## Collaborators

Sarah Glass

