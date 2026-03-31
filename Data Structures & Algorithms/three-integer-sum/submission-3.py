class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        list.sort(nums)
        ans = []

        for idx, num in enumerate(nums):
            if num > 0:
                break

            if idx > 0 and num == nums[idx - 1]:
                continue

            i = idx+1
            j = len(nums)-1
            while i<j:
                s = nums[i] + nums[j] + num
                if s == 0:
                    ans.append([nums[i], num, nums[j]])
                    i += 1
                    j -= 1
                    while nums[i] == nums[i - 1] and i < j:
                        i += 1
                elif s > 0:
                    j-=1
                else:
                    i+=1

        return list(ans)



