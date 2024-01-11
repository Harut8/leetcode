class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_linked_list_el(head, val):
    dummy = ListNode(None, head)
    prev = dummy
    cur = head
    while cur:
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    return dummy.next
