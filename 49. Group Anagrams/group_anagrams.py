from typing import List

# https://leetcode.com/problems/group-anagrams


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    dict_with_strs = {}
    for str_ in strs:
        sorted_str = "".join(sorted(str_))
        if sorted_str not in dict_with_strs.keys():
            dict_with_strs[sorted_str] = [str_]

        else:
            dict_with_strs[sorted_str].append(str_)

    return list(dict_with_strs.values())
