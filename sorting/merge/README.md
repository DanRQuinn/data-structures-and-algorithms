# Blog Notes: Merge Sort

Divide: The array is split into smaller halves until we have single elements or empty subarrays.

Conquer: Each small subarray is sorted individually. This is done by recursively applying the Merge Sort algorithm to the subarrays.

Merge: The sorted subarrays are merged back together in a sorted order. This is done by comparing the elements of the subarrays and placing them in the correct order in a new resulting array.

## Pseudocode

    ALGORITHM Mergesort(arr)
        DECLARE n <-- arr.length

        if n > 1
          DECLARE mid <-- n/2
          DECLARE left <-- arr[0...mid]
          DECLARE right <-- arr[mid...n]
          // sort the left side
          Mergesort(left)
          // sort the right side
          Mergesort(right)
          // merge the sorted left and right sides together
          Merge(left, right, arr)

    ALGORITHM Merge(left, right, arr)
        DECLARE i <-- 0
        DECLARE j <-- 0
        DECLARE k <-- 0

        while i < left.length && j < right.length
            if left[i] <= right[j]
                arr[k] <-- left[i]
                i <-- i + 1
            else
                arr[k] <-- right[j]
                j <-- j + 1

            k <-- k + 1

        if i = left.length
          set remaining entries in arr to remaining values in right
        else
          set remaining entries in arr to remaining values in left

By repeatedly dividing the array, sorting the smaller parts, and merging them back together, Merge Sort gradually sorts the entire array.

Initial arr: [8, 4, 23, 42, 16, 15]

Divide arr into two halves:

left: [8, 4, 24]

right: [15, 16, 42]

Recursively sort left and right arr's:

left: [4, 8, 23]

right: [15, 16, 42]

Merge the two sorted halves back into original arr:

arr: [4, 8, 15, 16, 23, 42]

Start with the initial call to Mergesort(arr) on the input array arr.

Check if the length of the array (n) is greater than 1.

If n > 1, find the middle index (mid) by dividing n by 2.

Split the array into two sub-arrays: left (arr[0...mid]) and right (arr[mid...n]).

Recursively call Mergesort(left) to sort the left sub-array.

Repeat steps 2-5 for the left sub-array until the sub-arrays have a length of 1 or are empty.

Once the left sub-array is sorted, repeat steps 2-6 for the right sub-array.

Merge the sorted left and right sub-arrays together using the Merge function.

In the Merge function, compare the elements of the left and right sub-arrays and place them in the merged array (arr) in the correct order.

Continue merging elements until either the left or right sub-array is fully processed.

If there are remaining elements in the left sub-array, copy them to the merged array.

If there are remaining elements in the right sub-array, copy them to the merged array.

Return to the previous recursive call level and continue merging until the entire array is sorted.

The algorithm terminates when the initial call level is reached, and the entire array is sorted.

![Alt text](<Screenshot 2023-07-18 at 1.51.35 PM.png>)
