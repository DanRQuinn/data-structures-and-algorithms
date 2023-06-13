## Challenge #2

Write a function called insertShiftArray which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Whiteboard Process

![Challenge 2](./Screenshot%202023-06-13%20at%202.21.55%20PM.png)

## Approach & Efficiency

We wanted to split the array by dividing it inhalf from each end. Then insert the new value into the middle.

## Solution

lst = [3, 12, 17, 2, 8]

def insertShiftArray

	midpoint = len(lst) // 2

	shiftArray= lst[0:midpoint] + [value to be added] + lst[midpoint:]

	shiftArray(lst)

	print(lst) # => [3, 12, 17, value to be added, 2, 8]

## Collaborators

Sarah Glass
Ashley Taylor
Jared Ciccarello
Andrew Carroll

[StackOverflow](https://stackoverflow.com/questions/48561673/adding-items-in-the-middle-of-a-list-in-python)
