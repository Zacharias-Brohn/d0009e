from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = []
        target = 0
        solution = []
        incindex = 1
        for i in nums:
            while nums[i] + nums[i+incindex] <= target:
                if nums[i] + nums[i+incindex] == target:
                    solution = [i, i+incindex]
                    return solution
                else:
                    incindex += 1
        return solution

def main():
    nums = [2,7,11,15]
    target = 9
    sol = Solution()
    output = sol.twoSum(nums, target)
    print(f"Output: {output}")
