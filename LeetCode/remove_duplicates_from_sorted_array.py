# LeetCode 'Remove Duplicates from Sorted Array' Exercise

class Solution(object):

    def removeDuplicates(self, nums):
        new = nums[0]
        write_index = 0
        for num in nums:
            if num > new:
                new = num
                write_index += 1
                nums[write_index] = new
        return (write_index+1)