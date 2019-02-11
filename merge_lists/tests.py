from merge import linear_merge0, linear_merge1, linear_merge2, heapq_merge, counter_merge
import unittest
from unittest.mock import patch, MagicMock


class TestMerge(unittest.TestCase):
    def test_one(self):
        list1 = [1, 3, 7, 9]
        list2 = [2, 4, 6, 8]
        res = [1,2,3,4,6,7,8,9]
        self.assertEqual(linear_merge0(list1, list2), res)
        self.assertEqual(linear_merge1(list1, list2), res)
        self.assertEqual(linear_merge2(list1, list2), res)
        self.assertEqual(heapq_merge(list1, list2), res)
        self.assertEqual(counter_merge(list1, list2), res)

    def test_two(self):
        list1 = [1, 1, 1, 1]
        list2 = [2, 2, 2, 2]
        res = [1,1,1,1,2,2,2,2]
        self.assertEqual(linear_merge0(list1, list2), res)
        self.assertEqual(linear_merge1(list1, list2), res)
        self.assertEqual(linear_merge2(list1, list2), res)
        self.assertEqual(heapq_merge(list1, list2), res)
        self.assertEqual(counter_merge(list1, list2), res)

    def test_three(self):
        list1 = [1, 2, 2, 2]
        list2 = [2, 2, 2, 2]
        res = [1,2,2,2,2,2,2,2]
        self.assertEqual(linear_merge0(list1, list2), res)
        self.assertEqual(linear_merge1(list1, list2), res)
        self.assertEqual(linear_merge2(list1, list2), res)
        self.assertEqual(heapq_merge(list1, list2), res)
        self.assertEqual(counter_merge(list1, list2), res)

    def test_four(self):
        list1 = [2, 2, 2, 2]
        list2 = [2, 2, 2, 2]
        res = [2,2,2,2,2,2,2,2]
        self.assertEqual(linear_merge0(list1, list2), res)
        self.assertEqual(linear_merge1(list1, list2), res)
        self.assertEqual(linear_merge2(list1, list2), res)
        self.assertEqual(heapq_merge(list1, list2), res)
        self.assertEqual(counter_merge(list1, list2), res)

    def test_five(self):
        list1 = [1, 20, 30, 40]
        list2 = [1, 10, 12, 21]
        res = [1,1,10,12,20,21,30,40]
        self.assertEqual(linear_merge0(list1, list2), res)
        self.assertEqual(linear_merge1(list1, list2), res)
        self.assertEqual(linear_merge2(list1, list2), res)
        self.assertEqual(heapq_merge(list1, list2), res)
        self.assertEqual(counter_merge(list1, list2), res)

    def test_six(self):
        list1 = [1, 20]
        list2 = [1, 10, 12, 21]
        res = [1,1,10,12,20,21]
        self.assertEqual(linear_merge0(list1, list2), res)
        self.assertEqual(linear_merge1(list1, list2), res)
        self.assertEqual(linear_merge2(list1, list2), res)
        self.assertEqual(heapq_merge(list1, list2), res)
        self.assertEqual(counter_merge(list1, list2), res)

    def test_seven(self):
        list1 = [1, 20]
        list2 = [2, 10, 12, 19]
        res = [1,2,10,12,19,20]
        self.assertEqual(linear_merge0(list1, list2), res)
        self.assertEqual(linear_merge1(list1, list2), res)
        self.assertEqual(linear_merge2(list1, list2), res)
        self.assertEqual(heapq_merge(list1, list2), res)
        self.assertEqual(counter_merge(list1, list2), res)


if __name__ == '__main__':
    unittest.main()
