<center><h2>week.1_ pdf.1</h2></center>
<h4>Queries:</h4>
### Q1.You are given an array of integers arr[]. You have to reverse the given array. 
Note: Modify the array in place. 
~~~sql
class Solution:
    def reverseArray(self, arr):
       start = 0
       end = len(arr)-1
       while start<= end :
           arr[start], arr[end]=arr[end],arr[start]
           start+=1
           end-=1
       return arr   
~~~

### Q2.Given an array arr[]. Your task is to find the minimum and maximum elements 
in the array.
~~~sql
class Solution:
    def getMinMax(self, arr):
        # code here
        max=arr[0]
        min=arr[0]
        n= len(arr)
        for i in range(1,n):
            if arr[i]> max:
                max=arr[i]
            elif arr[i]<min:
                min=arr[i]
        return min,max
~~~
### Q3.Given an integer array arr[] and an integer k, your task is to find and return 
the kth smallest element in the given array. 
Note: The kth smallest element is determined based on the sorted order of the 
array.
~~~sql 
class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        arr.sort()
        
        return arr[k-1]
~~~
### Q4.You are given two arrays a[] and b[], return the Union of both the arrays in any 
order. 
~~~sql
class Solution:    
    def findUnion(self, a, b):
        c=a+b
        d =set(c)
        return d
~~~
### Q5.Given an array arr[]. The task is to find the largest element and return it.
~~~sql
class Solution:
    def largest(self, arr):
        # code here
        max = arr[0]
        n =len(arr)
        for i in range(1,n):
            if arr[i]> max:
                max=arr[i]
        return max
~~~
### Q6.Given an array arr, rotate the array by one position in clockwise direction.
~~~sql
class Solution:
    def rotate(self, arr):
        n = len(arr)
        if n <= 1:
            return arr
        last_el = arr[n-1]

        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = last_el
        
        return arr
~~~
### Q7.You are given an integer array arr[]. You need to find the maximum sum of a 
subarray (containing at least one element) in the array arr[]. 
~~~sql
class Solution:
    def maxSubarraySum(self, arr):
       
        max_sum=arr[0]
        current_sum=0
        for num in arr:
            current_sum+=num
            if current_sum>max_sum:
                max_sum=current_sum
            if current_sum<0:
                current_sum=0
        return max_sum   
~~~
### 8.Given a sorted array of distinct integers and a target value, return the index if the 
target is found. If not, return the index where it would be if it were inserted in 
order. 
~~~sql
class Solution:
    def searchInsert(self, arr, target):
        low = 0
        high = len(arr) - 1  
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid  
            
            elif arr[mid] < target:
                low = mid +1
            else:
                high = mid - 1  
        return low
~~~
### Q9.Given an array of integers nums and an integer target, return indices of the two 
numbers such that they add up to target.
~~~sql
class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {} 
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
~~~
### Q10.You are given an array arr[] of non-negative numbers. Each number tells you 
the maximum number of steps you can jump forward from that position. 
~~~sql
class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1

        farthest = 0
        current_end = 0
        jumps = 0
        for i in range(n - 1):
            farthest = max(farthest, i + arr[i])
            if i == current_end:
                jumps += 1
                current_end = farthest

                if current_end <= i:
                    return -1
                if current_end >= n - 1:
                    return jumps

        return jumps
~~~
