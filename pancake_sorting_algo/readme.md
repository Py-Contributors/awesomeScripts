# Pancake Sorting Algo

### Unlike a traditional sorting algorithm, which attempts to sort with the fewest comparisons possible, the goal is to sort the sequence in as few reversals as possible.

Following are the detailed steps. Let given array be arr[] and size of array be n. 

- Start from current size equal to n and reduce current size by one while it’s greater than 1. Let the current size be curr_size. 
- Do following for every curr_size
- - Find index of the maximum element in arr[0 to curr_szie-1]. Let the index be ‘mi’
- - Call flip(arr, mi)
- - Call flip(arr, curr_size – 1)