class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        builder = []
        ans = []

        def kSum(k, target, start):
            if k == 2:
                l, r = start, n-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s < target:
                        l+=1
                    elif s > target:
                        r-=1
                    else:
                        ans.append(builder + [nums[l], nums[r]])
                        l+=1
                        r-=1

                        # avoid duplicates
                        while l<r and nums[l] == nums[l-1]:
                            l+=1
                        while l<r and nums[r] == nums[r+1]:
                            r-=1
                return
            
            for i in range(start, n-k+1):
                if i > start and nums[i] == nums[i-1]:
                    continue
                builder.append(nums[i])
                kSum(k-1, target-nums[i], i+1)
                builder.pop()
        
        kSum(4, target, 0)
        return ans
                        
                    
