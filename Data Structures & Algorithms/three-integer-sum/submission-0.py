class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []


        for i,elem in enumerate(nums):
            if i > 0 and elem == nums[i-1]:
                continue
            else:


                j = i+1
                k = len(nums) -1

                while k > j:
                    add = elem + nums[j] + nums[k]

                    if add > 0:
                        k -= 1
                    elif add<0:
                        j += 1
                    else:
                        ans.append([nums[i],nums[j],nums[k]])

                        j +=1 
                        while j < k and nums[j] == nums[j-1]:
                            j += 1


        return ans        
        