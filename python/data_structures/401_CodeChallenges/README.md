# Challenge Title

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
