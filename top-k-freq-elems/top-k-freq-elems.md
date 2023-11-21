## Top K Frequent elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Frequent element is an element that exists in the array more than any other element. 

## Constraints
* 1 <= nums.length <= 105
* -104 <= nums[i] <= 104
* k is in the range [1, the number of unique elements in the array].
* It is guaranteed that the answer is unique.


## Examples

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:
1 and 2 occur 3 and 2 times respectively making them the top 2 most occuring elements in the input array.


Input: nums = [1], k = 1
Output: [1]

## Idea

1. Create an array that will store the frequency of the elements. The indexes of the array will be bounded from 1 to the length of the input array and that will make sure that the array indices are linear in the input size. If we were to create an array such that indices would correspond to each number in the input array then we would have to account for negative elements which would require some transformation of the indices. Additionally, there would be many entries in the array that would be unused. 

2. Freq array is list of lists where the index of the first list corresponds to the freq and the inner list will represent the numbers that correspond to the frequency. 

3. Flow : 
    1. Create a counter hash map. Stores the count of each element in the input. 
    2. Iterate through all the key and values in the hash map and add them to the freq array. 
    3. Iterate the frequency array backwards since entry that is found first while iterating the array backwards is the most frequent occuring element. 
    4. Stop when we have results = k 

    
