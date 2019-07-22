class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        return self.binary_search(nums, target, left, right)

    def binary_search(self, nums, target, left, right):
        if right < left:
            return -1
        mid = (right + left) // 2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            return self.binary_search(nums, target, mid + 1, right)
        if target < nums[mid]:
            return self.binary_search(nums, target, left, mid - 1)
x = Solution()
print(x.search([-1,0,3,5,9,12],9))