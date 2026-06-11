# Question : Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

            #k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

            #You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Time Complexity : O(n)


# Space Complexity : O(1)



class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        grpPrev = dummy
        while True:
            kth = self.getkth(grpPrev, k)
            if not kth:
                break
            grpNext = kth.next if kth else None
            prev = kth.next if kth else None
            curr = grpPrev.next if grpPrev else None
            while curr != grpNext:
                temp = curr.next
                curr.next = prev
                prev = curr 
                curr = temp
            temp = grpPrev.next 
            grpPrev.next = kth 
            grpPrev = temp 
        return dummy.next
    def getkth(self ,curr , k):
        while curr and k>0:
            curr = curr.next
            k-= 1
        return curr
        
