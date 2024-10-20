# https://leetcode.com/problems/min-stack/
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.min_stack.append(min(val, self.min_stack[-1] if self.min_stack else val))
        self.stack.append(val)

    def pop(self):
        """
        :rtype: void
        """
        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

"""
AMEN PUSH I JMNK MENQ
STUGUM ENQ ARDYOQ AYD ELEMENTY MECAGUYNN E TE VOCH
AYSINQN PUSH ANELUC ARAJ ETE MIN_STACK UM KA ELEMENT
VERCNUM ENQ EV STUGUM ARDYOQ POQR E TE MEC EV AVELACNUM ENQ ETE KARIQY KA
HAKARAK DEPQUM CHENQ ANUM
"""