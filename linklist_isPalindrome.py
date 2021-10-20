class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head) :
        if head is None:
            return True
        first_half_end = self.find_median(head)
        second_half_start = self.reverse(first_half_end.next)
        start = head
        end = second_half_start
        result = True
        while result and end is not None:
            if start.val != end.val:
                result = False
            start = start.next
            end = end.next
        first_half_end.next = self.reverse(second_half_start)
        return result


    def find_median(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow


    def reverse(self, head):
        prevnode = None
        while head is not None:
            nextnode = head.next
            head.next = prevnode
            prevnode =head
            head = nextnode
        return prevnode


head = Listnode