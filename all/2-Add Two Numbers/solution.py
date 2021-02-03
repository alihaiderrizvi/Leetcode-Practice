class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        num2 = ''
        
        i = l1.val
        j = l2.val
        
        while l1 != None:
            num1 += str(i)
            l1 = l1.next
            try:
                i = l1.val
            except:
                pass
        
        while l2 != None:
            num2 += str(j)
            l2 = l2.next
            try:
                j = l2.val
            except:
                pass
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        num3 = str(int(num1) + int(num2))[::-1]
        
        k = ListNode(num3[0])
        head = k
        
        for i in num3[1:]:
            k.next = ListNode(i)
            k = k.next

        return head
