import warnings


class Heap:
    """
    Implements a heap that supports extract-min (and not extract-max)
    """
    def __init__(self, array):
        self.data = []
        # heapify array
        for a in array:
            self.insert(a)

    def __len__(self):
        return len(self.data)

    def insert(self, value):
        """Bubble-Up"""
        self.data.append(value)
        cidx = len(self)
        pidx = cidx // 2 # same as: if even(cidx): cidx/2 else floor(cidx/2)
        while (cidx > 1) and (self.data[pidx-1] > self.data[cidx-1]):
            self.data[pidx-1], self.data[cidx-1] = self.data[cidx-1], self.data[pidx-1]
            cidx = pidx
            pidx = cidx // 2

    def extract_min(self):
        """Bubble-Down"""

        if not len(self):
            warnings.warn("Heap is empty, returning None")
            return None

        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        min_value = self.data.pop() # pops last element in array
        pidx = 1
        cidx = self._get_smallest_child(pidx)
        while (cidx <= len(self)) and  (self.data[cidx-1] < self.data[pidx-1]):
            self.data[cidx-1], self.data[pidx-1] = self.data[pidx-1], self.data[cidx-1]
            pidx = cidx
            cidx = self._get_smallest_child(pidx)
        return min_value

    def _get_smallest_child(self, pidx):
        cidx1, cidx2 = pidx*2, pidx*2+1
        if cidx2 > len(self):
            return cidx1
        if self.data[cidx1-1] < self.data[cidx2-1]:
            return cidx1
        return cidx2


if __name__ == '__main__':

    array = [9, 11, 13, 4, 4, 8, 9, 4, 12]

    heap = Heap(array) # heapifies array (in heap.data)
    print("heap =", heap.data)
    value = -1
    while len(heap.data):
        value = heap.extract_min()
        print("heap.extract_min()    ->", value)
        print("heap after extraction :", heap.data)
        print('---'*20)
