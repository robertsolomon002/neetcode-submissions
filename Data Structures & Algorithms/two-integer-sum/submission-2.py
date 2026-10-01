class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        missing = set()
        mapping = {}
        resp =[]

        for i in range(0,len(nums)):

            curr = nums[i]

            rem = target - curr
            print("-----------------")
            print(curr)
            print(rem)

            if curr not in missing:
                missing.add(rem)
                mapping[rem] = i

                print(missing)
                print(mapping)

            elif curr in missing:
                resp =[]

                resp.append(mapping[curr])
                resp.append(i)
                break
            print("-----------------")

        return resp
        