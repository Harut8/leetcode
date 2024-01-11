def longest_common_prefix(strings):
    for i in range(len(strings[0])):
        for string in strings[1:]:
            if i == len(string) or string[i] != strings[0][i]:
                return strings[0][:i]
    return strings[0]

