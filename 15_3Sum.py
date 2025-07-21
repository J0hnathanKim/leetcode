class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() #1
        
        for left in range(len(nums)- 2): #2
            if left != 0 and nums[left] == nums[left - 1]: #3
                continue
            
            mid = left + 1 #4
            right = len(nums) - 1
            while mid < right: #5
                three_sum = nums[left] + nums[mid] + nums[right] #6
                if three_sum < 0:
                    mid += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    res.append([nums[left], nums[mid], nums[right]]) #7
                    
                    while mid < right and nums[mid] == nums[mid + 1]: #8
                        mid += 1
                    
                    while mid < right and nums[right] == nums[right - 1]: #9
                        right -= 1
                    
                    mid += 1 #10
                    right -= 1
            
        return res
