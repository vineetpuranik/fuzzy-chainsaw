## Problem Statement

Given a string s, find the length of the longest substring without repeating characters.

## Examples

Example 1:

Input: s = "abcabcbb"

Output: 3

Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"

Output: 1

Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"

Output: 3

Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

## Constraints

0 <= s.length <= 5 * 104

s consists of English letters, digits, symbols and spaces.

## Algorithm

Brute-force approach would be to collect all the substrings that can be formed from the given string. For a given string of length n, the number of substrings is given by (n * (n + 1 )) / 2 . This would mean that we would have substrings of the order n^2. For each of these substrings we can check the characters to get the length of the longest substring without repeating characters. The runtime would be O(n^2) which is polynomial in the input size and the space complexity will also be O(n^2) since we would have to store all these substrings in order to iterate over them.

Sliding window technique can be applied to this problem in order to attain a linear time complexity by using linear space. Here is the approach that can be taken :

Create a set that will keep track of all the characters that are present in our current window.

Create a result variable that will keep the track of the length of the longest substring and will be returned as the output.

Create a left pointer that will be initialized to 0. This will be the left endpoint of our window.

Create a right pointer which will iterate from start character of the string to the end of the string.

Check if the current character pointed by the right pointer is in the set. If it is not in the set then we can update result as result = max(result, right - left + 1). right - left + 1 will denote the length of the substring for our current window. If the current character is present in the set then, starting from the character pointed by our left pointer we will remove characters 1 by 1 from the set until the duplicate character is removed. While removing a character we will increment the value of left pointer every time. For this condition we will also add the current character to the set and update the result.

The key logic that needs to understood for efficiently solving the problem is the usage of the left pointer. The left pointer will always be at a position in the string such that the current substring formed by the window does not contain any duplicate characters. Additionally, removing the characters pointed by the left pointer from the set 1 by 1 while also updating the value of the left pointer every time is another crucial step.

