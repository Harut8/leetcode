def numUniqueEmails(emails):
    un = set()
    for i in emails:
        name, dom = i.split('@')
        name = name.split('+')[0]
        name = name.replace('.', '')
        print(f"{name}@{dom}")
    return len(un)

print(numUniqueEmails(["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]))
