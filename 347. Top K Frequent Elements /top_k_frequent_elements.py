from typing import List

# https://leetcode.com/problems/top-k-frequent-elements


def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter_map = {}
    for num in nums:
        if num in counter_map:
            counter_map[num] += 1
        else:
            counter_map[num] = 1

    sorted_list = sorted(counter_map.items(), reverse=True, key=lambda el: el[1])
    return [el[0] for el in sorted_list[:k]]
