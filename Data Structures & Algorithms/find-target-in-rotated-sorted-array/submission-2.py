class Solution:
    def search(self, nums: List[int], target: int) -> int:


        # We are now searching for the index of target. 
        # What can we do? 
        # We know that one side will be sorted. 
        # We can check to see if target is in the range of the sorted side


        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)//2
            print(mid, right, left)
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[right]:
                # right side is sorted
                if nums[mid] < target <= nums[right]:
                    # we can move left up 1.
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            

        return -1






        