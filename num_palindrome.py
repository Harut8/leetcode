def is_palindrome(n):
    orig = n
    reverse = 0
    while n:
        n, r = divmod(n, 10)  # 123->  12,3
        reverse = reverse * 10 + r
    return reverse == orig

