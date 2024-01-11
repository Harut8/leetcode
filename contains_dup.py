def contain_dup(lst):
    hash_map = {}
    for i in lst:
        if i in hash_map:
            return True
        else:
            hash_map[i] = 1
    return False

