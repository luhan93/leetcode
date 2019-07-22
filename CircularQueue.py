class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue_array = [None] * k
        self.head = 0
        self.tail = 0
        self.num_ele = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.queue_array[self.tail] = value
            self.num_ele += 1
            return True
        else:
            if self.tail >= self.k - 1:
                self.queue_array[0] = value
                self.num_ele += 1
                self.tail = 0
                return True
            else:
                self.queue_array[self.tail + 1] = value
                self.num_ele += 1
                self.tail += 1
                return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        if self.num_ele == 1:
            self.queue_array[self.head] = None
            self.num_ele -= 1
            return True
        else:
            self.queue_array[self.head] = None
            self.num_ele -= 1
            if self.head >= self.k - 1:
                self.head = 0
                return True
            else:
                self.head += 1
                return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.queue_array[head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.queue_array[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.num_ele == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self.num_ele == self.k:
            return True
        else:
            return False


