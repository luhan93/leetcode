# Array 
| Number   | Problems                                      | Frequency     |
| -------- | --------------------------------------------- | ------------- |
| Easy     |
| 27       | Remove Element                                |
| 26       | Remove Duplicates from Sorted Array           |
| 80       | Remove Duplicates from Sorted Array II        |
| 277      | Find the Celebrity                            |
| 189      | Rotate Array                                  |
| 41       | First Missing Positive                        |
| 299      | Bulls and Cows                                |
| 134      | Gas Station                                   |
| 118      | Pascal's Triangle                             | 很少考        |
| 119      | Pascal's Triangle II                          | 很少考        |
| 169      | Majority Element                              | 很少考        |
| 229      | Majority Element II                           | 很少考        |
| 274      | H-Index                                       |
| 275      | H-Index II                                    | Binary Search |
| 243      | Shortest Word Distance                        |
| 244      | Shortest Word Distance II                     |
| 245      | Shortest Word Distance III                    |
| 217      | Contains Duplicate                            |
| 219      | Contains Duplicate II                         | 很少考        |
| 220      | Contains Duplicate III                        | 很少考        |
| 55       | Jump Game                                     |
| 45       | Jump Game II                                  |
| 121      | Best Time to Buy and Sell Stock               |
| 122      | Best Time to Buy and Sell Stock II            |
| 123      | Best Time to Buy and Sell Stock III           |
| 188      | Best Time to Buy and Sell Stock IV            |
| 309      | Best Time to Buy and Sell Stock with Cooldown |
| 11       | Container With Most Water                     |
| 42       | Trapping Rain Water                           |
| 334      | Increasing Triplet Subsequence                |
| 128      | Longest Consecutive Sequence                  |
| 164      | Maximum Gap                                   | Bucket        |
| 287      | Find the Duplicate Number                     |
| 135      | Candy                                         | 很少考        |
| 330      | Patching Array                                | 很少考        |
| 提高     |                                               |
| 4        | Median of Two Sorted Arrays                   |
| 321      | Create Maximum Number                         | 很少考        |
| 327      | Count of Range Sum                            | 很少考        |
| 289      | Game of Life                                  |
| Interval |                                               |
| 57       | Insert Interval                               |
| 56       | Merge Intervals                               |
| 252      | Meeting Rooms                                 |
| 253      | Meeting Rooms II                              |
| 352      | Data Stream as Disjoint Intervals             | TreeMap       |
| Counter  |                                               |
| 239      | Sliding Window Maximum                        |
| 295      | Find Median from Data Stream                  |
| 53       | Maximum Subarray                              |
| 325      | Maximum Size Subarray Sum Equals k            |
| 209      | Minimum Size Subarray Sum                     |
| 238      | Product of Array Except Self                  |
| 152      | Maximum Product Subarray                      |
| 228      | Summary Ranges                                |
| 163      | Missing Ranges                                |
| Sort     |                                               |
| 88       | Merge Sorted Array                            |
| 75       | Sort Colors                                   |
| 283      | Move Zeroes                                   |
| 376      | Wiggle Subsequence                            |
| 280      | Wiggle Sort                                   |


## **27. Remove Element**
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:
```
Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.

```
Example 2:

```
Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

```
Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

```

#### My solution 
**This solution is based on the order of the array can be changed.**
When we encounter $nums[i] = val$, we can swap the current element out with the last element and dispose the last one. This essentially reduces the array's size by 1.

Note that the last element that was swapped in could be the value you want to remove itself. But don't worry, in the next iteration we will still check this element.
```
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        n = len(nums)-1
        while i <= n:
            if nums[i] == val:
                nums[i] = nums[n]
                n = n-1
            else:
                i = i+1
        return n+1
```
**It should change to this one if the order cannot be changed.**
Since this question is asking us to remove all elements of the given value in-place, we have to handle it with $O(1)$ extra space. How to solve it? We can keep two pointers $i$ and $j$, where $i$ is the slow-runner while $j$ is the fast-runner.

When $nums[j]$ equals to the given value, skip this element by incrementing $j$. As long as $nums[j] \neq val$, we copy $nums[j]$ to $nums[i]$ and increment both indexes at the same time. Repeat the process until $j$ reaches the end of the array and the new length is $i$.

```
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i = i+1          
        return i 
```

## **26. Remove Duplicates from Sorted Array**
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length. Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
```
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
```
Example 2:
```
Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
```
It doesn't matter what values are set beyond the returned length.

Clarification:

Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:
```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

#### My solution
Similar to 27, we can keep two pointers $i$ and $l$, where $l$ is the slow-runner while $i$ is the fast-runner. We run a for loop of $i$, looping from the beginning to the end of the array.
When $nums[i]$ equals to the given value, skip this element. As long as $nums[i] \neq val$, we copy $nums[i]$ to $nums[l]$ and increment $l$. Repeat the process until $i$ reaches the end of the array and the new length is $l$.
```
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        l = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:    
                nums[l] = nums[i]
                l = l+1
        return l
```
## **80. Remove Duplicates from Sorted Array II**
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
```
Given nums = [1,1,1,2,2,3],
Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It doesn't matter what you leave beyond the returned length.
```
Example 2:
```
Given nums = [0,0,1,1,1,1,2,3,3],
Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
It doesn't matter what values are set beyond the returned length.
```
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:
```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```
#### My solution
One difference from 26 is that one-time duplicate is allowed. So we can still keep two pointers $i$ and $l$, where $l$ is the slow-runner while $i$ is the fast-runner. We run a for loop of $i$, looping from the beginning to the end of the array.
As long as $nums[i] \neq val$, we copy $nums[l]$ to $nums[i]$ and increment $l$. We set another variable ifduplicate $ifdu$. When $nums[i]$ equals to the given value, if the $ifdu = True$, skip this element, otherwise we copy $nums[l]$ to $nums[i]$ and increment $l$.  Repeat the process until $i$ reaches the end of the array and the new length is $l$.
```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        l = 1
        ifdu = False
        for i in range(1,len(nums)):       
            if nums[i] != nums[i-1]:
                nums[l] = nums[i]
                l = l+1
                ifdu = False
            else:
                if not ifdu:
                    nums[l] = nums[i]
                    l = l+1
                ifdu = True
        return l
```
