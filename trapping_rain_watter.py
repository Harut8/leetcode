# https://leetcode.com/problems/trapping-rain-water/

def trapping_rain_water(heights):
    lft, rgt = 0, len(heights) - 1
    l_max, r_max = 0, 0
    result = 0
    while lft <= rgt:
        if l_max < r_max:
            l_max = max(l_max, heights[lft])
            result += l_max - heights[lft]
            lft += 1
        else:
            r_max = max(r_max, heights[rgt])
            result += r_max - heights[rgt]
            rgt -= 1
    return result

print(trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))
