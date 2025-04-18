import sys


class ObjList:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        self.__prev = obj

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj


def push_back(num):
    global tail, mid, p
    l = len(queue)
    obj = ObjList(num)
    queue.append(obj)
    queue[tail].next = l
    queue[l].prev = tail
    tail = l
    if isinstance(mid, ObjList):
        if (l - p) % 2 != 0:
            mid = queue[mid.next]


def push_first(num):
    global mid
    obj = ObjList(num)
    queue.append(obj)


def push_mid(num):
    global mid, tail, p
    l = len(queue)
    obj = ObjList(num)
    queue.append(obj)
    if l - p == 0:
        pass
    elif mid is None:
        inx = (l - p) // 2 + p
        if (l - p) % 2 == 0:
            mid_prev = queue[inx].prev
            queue[inx].prev = l
            obj.prev = mid_prev
            obj.next = inx
            if mid_prev is not None:
                queue[mid_prev].next = l
            mid = obj
        elif (l - p) % 2 != 0:
            mid_next = queue[inx].next
            queue[inx].next = l
            obj.prev = inx
            obj.next = mid_next
            if mid_next is not None:
                queue[mid_next].prev = l
            mid = obj
    else:
        if (l - p) % 2 == 0:
            mid_prev = mid.prev
            mid.prev = l
            if mid_prev is not None:
                obj.prev = mid_prev
                obj.next = queue[mid_prev].next
                queue[mid_prev].next = l
            mid = obj
        elif (l - p) % 2 != 0:
            mid_next = mid.next
            mid.next = l
            if mid_next is not None:
                obj.next = mid_next
                obj.prev = queue[mid_next].prev
                queue[mid_next].prev = l
            else:
                obj.prev = head
            mid = obj
    if l - p == 1:
        tail = l


def pop_front():
    global head, mid, tail, p
    head_data = queue[head].data
    new_head = queue[head].next
    if new_head:
        queue[head].next = None
        queue[new_head].prev = None
        head = new_head
    else:
        head += 1

    l = len(queue) - 1
    if l - p == 0:
        tail += 1
    p += 1
    if isinstance(mid, ObjList) and (p != l):
        if not new_head:
            mid = None
        else:
            if (l - p) % 2 != 0:
                mid = queue[mid.next]
    return head_data


n = sys.stdin.readline().strip()
lst_in = [list(value.split()) for value in sys.stdin.readlines()]

queue = []
head = tail = 0
mid = None
p = 0

for goblin in lst_in:
    goblin_type = goblin[0]
    if goblin_type == '+':
        num = int(goblin[1])
        if len(queue) != head:
            push_back(num)
        else:
            push_first(num)

    elif goblin_type == '*':
        num = int(goblin[1])
        push_mid(num)

    elif goblin_type == '-':
        print(pop_front())
