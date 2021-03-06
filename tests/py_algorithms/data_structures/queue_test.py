import copy
from typing import List

import pytest

from py_algorithms.data_structures import new_queue


@pytest.fixture
def collection() -> List[int]:
    return [0, 6, 7, 8, 9, 4, 5, 12]


class TestQueue:
    def test_properties(self):
        items = collection()
        queue = new_queue(copy.deepcopy(items))
        assert queue.is_empty() is False
        assert queue.size == len(items)

    def test_pop(self):
        items = collection()
        queue = new_queue(copy.deepcopy(items))
        for _ in range(0, len(items) - 1):
            queue.pop()
        assert queue.next == items[len(items) - 1]

    def test_pop_push(self):
        queue = new_queue()
        queue.push(10)
        assert queue.next == 10
        assert queue.pop() == 10

    def test_corner_cases(self):
        queue = new_queue()
        assert queue.pop() is None
        queue.push(1)
        queue.pop()
        assert queue.pop() is None
