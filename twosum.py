class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #loop over array with index n
        for n in range(len(nums)):
            #substract aray [n] from target
            tmp=target-nums[n]
            #loop over the list starting by n+1
            for i in range(n,len(nums)):
                if nums[i]==tmp and i != n:
                    return [n,i]
                else:
                    pass
        # continue looping until result the array eolement equal previous results 
