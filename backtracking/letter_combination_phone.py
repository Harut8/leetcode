# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

def letter_comb(digits):
    digit_letter = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    comb = []
    def backtrack(index, curr_path):
        if len(curr_path) == len(digits):
            comb.append(curr_path[:])
            return
        letters = digit_letter[digits[index]]
        for letter in letters:
            curr_path.append(letter)
            backtrack(index + 1, curr_path)
            curr_path.pop()
    backtrack(0, [])
    return comb

print(letter_comb('23'))