class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def createLinkedList(arr: 'List[int]') -> 'ListNode':
    if arr is None or len(arr) == 0:
        return None

    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next

    return head

## 查/改
head = createLinkedList([1,2,3,4,5])

p = head
while p is not None:
    # print(p.val)
    p = p.next


## 增
##在单链表头部插入新元素
head = createLinkedList([1, 2, 3, 4, 5])
newNode = ListNode(0)
newNode.next = head
head = newNode

p = head
while p is not None:
    # print(p.val)
    p = p.next

##在单链表尾部插入新元素
head = createLinkedList([1, 2, 3, 4, 5])

p = head
while p.next is not None:
    p = p.next
p.next = ListNode(6)

p = head
while p is not None:
    # print(p.val)
    p = p.next


##在单链表中间插入新元素
head = createLinkedList([1, 2, 3, 4, 5])
p = head
for _ in range(2):
    p = p.next

newNode = ListNode(666)
newNode.next = p.next
p.next = newNode

p = head
while p is not None:
    print(p.val)
    p = p.next



