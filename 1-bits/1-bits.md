## Number of 1 Bits
Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

## Example 1
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits


## Algorithm 
1. If n mod 2 is not 0 then increment result by 1.
2. Right shift n by 1 bit. 
3. At most we will have to check 32 bits so O(32) - O(1)