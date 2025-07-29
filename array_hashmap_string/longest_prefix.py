# https://leetcode.com/problems/longest-common-prefix/?envType=study-plan-v2&envId=top-interview-150

def longestCommonPrefix(strs: list[str]) -> str:
    common = strs[0]
    for i in range(1, len(strs)):
        limit = min(len(strs[i]), len(common))
        for j in range(limit):
            if strs[i][j] != common[j]:
                common = common[:j]
                break
        else:
            # No mismatch found, but current string might be shorter than common
            common = common[:limit]
        if not common:
            break  # Early stop if prefix is empty
    return common

