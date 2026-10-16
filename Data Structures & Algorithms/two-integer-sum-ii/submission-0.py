class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Condition. 
        # 1. To find target we do target - num in set 
        # 2. Can't use a set. So constant space. 

        i = 0 
        j = len(numbers)-1
        
        while i < j and numbers[i] + numbers[j] != target:
            s = numbers[i] + numbers[j]
            if s > target:
                j -= 1
            else:
                i += 1
        

        return [i+1, j+1]