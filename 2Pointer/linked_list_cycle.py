class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None
class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

ans=Solution()
print(ans.hasCycle(node1))

a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)

a.next=b
b.next=c
c.next=d

print(ans.hasCycle(a))