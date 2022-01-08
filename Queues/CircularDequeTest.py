from CircularDeque import CircularDeque
import unittest, random

random.seed(1342)

"""
    !!! I did not write these test cases. They were written by my professor for testing
    a circular deque !!!

    I used this code to prove that the CD I wrote does, in fact, work at the level that 
    my professor would have wanted it to.
"""

class CircularDequeTests(unittest.TestCase):

    def test_len(self):
        cd = CircularDeque()
        self.assertEqual(0, len(cd))

        cd = CircularDeque([1])
        self.assertEqual(1, len(cd))

        cd = CircularDeque([1, 2])
        self.assertEqual(2, len(cd))

        cd = CircularDeque(list(range(50)), 50)
        self.assertEqual(50, len(cd))

    def test_is_empty(self):
        cd = CircularDeque()
        self.assertTrue(cd.is_empty())

        cd = CircularDeque([1])
        self.assertFalse(cd.is_empty())

        cd = CircularDeque([1, 2])
        self.assertFalse(cd.is_empty())

        cd = CircularDeque(list(range(50)), 50)
        self.assertFalse(cd.is_empty())

    def test_front_element(self):
        cd = CircularDeque()
        self.assertIsNone(cd.front_element())

        cd = CircularDeque([1])
        self.assertEqual(1, cd.front_element())
        cd.front = cd.back = None
        cd.size = 0
        self.assertIsNone(cd.front_element())

        cd = CircularDeque([2, 1])
        self.assertEqual(2, cd.front_element())
        cd.front = cd.back = None
        cd.size = 0
        self.assertIsNone(cd.front_element())

        cd = CircularDeque(list(range(50)), 50)
        self.assertFalse(cd.is_empty())
        self.assertEqual(0, cd.front_element())
        cd.front = cd.back = None
        cd.size = 0
        self.assertIsNone(cd.front_element())

    def test_back_element(self):
        cd = CircularDeque()
        self.assertIsNone(cd.back_element())

        cd = CircularDeque([1])
        self.assertEqual(1, cd.back_element())
        cd.back = cd.back = None
        cd.size = 0
        self.assertIsNone(cd.back_element())

        cd = CircularDeque([1, 2])
        self.assertEqual(2, cd.back_element())
        cd.back = cd.back = None
        cd.size = 0
        self.assertIsNone(cd.back_element())

        cd = CircularDeque(list(range(50)), 50)
        self.assertFalse(cd.is_empty())
        self.assertEqual(49, cd.back_element())
        cd.back = cd.back = None
        cd.size = 0
        self.assertIsNone(cd.back_element())

    def test_enqueue_basic(self):
        # (1) empty queue
        # (1a) front_enqueue
        for capacity in range(4, 50):
            for front in range(capacity):
                cd = CircularDeque(list(range(capacity)), capacity)
                cd.size = 0
                cd.front = cd.back = front
                cd.front_enqueue(1000)
                self.assertIn(1000, cd.queue)
                self.assertEqual(1, cd.queue.count(1000))
                self.assertEqual(cd.back, cd.front)
                self.assertEqual(1, cd.size)

        # (1b) back_enqueue
        for capacity in range(4, 50):
            for front in range(capacity):
                cd = CircularDeque(list(range(capacity)), capacity)
                cd.size = 0
                cd.front = cd.back = front
                cd.back_enqueue(1000)
                self.assertIn(1000, cd.queue)
                self.assertEqual(1, cd.queue.count(1000))
                self.assertEqual(cd.back, cd.front)
                self.assertEqual(1, cd.size)

        # (2) front_enqueue basics
        for capacity in range(4, 50):
            for front in range(capacity):
                for back in range(capacity):  # So grow isn't called upon
                    if front == back:  # Skip, means queue is empty
                        continue
                    list_representation = list(range(capacity))
                    size = back - front + 1 if front < back else capacity - (front - back)
                    if size == capacity - 1:  # Skip, means adding to the queue will make the queue full and then grow
                        continue
                    cd = CircularDeque(list(range(capacity)), capacity)
                    cd.front = front
                    cd.back = back
                    cd.size = size
                    cd.front_enqueue(1000)
                    list_representation[(front - 1) % capacity] = 1000
                    self.assertEqual(list_representation, cd.queue)
                    self.assertEqual((front - 1) % capacity, cd.front)
                    self.assertEqual(back, cd.back)
                    self.assertEqual(size + 1, cd.size)

        # (3) back_enqueue basics
        for capacity in range(4, 50):
            for front in range(capacity):
                for back in range(capacity - 1):  # So grow isn't called upon
                    if front == back:  # Skip, means queue is empty
                        continue
                    list_representation = list(range(capacity))
                    size = back - front + 1 if front < back else capacity - (front - back)
                    if size == capacity - 1:  # Skip, means adding to the queue will make the queue full and then grow
                        continue
                    cd = CircularDeque(list(range(capacity)), capacity)
                    cd.front = front
                    cd.back = back
                    cd.size = size
                    cd.back_enqueue(1000)
                    list_representation[back + 1] = 1000
                    self.assertEqual(list_representation, cd.queue)
                    self.assertEqual(front, cd.front)
                    # self.assertEqual((back + 1) % capacity, cd.back)
                    self.assertEqual(size + 1, cd.size)

    def test_front_enqueue(self):
        cd = CircularDeque()
        for element in range(50):
            cd.front_enqueue(element)
        self.assertEqual(list(range(31, -1, -1)) + [None] * 14 + list(range(49, 31, -1)), cd.queue)

        cd = CircularDeque()
        for element in range(64):
            cd.front_enqueue(element)
        self.assertEqual(list(range(63, -1, -1)) + [None] * 64, cd.queue)

    def test_back_enqueue(self):
        cd = CircularDeque()
        for element in range(50):
            cd.back_enqueue(element)
        self.assertEqual(list(range(50)) + [None] * 14, cd.queue)

        cd = CircularDeque()
        for element in range(64):
            cd.back_enqueue(element)
        self.assertEqual(list(range(64)) + [None] * 64, cd.queue)

    def test_dequeue_basic(self):
        """
        Testing dequed values from any valid CircularQueue configuration.
        :return: None
        """
        def Test_CQ_dequeue_front(cd, ans, size, cap):
            for i in range(size + 1):
                if i > 0:  # checks initial list before dequeing
                    size -= 1
                    self.assertEqual(ans[i - 1], cd.front_dequeue())  # dequeued proper element

                # checks
                self.assertEqual(size, cd.size)  # check decrement size

        def Test_CQ_dequeue_back(cd, ans, size, cap):
            for i in range(size + 1):
                if i > 0:  # checks initial list before dequeing
                    size -= 1
                    self.assertEqual(ans[-1 * i], cd.back_dequeue())  # dequeued proper element

                # checks
                self.assertEqual(size, cd.size)  # check decrement size

        # Test 1
        size, cap = 4, 4
        queue = [1, 2, 3, 4]
        front, back = 0, 3

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, size, cap)
        Test_CQ_dequeue_back(cd_back, ans, size, cap)

        # Test 2
        size, cap = 4, 4
        queue = [1, 2, 3, 4]
        front, back = 0, 3

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, size, cap)
        Test_CQ_dequeue_back(cd_back, ans, size, cap)

        # Test 3
        size, cap = 10, 11
        queue = [10, 11, 12, 13, 14, 15, 16, 17, 18, None, 20]
        front, back = 10, 8

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, size, cap)
        Test_CQ_dequeue_back(cd_back, ans, size, cap)

        # Test 4
        size, cap = 10, 11
        queue = [None, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        front, back = 1, 10

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, size, cap)
        Test_CQ_dequeue_back(cd_back, ans, size, cap)

        # Test 5
        size, cap = 15, 20
        queue = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, None, None, None, None, None, 32, 33]
        front, back = 18, 12

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, size, cap)
        Test_CQ_dequeue_back(cd_back, ans, size, cap)

        # Test 6
        size, cap = 15, 20
        queue = [None, None, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, None, None, None]
        front, back = 2, 16

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, size, cap)
        Test_CQ_dequeue_back(cd_back, ans, size, cap)

        # Test 7
        size, cap = 20, 31
        queue = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, None, None, None, None, None, None,
                 None, None, None, None, None, 46, 47, 48]
        front, back = 28, 16

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, size, cap)
        Test_CQ_dequeue_back(cd_back, ans, size, cap)

    def test_back_dequeue(self):
        """
        Testing wrapping, resizing, capacity, front, back, size, enquing, dequing
        :return: None
        """
        def Check_CQ(ans, size, front, back, cap, cd, b, f=0):
            # checks
            self.assertEqual(size, cd.size)  # check decrement size
            self.assertEqual(size, len(cd))  # check decrement size
            self.assertEqual(back, cd.back)
            self.assertEqual(front, cd.front)  # Front wraps around back of queue
            if size != 0:
                self.assertEqual(ans[f], cd.front_element())
                self.assertEqual(ans[-1 * b - 1], cd.back_element())
            else:
                self.assertEqual(None, cd.front_element())  # empty
                self.assertEqual(None, cd.back_element())  # empty
            self.assertEqual(cap, cd.capacity)  # capacity halves at proper intervals

        def Test_CQ_dequeue_back(cd, ans, front, back, size, cap):
            for i in range(size + 1):
                if i > 0:  # checks initial list before dequeing
                    size -= 1
                    if size <= cap // 4 and cap // 2 >= 4:  # if shrink
                        cap //= 2
                        front = 0  # reset front
                        back = size - 1  # back same until cd shrunk
                    else:
                        back = (back - 1) % cap
                    self.assertEqual(ans[-1 * i], cd.back_dequeue())  # dequeued proper element

                # checks
                Check_CQ(ans, size, front, back, cap, cd, b=i, f=0)

        # Test 1
        size, cap = 4, 4
        queue = [1, 2, 3, 4]
        front, back = 0, 3

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_back = CircularDeque(queue, cap)
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_back(cd_back, ans, cd_back.front, cd_back.back, size, cap)

        # Test 3
        size, cap = 10, 11
        queue = [10, 11, 12, 13, 14, 15, 16, 17, 18, None, 20]
        front, back = 10, 8

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_back(cd_back, ans, cd_back.front, cd_back.back, size, cap)

        # Test 4
        size, cap = 10, 11
        queue = [None, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        front, back = 1, 10

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_back(cd_back, ans, cd_back.front, cd_back.back, size, cap)

        # Test 5
        size, cap = 15, 20
        queue = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, None, None, None, None, None, 32, 33]
        front, back = 18, 12

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_back(cd_back, ans, cd_back.front, cd_back.back, size, cap)

        # Test 6
        size, cap = 15, 20
        queue = [None, None, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, None, None, None]
        front, back = 2, 16

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_back(cd_back, ans, cd_back.front, cd_back.back, size, cap)

        # Test 7
        size, cap = 20, 31
        queue = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, None, None, None, None,
                 None, None,
                 None, None, None, None, None, 46, 47, 48]
        front, back = 28, 16

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_back(cd_back, ans, cd_back.front, cd_back.back, size, cap)

        # Test 8
        size, cap = 20, 31
        queue = [None, None, None, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                 None,
                 None, None, None, None, None, None, None]
        front, back = 3, 22

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_back = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size
        cd_back.front, cd_back.back, cd_back.size = front, back, size

        Test_CQ_dequeue_back(cd_back, ans, cd_back.front, cd_back.back, size, cap)

    def test_front_dequeue(self):
        """
        Testing wrapping, resizing, capacity, front, back, size, enquing, dequing
        :return: None
        """
        def Check_CQ(ans, size, front, back, cap, cd, b, f=0):
            # checks
            self.assertEqual(size, cd.size)  # check decrement size
            self.assertEqual(size, len(cd))  # check decrement size
            self.assertEqual(back, cd.back)
            self.assertEqual(front, cd.front)  # Front wraps around back of queue
            if size != 0:
                self.assertEqual(ans[f], cd.front_element())
                self.assertEqual(ans[-1 * b - 1], cd.back_element())
            else:
                self.assertEqual(None, cd.front_element())  # empty
                self.assertEqual(None, cd.back_element())  # empty
            self.assertEqual(cap, cd.capacity)  # capacity halves at proper intervals

        def Test_CQ_dequeue_front(cd, ans, front, back, size, cap):
            for i in range(size + 1):
                if i > 0:  # checks initial list before dequeing
                    size -= 1
                    if size <= cap // 4 and cap // 2 >= 4:  # if shrink
                        cap //= 2
                        front = 0  # reset front
                        back = size - 1  # back same until cd shrunk
                    else:
                        front = (front + 1) % cap
                    self.assertEqual(ans[i - 1], cd.front_dequeue())  # dequeued proper element

                # checks
                Check_CQ(ans, size, front, back, cap, cd, b=0, f=i)

        # Test 1
        size, cap = 4, 4
        queue = [1, 2, 3, 4]
        front, back = 0, 3

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, cd_front.front, cd_front.back, size, cap)

        # Test 3
        size, cap = 10, 11
        queue = [10, 11, 12, 13, 14, 15, 16, 17, 18, None, 20]
        front, back = 10, 8

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, cd_front.front, cd_front.back, size, cap)

        # Test 4
        size, cap = 10, 11
        queue = [None, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        front, back = 1, 10

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, cd_front.front, cd_front.back, size, cap)

        # Test 5
        size, cap = 15, 20
        queue = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, None, None, None, None, None, 32, 33]
        front, back = 18, 12

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, cd_front.front, cd_front.back, size, cap)

        # Test 6
        size, cap = 15, 20
        queue = [None, None, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, None, None, None]
        front, back = 2, 16

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, cd_front.front, cd_front.back, size, cap)

        # Test 7
        size, cap = 20, 31
        queue = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, None, None, None, None,
                 None, None,
                 None, None, None, None, None, 46, 47, 48]
        front, back = 28, 16

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, cd_front.front, cd_front.back, size, cap)

        # Test 8
        size, cap = 20, 31
        queue = [None, None, None, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                 None,
                 None, None, None, None, None, None, None]
        front, back = 3, 22

        ans = [None] * size
        for i in range(size):
            ans[i] = queue[(front + i) % cap]  # modulus wraps around back of queue]

        cd_front = CircularDeque(queue, cap)
        cd_front.front, cd_front.back, cd_front.size = front, back, size

        Test_CQ_dequeue_front(cd_front, ans, cd_front.front, cd_front.back, size, cap)

    def test_grow(self):
        """
        Tests capacity and values of list while growing
        :return: None
        """
        r_sz = 100
        r_data = [random.randint(-1000, 1000) for val in range(r_sz)]

        # Checks grow via checking new capacity, that the list has been
        # extended, and that the data is properly ordered.
        # Checks ordering by offsetting data so that it can leverage
        # and test circular property without relying on
        # dequeue and enqueue methods.
        cap = 4
        amnt = 6  # log(len(data))
        for offset in range(1, amnt):
            queue = [r_data[j % cap]  # wraps to mimic circularity
                     for j in range((3 * offset), cap + (3 * offset))]

            cd = CircularDeque(queue, cap)  # Fill cd to max capacity
            cd.front, cd.back = (cap + cap - (3 * offset)) % cap, (cap + cap - (3 * offset) - 1) % cap  # correct circular

            queue = r_data[0:cap]  # correct queue order
            queue.extend([None] * cap)  # grow list

            cd.grow()
            cap *= 2  # new expected capacity

            self.assertEqual(cap, cd.capacity)  # check capacity is growing
            self.assertEqual(cd.queue, queue)  # check reordered data like expected

    def test_shrink(self):
        """
        Tests capacity and values of list while shrinking
        :return: None
        """

        r_sz = 100
        r_data = [random.randint(-1000, 1000) for val in range(r_sz)]
        cd = CircularDeque()

        # Checks grow via checking new capacity, that the list has been
        # extended, and that the data is properly ordered.
        # Checks ordering by offsetting data so that it can leverage
        # and test circular property without relying on
        # dequeue and enqueue methods.
        amnt = 6  # log(len(data))
        cap = (2 ** (amnt + 2))  # max capacity
        for offset in range(1, amnt):
            queue = [r_data[(j + (3 * offset)) % (cap // 4)]  # wraps pivot at i in rdata
                     if not (((cap // 4) - (3 * offset)) < j < cap - (3 * offset))  # left shifted
                     else None  # None between start and end
                     for j in range(0, cap)]  # cap * 4 works w/ j % cap
            cd = CircularDeque(queue, cap)  # Fill cd to 1/4 capacity
            cd.front = (cap + cap - (3 * offset)) % cap  # i ints wrapped around
            cd.back = (cap + cap // 4 - (3 * offset) - 1) % cap  # size - i not wrapped
            cd.size //= 4

            queue = r_data[0:(cap // 4)]  # correct queue order
            queue.extend([None] * (cap // 4))  # add extra space

            cd.shrink()
            cap //= 2  # new expected capacity

            self.assertEqual(cap, cd.capacity)  # check capacity is growing
            self.assertEqual(cd.queue, queue)  # check reordered data like expected

