## Merge Sort

Recursively split the input array a into left and right halves until we are left with 1 element. 

function mergesort(a[1 . . . n])
Input: An array of numbers a[1 . . . n]
Output: A sorted version of this array
if n > 1:
return merge(mergesort(a[1 . . . bn/2c]), mergesort(a[bn/2c + 1 . . . n]))
else:
return a


function merge(x[1 . . . k], y[1 . . . l])
if k = 0: return y[1 . . . l]
if l = 0: return x[1 . . . k]
if x[1] ≤ y[1]:
return x[1] ◦ merge(x[2 . . . k], y[1 . . . l])
else:
return y[1] ◦ merge(x[1 . . . k], y[2 . . . l])