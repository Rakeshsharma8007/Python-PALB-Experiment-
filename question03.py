''' question 03.
Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.
Note: The kth smallest element is determined based on the sorted order of the array.
Examples :
Input: arr[] = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4
Output: 5
Explanation: 4th smallest element in the given array is 5.'''

class Solution:
    def kthSmallest(self, arr, k):
        arr.sort()
        return arr[k-1]
if __name__ == "__main__":
    sol = Solution()
    my_arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
    k_value = 4
    
    result = sol.kthSmallest(my_arr, k_value)
    print(f"The {k_value}th smallest element is: {result}")