import sys

class MaxHeap:
    def __init__(self):
        self.heap = []

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left_child(i):
        return 2 * i + 1

    @staticmethod
    def right_child(i):
        return 2 * i + 2

    def add(self, elem):
        self.heap.append(elem)
        self.siftUp(len(self.heap) - 1)

    def siftUp(self, elem_inx):
        while elem_inx > 0 and self.heap[elem_inx] > self.heap[self.parent(elem_inx)]:
            parent_inx = self.parent(elem_inx)
            self.heap[elem_inx], self.heap[parent_inx] = self.heap[parent_inx], self.heap[elem_inx]
            elem_inx = parent_inx

    def siftDown(self, elem):
        len_heap = len(self.heap)
        while True:
            left_child = self.left_child(elem)
            right_child = self.right_child(elem)
            max_elem = elem
            if left_child < len_heap and self.heap[max_elem] < self.heap[left_child]:
                max_elem = left_child
            if right_child < len_heap and self.heap[max_elem] < self.heap[right_child]:
                max_elem = right_child

            if elem != max_elem:
                self.heap[elem], self.heap[max_elem] = self.heap[max_elem], self.heap[elem]
                elem = max_elem
            else:
                break

    def extractMax(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        print(self.heap.pop(-1))
        self.siftDown(0)


n = sys.stdin.readline().strip()
lst_in = [list(map(int, value.split())) for value in sys.stdin.readlines()]
heap = MaxHeap()

for value in lst_in:
    operation = value[0]
    if operation == 0:
        heap.add(value[1])
    else:
        heap.extractMax()
