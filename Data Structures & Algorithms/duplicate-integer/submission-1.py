class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        booleanHash = {}
        for i in range (len(nums)):
            if booleanHash.get(nums[i]) == None:
                booleanHash[nums[i]] = True
            elif booleanHash.get(nums[i]) == True:
                return True
            
        return False
        