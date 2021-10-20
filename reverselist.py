class ListNode:
    def __init__(self, val=0, next = None):
         self.val = val
         self.next = next



def reverseList(head):
    prevnode = None
    while head != None:
        print(head.val)
        nextnode = head.next
        head.next = prevnode
        prevnode = head
        head = nextnode
    return prevnode


def build_linked_list(values):
    zero = ListNode(-1, None)
    previous = zero
    for v in values:
        head = ListNode(-1, None)
        previous.next = head
        head.val = v
        previous = head
    return zero.next

head = build_linked_list([1,2,3,4,5])

# while head:
#     print(head.val)
#     head = head.next

    