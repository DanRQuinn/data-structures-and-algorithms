# Code Challenges

## Challenge 02

Take and array and reverse the order.

## Whiteboard Process

![Challenge 1](./WhiteBoards/Screenshot%202023-06-12%20at%203.05.25%20PM.png)

## Approach & Efficiency

We used what we knew from JavaScript and implemented some of the W3 schools variable names that we learned in our prep work.

## Solution

    def reverse_list(list):

      for i in range(len(list) // 2):

        temp = list[i]

        list[i] = list[len(list) - i - 1]

        list[len(list) - i - 1] = temp

      return list



    list = [1, 2, 3, 4]



    reverse_list(list)



    print(list)

Credit and Collaboration:

Anthony Sinitsa


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


## Challenge #

## Whiteboard Process

## Approach & Efficiency

## Solution

## Collaborators




## Challenge #

## Whiteboard Process

## Approach & Efficiency

## Solution

## Collaborators


## Challenge #

## Whiteboard Process

## Approach & Efficiency

## Solution

## Collaborators
