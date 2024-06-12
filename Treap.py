
import random
class TreapNode:
    def __init__(self, key, priority, value=0):
        self.key = key
        self.priority = priority
        self.value = value
        self.sum = value
        self.count = {value: 1}
        self.left = None
        self.right = None

class Treap:
    def __init__(self):
        self.root = None

    def _update(self, node):
        if not node:
            return
        node.sum = node.value
        node.count = {node.value: 1}
        if node.left:
            node.sum += node.left.sum
            for k, v in node.left.count.items():
                if k in node.count:
                    node.count[k] += v
                else:
                    node.count[k] = v
        if node.right:
            node.sum += node.right.sum
            for k, v in node.right.count.items():
                if k in node.count:
                    node.count[k] += v
                else:
                    node.count[k] = v

    def _split(self, node, key):
        if not node:
            return None, None
        elif key < node.key:
            left, node.left = self._split(node.left, key)
            self._update(node)
            return left, node
        else:
            node.right, right = self._split(node.right, key)
            self._update(node)
            return node, right

    def _merge(self, left, right):
        if not left or not right:
            return left or right
        elif left.priority > right.priority:
            left.right = self._merge(left.right, right)
            self._update(left)
            return left
        else:
            right.left = self._merge(left, right.left)
            self._update(right)
            return right

    def insert(self, key, value):
        priority = random.random()
        new_node = TreapNode(key, priority, value)
        if not self.root:
            self.root = new_node
        else:
            left, right = self._split(self.root, key)
            self.root = self._merge(self._merge(left, new_node), right)

    def _erase(self, node, key):
        if not node:
            return None
        elif key < node.key:
            node.left = self._erase(node.left, key)
        elif key > node.key:
            node.right = self._erase(node.right, key)
        else:
            node = self._merge(node.left, node.right)
        if node:
            self._update(node)
        return node

    def erase(self, key):
        self.root = self._erase(self.root, key)

    def _range_query(self, node, L, R):
        if not node:
            return 0
        if node.key < L:
            return self._range_query(node.right, L, R)
        elif node.key > R:
            return self._range_query(node.left, L, R)
        else:
            left_sum = self._range_query(node.left, L, R)
            right_sum = self._range_query(node.right, L, R)
            return left_sum + node.value + right_sum

    def range_sum(self, L, R):
        return self._range_query(self.root, L, R)

    def _range_min(self, node, L, R):
        if not node:
            return float('inf')
        if node.key < L:
            return self._range_min(node.right, L, R)
        elif node.key > R:
            return self._range_min(node.left, L, R)
        else:
            left_min = self._range_min(node.left, L, R)
            right_min = self._range_min(node.right, L, R)
            return min(left_min, node.value, right_min)

    def range_min(self, L, R):
        return self._range_min(self.root, L, R)

    def _range_max(self, node, L, R):
        if not node:
            return -float('inf')
        if node.key < L:
            return self._range_max(node.right, L, R)
        elif node.key > R:
            return self._range_max(node.left, L, R)
        else:
            left_max = self._range_max(node.left, L, R)
            right_max = self._range_max(node.right, L, R)
            return max(left_max, node.value, right_max)

    def range_max(self, L, R):
        return self._range_max(self.root, L, R)

    def _range_count(self, node, L, R, value):
        if not node:
            return 0
        if node.key < L:
            return self._range_count(node.right, L, R, value)
        elif node.key > R:
            return self._range_count(node.left, L, R, value)
        else:
            left_count = self._range_count(node.left, L, R, value)
            right_count = self._range_count(node.right, L, R, value)
            return left_count + (1 if node.value == value else 0) + right_count

    def range_count(self, L, R, value):
        return self._range_count(self.root, L, R, value)

