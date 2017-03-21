class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            while low < high and nums[low] == nums[high]:
                low += 1
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            if nums[mid] >= nums[low]:
                if nums[mid] < target:
                    low = mid + 1
                else:
                    if nums[low] > target:
                        low = mid + 1
                    else:
                        high = mid - 1
            else:
                if nums[mid] > target:
                    high = mid - 1
                else:
                    if nums[high] < target:
                        high = mid - 1
                    else:
                        low = mid + 1
        return False
