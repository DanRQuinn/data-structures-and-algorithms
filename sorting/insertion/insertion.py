def insertion_sort(arr): # Accepts an array as input
  for i in range(1, len(arr)): # Iterate through the array using a for loop
    value = arr[i] # The current element is assigned to the variable "value"
    j = i - 1 # "j" represents the index of the previous element
    while j >= 0 and arr[j] > value:  # Check if the previous element is greater than the current element
      arr[j + 1] = arr[j]  # If it is, move the previous element to the next position
      j -= 1  # Decrement "j"

    arr[j + 1] = value  # Move the current element to the next position

  return arr  # Return the sorted array

# The time complexity is O(n^2) due to the nested while loop
# The space complexity is O(1) because the array is sorted in-place

