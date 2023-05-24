from typing import List

# https://leetcode.com/problems/two-sum

def twoSum(nums: List[int], target: int) -> List[int]:
    sorted_nums = sorted(enumerate(nums), key=lambda elem: elem[1])
    head = 0
    tail = len(sorted_nums) - 1
    for _ in range(len(sorted_nums)):
        if sorted_nums[head][1] + sorted_nums[tail][1] > target:
            tail -= 1

        elif sorted_nums[head][1] + sorted_nums[tail][1] < target:
            head += 1

        else:
            return [sorted_nums[head][0], sorted_nums[tail][0]]
