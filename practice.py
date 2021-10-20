class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values):
    zero = ListNode(-1, None)
    previous = zero
    for v in values:
        head = ListNode(-1, None)
        previous.next = head
        head.val = v
        previous = head
    return zero.next


def reverse_list(head):
    previous = None
    while head:
        #print(head.val)
        nextnode = head.next
        head.next = previous
        previous = head
        head = nextnode
    return previous

head = build_linked_list([1,2,3,4,5])
# tail = reverse_list(head)
#
reversed_head = reverse_list(head)
while reversed_head:
    print(reversed_head.val)
    reversed_head = reversed_head.next

