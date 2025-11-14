import os
from datetime import datetime, timedelta
from calendar import monthrange

# Common Python error challenges
common_errors = [
    # Mutable default arguments
    {
        "code": "def append_item(item, lst=[]):\n    lst.append(item)\n    return lst\n\nprint(append_item(1))\nprint(append_item(2))",
        "options": ["A. [1]\\n[2]", "B. [1]\\n[1, 2]", "C. [1, 2]\\n[1, 2]", "D. Error"],
        "answer": "B",
        "explanation": "Mutable default arguments are shared across function calls."
    },
    # Variable scope
    {
        "code": "x = 10\n\ndef func():\n    print(x)\n    x = 20\n\nfunc()",
        "options": ["A. 10", "B. 20", "C. UnboundLocalError", "D. None"],
        "answer": "C",
        "explanation": "Local variable x is referenced before assignment."
    },
    # List comprehension scope
    {
        "code": "x = [i for i in range(3)]\nprint(i)",
        "options": ["A. 2", "B. 3", "C. NameError", "D. [0, 1, 2]"],
        "answer": "A",
        "explanation": "In Python 3, list comprehension variables leak to outer scope."
    },
    # String immutability
    {
        "code": "s = 'hello'\ns[0] = 'H'\nprint(s)",
        "options": ["A. Hello", "B. hello", "C. TypeError", "D. H"],
        "answer": "C",
        "explanation": "Strings are immutable in Python."
    },
    # Integer caching
    {
        "code": "a = 256\nb = 256\nprint(a is b)\nc = 257\nd = 257\nprint(c is d)",
        "options": ["A. True\\nTrue", "B. True\\nFalse", "C. False\\nFalse", "D. Error"],
        "answer": "B",
        "explanation": "Python caches integers from -5 to 256."
    },
    # Dictionary key order (Python 3.7+)
    {
        "code": "d = {}\nd[1] = 'a'\nd[2] = 'b'\nprint(list(d.keys()))",
        "options": ["A. [1, 2]", "B. [2, 1]", "C. Random order", "D. Error"],
        "answer": "A",
        "explanation": "Python 3.7+ maintains insertion order in dictionaries."
    },
    # Tuple unpacking
    {
        "code": "a, b = [1, 2, 3]\nprint(a, b)",
        "options": ["A. 1 2", "B. ValueError", "C. [1, 2] [3]", "D. 1 [2, 3]"],
        "answer": "B",
        "explanation": "Too many values to unpack."
    },
    # Modifying list while iterating
    {
        "code": "lst = [1, 2, 3, 4]\nfor i in lst:\n    if i % 2 == 0:\n        lst.remove(i)\nprint(lst)",
        "options": ["A. [1, 3]", "B. [1, 2, 3, 4]", "C. [2, 4]", "D. Error"],
        "answer": "B",
        "explanation": "Modifying list while iterating can skip elements."
    },
    # is vs ==
    {
        "code": "a = [1, 2]\nb = [1, 2]\nprint(a == b, a is b)",
        "options": ["A. True True", "B. True False", "C. False True", "D. False False"],
        "answer": "B",
        "explanation": "== compares values, is compares identity."
    },
    # Scope and global
    {
        "code": "count = 0\n\ndef increment():\n    count += 1\n    return count\n\nprint(increment())",
        "options": ["A. 1", "B. 0", "C. UnboundLocalError", "D. NameError"],
        "answer": "C",
        "explanation": "Need 'global count' to modify global variable."
    },
    # Set operations
    {
        "code": "s1 = {1, 2, 3}\ns2 = {3, 4, 5}\nprint(s1 - s2)",
        "options": ["A. {1, 2}", "B. {4, 5}", "C. {1, 2, 3, 4, 5}", "D. Error"],
        "answer": "A",
        "explanation": "- operator returns difference (elements in s1 not in s2)."
    },
    # String slicing
    {
        "code": "s = 'Python'\nprint(s[1:4:2])",
        "options": ["A. yt", "B. yth", "C. yh", "D. Error"],
        "answer": "C",
        "explanation": "Slice from index 1 to 4 with step 2."
    },
    # Dictionary get vs indexing
    {
        "code": "d = {1: 'a'}\nprint(d.get(2, 'default'), d[2])",
        "options": ["A. default default", "B. default KeyError", "C. None default", "D. Error"],
        "answer": "B",
        "explanation": "get() returns default, [] raises KeyError."
    },
    # List copy
    {
        "code": "a = [[1, 2], [3, 4]]\nb = a.copy()\nb[0][0] = 99\nprint(a)",
        "options": ["A. [[1, 2], [3, 4]]", "B. [[99, 2], [3, 4]]", "C. Error", "D. [[99, 2]]"],
        "answer": "B",
        "explanation": "copy() is shallow, nested lists are shared."
    },
    # Generator exhaustion
    {
        "code": "gen = (i for i in range(3))\nprint(list(gen))\nprint(list(gen))",
        "options": ["A. [0,1,2]\\n[0,1,2]", "B. [0,1,2]\\n[]", "C. Error", "D. [0,1,2]\\nNone"],
        "answer": "B",
        "explanation": "Generators are exhausted after first iteration."
    },
    # Type coercion
    {
        "code": "print(3 + '3')",
        "options": ["A. 6", "B. '33'", "C. TypeError", "D. '6'"],
        "answer": "C",
        "explanation": "Cannot add int and str without conversion."
    },
    # Boolean evaluation
    {
        "code": "print(0 or 1 and 2)",
        "options": ["A. 0", "B. 1", "C. 2", "D. True"],
        "answer": "C",
        "explanation": "and has higher precedence than or."
    },
    # Range behavior
    {
        "code": "print(list(range(5, 2)))",
        "options": ["A. [5, 4, 3]", "B. [5, 4, 3, 2]", "C. []", "D. Error"],
        "answer": "C",
        "explanation": "range(5, 2) is empty (start > stop with step 1)."
    },
    # String methods
    {
        "code": "s = 'Hello World'\nprint(s.split('l'))",
        "options": ["A. ['He', 'o Wor', 'd']", "B. ['Hel', 'lo Wor', 'ld']", "C. ['He', '', 'o Wor', 'd']", "D. Error"],
        "answer": "C",
        "explanation": "split() includes empty strings between consecutive delimiters."
    },
    # Dictionary comprehension
    {
        "code": "d = {i: i*2 for i in range(3)}\nprint(d)",
        "options": ["A. {0: 0, 1: 2, 2: 4}", "B. {0, 2, 4}", "C. [0, 2, 4]", "D. Error"],
        "answer": "A",
        "explanation": "Dictionary comprehension creates key-value pairs."
    },
    # Enumerate
    {
        "code": "for i, val in enumerate(['a', 'b'], 1):\n    print(i, val)",
        "options": ["A. 0 a\\n1 b", "B. 1 a\\n2 b", "C. (0, 'a')\\n(1, 'b')", "D. Error"],
        "answer": "B",
        "explanation": "enumerate(iterable, start) starts counting from start."
    },
]

# Class-related challenges
class_challenges = [
    # Class vs instance variables
    {
        "code": "class MyClass:\n    class_var = 0\n    \n    def __init__(self):\n        self.instance_var = 0\n\nobj1 = MyClass()\nobj2 = MyClass()\nobj1.class_var = 1\nobj1.instance_var = 1\nprint(obj2.class_var, obj2.instance_var)",
        "options": ["A. 0 0", "B. 1 0", "C. 1 1", "D. 0 1"],
        "answer": "A",
        "explanation": "obj1.class_var = 1 creates an instance variable, not modifying the class variable. obj2.class_var still refers to the original class variable."
    },
    # Mutable class variables
    {
        "code": "class Counter:\n    count = []\n    \n    def add(self, item):\n        self.count.append(item)\n\nc1 = Counter()\nc2 = Counter()\nc1.add(1)\nprint(c2.count)",
        "options": ["A. []", "B. [1]", "C. Error", "D. None"],
        "answer": "B",
        "explanation": "Mutable class variables are shared across all instances. Modifying through one instance affects all."
    },
    # self parameter
    {
        "code": "class Test:\n    def method(self):\n        return 'called'\n\nt = Test()\nprint(Test.method(t))",
        "options": ["A. called", "B. Error", "C. None", "D. <bound method>"],
        "answer": "A",
        "explanation": "You can call instance methods by passing the instance as the first argument to the class method."
    },
    # __init__ return
    {
        "code": "class Test:\n    def __init__(self):\n        return 'hello'\n\nt = Test()\nprint(t)",
        "options": ["A. hello", "B. <__main__.Test object>", "C. TypeError", "D. None"],
        "answer": "C",
        "explanation": "__init__ cannot return a value (except None). Returning anything else raises TypeError."
    },
    # Private attributes (name mangling)
    {
        "code": "class Test:\n    def __init__(self):\n        self.__private = 10\n        self.public = 20\n\nt = Test()\nprint(t.__private)",
        "options": ["A. 10", "B. 20", "C. AttributeError", "D. None"],
        "answer": "C",
        "explanation": "Names starting with __ are name-mangled. Access via t._Test__private, not t.__private."
    },
    # Class method vs static method
    {
        "code": "class MyClass:\n    x = 10\n    \n    @classmethod\n    def class_method(cls):\n        return cls.x\n    \n    @staticmethod\n    def static_method():\n        return MyClass.x\n\nprint(MyClass.class_method(), MyClass.static_method())",
        "options": ["A. 10 10", "B. Error", "C. None None", "D. <bound method> <function>"],
        "answer": "A",
        "explanation": "Both can access class variables. classmethod receives cls, staticmethod doesn't receive self or cls."
    },
    # Inheritance and method resolution
    {
        "code": "class A:\n    def method(self):\n        return 'A'\n\nclass B(A):\n    def method(self):\n        return 'B'\n\nclass C(A):\n    pass\n\nb = B()\nc = C()\nprint(b.method(), c.method())",
        "options": ["A. B A", "B. A B", "C. B B", "D. Error"],
        "answer": "A",
        "explanation": "B overrides method() from A, so b.method() returns 'B'. C doesn't override, so c.method() returns 'A'."
    },
    # Multiple inheritance MRO
    {
        "code": "class A:\n    def method(self):\n        return 'A'\n\nclass B(A):\n    def method(self):\n        return 'B'\n\nclass C(A):\n    def method(self):\n        return 'C'\n\nclass D(B, C):\n    pass\n\nd = D()\nprint(d.method())",
        "options": ["A. A", "B. B", "C. C", "D. Error"],
        "answer": "B",
        "explanation": "Method Resolution Order (MRO) follows D -> B -> C -> A. B's method is found first."
    },
    # Property decorator
    {
        "code": "class Circle:\n    def __init__(self, radius):\n        self._radius = radius\n    \n    @property\n    def radius(self):\n        return self._radius\n    \n    @radius.setter\n    def radius(self, value):\n        if value < 0:\n            raise ValueError\n        self._radius = value\n\nc = Circle(5)\nc.radius = -1\nprint(c.radius)",
        "options": ["A. -1", "B. 5", "C. ValueError", "D. AttributeError"],
        "answer": "C",
        "explanation": "The setter validates input and raises ValueError for negative values."
    },
    # __str__ vs __repr__
    {
        "code": "class Point:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n    \n    def __str__(self):\n        return f'({self.x}, {self.y})'\n    \n    def __repr__(self):\n        return f'Point({self.x}, {self.y})'\n\np = Point(1, 2)\nprint(str(p), repr(p))",
        "options": ["A. (1, 2) (1, 2)", "B. (1, 2) Point(1, 2)", "C. Point(1, 2) (1, 2)", "D. Error"],
        "answer": "B",
        "explanation": "__str__ is for user-friendly output, __repr__ is for developer representation (ideally can recreate object)."
    },
    # Class variable access
    {
        "code": "class Test:\n    x = 10\n    \n    def __init__(self):\n        self.x = 20\n\nt = Test()\nprint(t.x, Test.x)",
        "options": ["A. 10 10", "B. 20 20", "C. 20 10", "D. 10 20"],
        "answer": "C",
        "explanation": "Instance variable self.x shadows class variable Test.x. Instance gets 20, class still has 10."
    },
    # super() usage
    {
        "code": "class A:\n    def method(self):\n        return 'A'\n\nclass B(A):\n    def method(self):\n        return super().method() + 'B'\n\nb = B()\nprint(b.method())",
        "options": ["A. A", "B. AB", "C. B", "D. Error"],
        "answer": "B",
        "explanation": "super() calls the parent class method, so it returns 'A' + 'B' = 'AB'."
    },
    # __getattr__ vs __getattribute__
    {
        "code": "class Test:\n    def __getattr__(self, name):\n        return f'Missing: {name}'\n\nt = Test()\nprint(t.x, t.y)",
        "options": ["A. Missing: x Missing: y", "B. AttributeError", "C. None None", "D. Error"],
        "answer": "A",
        "explanation": "__getattr__ is called only when attribute is not found through normal lookup."
    },
    # Class decorators
    {
        "code": "def add_method(cls):\n    cls.new_method = lambda self: 'added'\n    return cls\n\n@add_method\nclass Test:\n    pass\n\nt = Test()\nprint(t.new_method())",
        "options": ["A. added", "B. Error", "C. None", "D. <lambda>"],
        "answer": "A",
        "explanation": "Class decorators can modify or add attributes to a class before it's used."
    },
    # __slots__
    {
        "code": "class Test:\n    __slots__ = ['x', 'y']\n    \n    def __init__(self):\n        self.x = 1\n        self.y = 2\n\nt = Test()\nt.z = 3\nprint(t.z)",
        "options": ["A. 3", "B. AttributeError", "C. None", "D. Error"],
        "answer": "B",
        "explanation": "__slots__ restricts instance attributes to only those listed. Adding 'z' raises AttributeError."
    },
    # Descriptors
    {
        "code": "class Descriptor:\n    def __get__(self, obj, objtype=None):\n        return 'get'\n    \n    def __set__(self, obj, value):\n        print(f'set: {value}')\n\nclass Test:\n    attr = Descriptor()\n\nt = Test()\nprint(t.attr)\nt.attr = 10",
        "options": ["A. get\\nset: 10", "B. get\\n10", "C. Error", "D. None\\nset: 10"],
        "answer": "A",
        "explanation": "Descriptors control attribute access. __get__ is called on access, __set__ on assignment."
    },
    # Abstract base class
    {
        "code": "from abc import ABC, abstractmethod\n\nclass Shape(ABC):\n    @abstractmethod\n    def area(self):\n        pass\n\nclass Circle(Shape):\n    def __init__(self, r):\n        self.r = r\n\nc = Circle(5)\nprint(c.area())",
        "options": ["A. 0", "B. TypeError", "C. None", "D. 25"],
        "answer": "B",
        "explanation": "Circle doesn't implement abstract method area(), so instantiating Circle raises TypeError."
    },
    # Operator overloading
    {
        "code": "class Vector:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n    \n    def __add__(self, other):\n        return Vector(self.x + other.x, self.y + other.y)\n    \n    def __str__(self):\n        return f'({self.x}, {self.y})'\n\nv1 = Vector(1, 2)\nv2 = Vector(3, 4)\nprint(v1 + v2)",
        "options": ["A. (4, 6)", "B. (1, 2)", "C. Error", "D. <Vector object>"],
        "answer": "A",
        "explanation": "__add__ overloads the + operator. v1 + v2 calls v1.__add__(v2), returning a new Vector."
    },
    # __call__ method
    {
        "code": "class Callable:\n    def __init__(self, value):\n        self.value = value\n    \n    def __call__(self, x):\n        return self.value + x\n\nc = Callable(10)\nprint(c(5))",
        "options": ["A. 15", "B. 10", "C. 5", "D. TypeError"],
        "answer": "A",
        "explanation": "__call__ makes instances callable like functions. c(5) calls c.__call__(5)."
    },
    # Class method accessing instance
    {
        "code": "class Test:\n    @classmethod\n    def method(cls):\n        return cls.x\n    \n    x = 10\n\nt = Test()\nprint(t.method())",
        "options": ["A. 10", "B. AttributeError", "C. None", "D. Error"],
        "answer": "A",
        "explanation": "Class methods can access class variables via cls parameter. cls.x refers to Test.x."
    },
    # Method binding
    {
        "code": "class Test:\n    def method(self):\n        return self\n\nt = Test()\nunbound = Test.method\nbound = t.method\nprint(unbound is bound)",
        "options": ["A. True", "B. False", "C. Error", "D. None"],
        "answer": "B",
        "explanation": "Unbound method (class.method) and bound method (instance.method) are different objects."
    },
]

# LeetCode-style problems
leetcode_problems = [
    {
        "title": "Two Sum",
        "code": "# Given an array of integers nums and an integer target,\n# return indices of the two numbers that add up to target.\n# Example: nums = [2,7,11,15], target = 9\n# Answer: [0, 1] because nums[0] + nums[1] = 2 + 7 = 9",
        "solution": "def two_sum(nums, target):\n    seen = {}\n    for i, num in enumerate(nums):\n        complement = target - num\n        if complement in seen:\n            return [seen[complement], i]\n        seen[num] = i\n    return []",
        "explanation": "Use a hash map to store each number and its index. For each number, check if its complement (target - num) exists in the map. Time: O(n), Space: O(n)."
    },
    {
        "title": "Reverse String",
        "code": "# Write a function that reverses a string.\n# Example: 'hello' -> 'olleh'",
        "solution": "def reverse_string(s):\n    return s[::-1]\n\n# Or using two pointers:\ndef reverse_string(s):\n    s = list(s)\n    left, right = 0, len(s) - 1\n    while left < right:\n        s[left], s[right] = s[right], s[left]\n        left += 1\n        right -= 1\n    return ''.join(s)",
        "explanation": "Use slicing [::-1] for simplicity, or two-pointer technique. Time: O(n), Space: O(1) for two-pointer, O(n) for slicing."
    },
    {
        "title": "Valid Parentheses",
        "code": "# Given a string containing just '(', ')', '{', '}', '[' and ']',\n# determine if the input string is valid.\n# Example: '()[]{}' -> True, '([)]' -> False",
        "solution": "def is_valid(s):\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            if not stack or stack.pop() != mapping[char]:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
        "explanation": "Use a stack to track opening brackets. When encountering a closing bracket, check if it matches the most recent opening bracket. Time: O(n), Space: O(n)."
    },
    {
        "title": "Maximum Subarray",
        "code": "# Find the contiguous subarray with the largest sum.\n# Example: [-2,1,-3,4,-1,2,1,-5,4] -> 6 (subarray [4,-1,2,1])",
        "solution": "def max_subarray(nums):\n    max_sum = current_sum = nums[0]\n    for num in nums[1:]:\n        current_sum = max(num, current_sum + num)\n        max_sum = max(max_sum, current_sum)\n    return max_sum",
        "explanation": "Kadane's algorithm: keep track of maximum sum ending at current position. Time: O(n), Space: O(1)."
    },
    {
        "title": "Contains Duplicate",
        "code": "# Given an array of integers, return True if any value appears at least twice.\n# Example: [1,2,3,1] -> True",
        "solution": "def contains_duplicate(nums):\n    return len(nums) != len(set(nums))",
        "explanation": "Convert to set and compare lengths. If lengths differ, there are duplicates. Time: O(n), Space: O(n)."
    },
    {
        "title": "Best Time to Buy and Sell Stock",
        "code": "# Find the maximum profit from buying and selling stock.\n# Example: [7,1,5,3,6,4] -> 5 (buy at 1, sell at 6)",
        "solution": "def max_profit(prices):\n    min_price = float('inf')\n    max_profit = 0\n    for price in prices:\n        min_price = min(min_price, price)\n        max_profit = max(max_profit, price - min_price)\n    return max_profit",
        "explanation": "Track minimum price seen so far and maximum profit. Time: O(n), Space: O(1)."
    },
    {
        "title": "Palindrome Number",
        "code": "# Determine if an integer is a palindrome.\n# Example: 121 -> True, -121 -> False",
        "solution": "def is_palindrome(x):\n    if x < 0:\n        return False\n    return str(x) == str(x)[::-1]\n\n# Without converting to string:\ndef is_palindrome(x):\n    if x < 0 or (x % 10 == 0 and x != 0):\n        return False\n    reverted = 0\n    while x > reverted:\n        reverted = reverted * 10 + x % 10\n        x //= 10\n    return x == reverted or x == reverted // 10",
        "explanation": "Convert to string and reverse, or reverse half the number mathematically. Time: O(log n), Space: O(1) for math approach."
    },
    {
        "title": "Remove Duplicates from Sorted Array",
        "code": "# Remove duplicates in-place, return new length.\n# Example: [1,1,2] -> length 2, array becomes [1,2,_]",
        "solution": "def remove_duplicates(nums):\n    if not nums:\n        return 0\n    write_index = 1\n    for i in range(1, len(nums)):\n        if nums[i] != nums[i-1]:\n            nums[write_index] = nums[i]\n            write_index += 1\n    return write_index",
        "explanation": "Two-pointer technique: one pointer for reading, one for writing unique elements. Time: O(n), Space: O(1)."
    },
    {
        "title": "Single Number",
        "code": "# Find the single number that appears once (others appear twice).\n# Example: [2,2,1] -> 1",
        "solution": "def single_number(nums):\n    result = 0\n    for num in nums:\n        result ^= num\n    return result",
        "explanation": "XOR all numbers. XOR of same numbers is 0, XOR with 0 is the number itself. Time: O(n), Space: O(1)."
    },
    {
        "title": "Climbing Stairs",
        "code": "# Count ways to climb n stairs (1 or 2 steps at a time).\n# Example: n=3 -> 3 ways (1+1+1, 1+2, 2+1)",
        "solution": "def climb_stairs(n):\n    if n <= 2:\n        return n\n    a, b = 1, 2\n    for _ in range(3, n + 1):\n        a, b = b, a + b\n    return b",
        "explanation": "Fibonacci sequence: ways(n) = ways(n-1) + ways(n-2). Use dynamic programming with O(1) space. Time: O(n), Space: O(1)."
    },
    {
        "title": "Merge Sorted Arrays",
        "code": "# Merge two sorted arrays in-place.\n# nums1 has enough space at the end for nums2.\n# Example: nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3\n# Result: [1,2,2,3,5,6]",
        "solution": "def merge(nums1, m, nums2, n):\n    i, j, k = m - 1, n - 1, m + n - 1\n    while j >= 0:\n        if i >= 0 and nums1[i] > nums2[j]:\n            nums1[k] = nums1[i]\n            i -= 1\n        else:\n            nums1[k] = nums2[j]\n            j -= 1\n        k -= 1",
        "explanation": "Start from the end of both arrays and merge backwards. Time: O(m+n), Space: O(1)."
    },
    {
        "title": "Plus One",
        "code": "# Increment a number represented as array of digits.\n# Example: [1,2,3] -> [1,2,4], [9,9] -> [1,0,0]",
        "solution": "def plus_one(digits):\n    for i in range(len(digits) - 1, -1, -1):\n        if digits[i] < 9:\n            digits[i] += 1\n            return digits\n        digits[i] = 0\n    return [1] + digits",
        "explanation": "Process from right to left. If digit < 9, increment and return. If 9, set to 0 and continue. If all 9s, prepend 1. Time: O(n), Space: O(1)."
    },
    {
        "title": "Sqrt(x)",
        "code": "# Compute square root of x (integer part only).\n# Example: 4 -> 2, 8 -> 2",
        "solution": "def my_sqrt(x):\n    if x < 2:\n        return x\n    left, right = 1, x // 2\n    while left <= right:\n        mid = (left + right) // 2\n        if mid * mid == x:\n            return mid\n        elif mid * mid < x:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return right",
        "explanation": "Binary search between 1 and x//2. Time: O(log x), Space: O(1)."
    },
    {
        "title": "Length of Last Word",
        "code": "# Return length of last word in string.\n# Example: 'Hello World' -> 5",
        "solution": "def length_of_last_word(s):\n    return len(s.strip().split()[-1])",
        "explanation": "Strip whitespace, split by spaces, get last element's length. Time: O(n), Space: O(n)."
    },
    {
        "title": "Add Binary",
        "code": "# Add two binary strings.\n# Example: '11' + '1' -> '100'",
        "solution": "def add_binary(a, b):\n    result = []\n    carry = 0\n    i, j = len(a) - 1, len(b) - 1\n    while i >= 0 or j >= 0 or carry:\n        total = carry\n        if i >= 0:\n            total += int(a[i])\n            i -= 1\n        if j >= 0:\n            total += int(b[j])\n            j -= 1\n        result.append(str(total % 2))\n        carry = total // 2\n    return ''.join(reversed(result))",
        "explanation": "Add from right to left with carry, similar to decimal addition. Time: O(max(len(a), len(b))), Space: O(max(len(a), len(b)))."
    },
    {
        "title": "Remove Element",
        "code": "# Remove all instances of val in-place, return new length.\n# Example: [3,2,2,3], val=3 -> length 2, array becomes [2,2,_,_]",
        "solution": "def remove_element(nums, val):\n    write_index = 0\n    for num in nums:\n        if num != val:\n            nums[write_index] = num\n            write_index += 1\n    return write_index",
        "explanation": "Two-pointer: overwrite elements not equal to val. Time: O(n), Space: O(1)."
    },
    {
        "title": "Search Insert Position",
        "code": "# Find index where target should be inserted in sorted array.\n# Example: [1,3,5,6], target=5 -> 2",
        "solution": "def search_insert(nums, target):\n    left, right = 0, len(nums)\n    while left < right:\n        mid = (left + right) // 2\n        if nums[mid] < target:\n            left = mid + 1\n        else:\n            right = mid\n    return left",
        "explanation": "Binary search for insertion point. Time: O(log n), Space: O(1)."
    },
    {
        "title": "Count and Say",
        "code": "# Generate nth term of count-and-say sequence.\n# Example: n=4 -> '1211' (one 1, one 2, two 1s)",
        "solution": "def count_and_say(n):\n    if n == 1:\n        return '1'\n    prev = count_and_say(n - 1)\n    result = []\n    count = 1\n    for i in range(1, len(prev)):\n        if prev[i] == prev[i-1]:\n            count += 1\n        else:\n            result.append(str(count) + prev[i-1])\n            count = 1\n    result.append(str(count) + prev[-1])\n    return ''.join(result)",
        "explanation": "Recursively generate previous term, then count consecutive digits. Time: O(2^n), Space: O(2^n)."
    },
    {
        "title": "Longest Common Prefix",
        "code": "# Find longest common prefix among array of strings.\n# Example: ['flower','flow','flight'] -> 'fl'",
        "solution": "def longest_common_prefix(strs):\n    if not strs:\n        return ''\n    prefix = strs[0]\n    for s in strs[1:]:\n        while not s.startswith(prefix):\n            prefix = prefix[:-1]\n            if not prefix:\n                return ''\n    return prefix",
        "explanation": "Start with first string as prefix, shorten it until it matches all strings. Time: O(S) where S is sum of all characters, Space: O(1)."
    },
    {
        "title": "Roman to Integer",
        "code": "# Convert Roman numeral to integer.\n# Example: 'IV' -> 4, 'LVIII' -> 58",
        "solution": "def roman_to_int(s):\n    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}\n    total = 0\n    prev = 0\n    for char in reversed(s):\n        value = values[char]\n        if value < prev:\n            total -= value\n        else:\n            total += value\n        prev = value\n    return total",
        "explanation": "Process from right to left. If current value < previous, subtract; otherwise add. Time: O(n), Space: O(1)."
    },
    {
        "title": "Valid Anagram",
        "code": "# Check if two strings are anagrams.\n# Example: 'anagram' and 'nagaram' -> True",
        "solution": "def is_anagram(s, t):\n    return sorted(s) == sorted(t)\n\n# Or using Counter:\nfrom collections import Counter\ndef is_anagram(s, t):\n    return Counter(s) == Counter(t)",
        "explanation": "Sort both strings and compare, or count character frequencies. Time: O(n log n) for sort, O(n) for Counter. Space: O(n)."
    },
    {
        "title": "First Unique Character",
        "code": "# Find index of first non-repeating character.\n# Example: 'leetcode' -> 0 (l is first unique)",
        "solution": "def first_uniq_char(s):\n    from collections import Counter\n    count = Counter(s)\n    for i, char in enumerate(s):\n        if count[char] == 1:\n            return i\n    return -1",
        "explanation": "Count character frequencies, then find first character with count 1. Time: O(n), Space: O(n)."
    },
    {
        "title": "Reverse Integer",
        "code": "# Reverse digits of an integer.\n# Example: 123 -> 321, -123 -> -321",
        "solution": "def reverse(x):\n    sign = -1 if x < 0 else 1\n    x = abs(x)\n    reversed_num = 0\n    while x > 0:\n        reversed_num = reversed_num * 10 + x % 10\n        x //= 10\n    reversed_num *= sign\n    if reversed_num < -2**31 or reversed_num > 2**31 - 1:\n        return 0\n    return reversed_num",
        "explanation": "Extract digits from right to left, build reversed number. Check for 32-bit integer overflow. Time: O(log n), Space: O(1)."
    },
    {
        "title": "Implement strStr()",
        "code": "# Find first occurrence of needle in haystack.\n# Example: haystack='hello', needle='ll' -> 2",
        "solution": "def str_str(haystack, needle):\n    if not needle:\n        return 0\n    for i in range(len(haystack) - len(needle) + 1):\n        if haystack[i:i+len(needle)] == needle:\n            return i\n    return -1",
        "explanation": "Sliding window: check each position if substring matches needle. Time: O(n*m), Space: O(1)."
    },
]

def get_last_day_of_month(year, month):
    return monthrange(year, month)[1]

def is_special_day(day, month, year):
    last_day = get_last_day_of_month(year, month)
    return day == 15 or day == last_day

def is_class_day(day):
    return day in [4, 8, 12, 28]

def generate_file(date, challenge_num):
    filename = f"{date.strftime('%Y%m%d')}.py"
    filepath = os.path.join(os.path.dirname(__file__), filename)
    
    if is_special_day(date.day, date.month, date.year):
        # LeetCode-style problem
        problem = leetcode_problems[challenge_num % len(leetcode_problems)]
        content = f"# {problem['title']}\n"
        content += f"# Date: {date.strftime('%Y-%m-%d')}\n\n"
        content += f"{problem['code']}\n\n"
        content += "###########################################\n"
        content += "# Solution:\n"
        content += f"{problem['solution']}\n\n"
        content += "###########################################\n"
        content += "# Explanation:\n"
        content += f"# {problem['explanation']}\n"
    elif is_class_day(date.day):
        # Class-related challenge
        challenge = class_challenges[challenge_num % len(class_challenges)]
        content = f"# Date: {date.strftime('%Y-%m-%d')}\n\n"
        content += f"{challenge['code']}\n\n"
        content += "\n"
        for opt in challenge['options']:
            # Replace literal \n with actual newlines in options
            opt_formatted = opt.replace('\\n', '\n')
            # If option contains newlines, format it properly
            if '\n' in opt_formatted:
                lines = opt_formatted.split('\n')
                content += f"# {lines[0]}\n"
                for line in lines[1:]:
                    if line.strip():  # Only add non-empty continuation lines
                        content += f"#    {line}\n"
            else:
                content += f"# {opt}\n"
        content += "\n"
        content += "###########################################\n"
        content += f"# Answer: {challenge['answer']}\n"
        if 'explanation' in challenge:
            content += f"# Explanation: {challenge['explanation']}\n"
    else:
        # Regular challenge with common error
        challenge = common_errors[challenge_num % len(common_errors)]
        content = f"# Date: {date.strftime('%Y-%m-%d')}\n\n"
        content += f"{challenge['code']}\n\n"
        content += "\n"
        for opt in challenge['options']:
            # Replace literal \n with actual newlines in options
            opt_formatted = opt.replace('\\n', '\n')
            # If option contains newlines, format it properly
            if '\n' in opt_formatted:
                lines = opt_formatted.split('\n')
                content += f"# {lines[0]}\n"
                for line in lines[1:]:
                    if line.strip():  # Only add non-empty continuation lines
                        content += f"#    {line}\n"
            else:
                content += f"# {opt}\n"
        content += "\n"
        content += "###########################################\n"
        content += f"# Answer: {challenge['answer']}\n"
        if 'explanation' in challenge:
            content += f"# Explanation: {challenge['explanation']}\n"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    start_date = datetime(2026, 1, 1)
    challenge_counter = 0
    
    for day in range(365):
        current_date = start_date + timedelta(days=day)
        generate_file(current_date, challenge_counter)
        challenge_counter += 1
    
    print(f"Generated 365 Python challenge files for 2026!")

if __name__ == "__main__":
    main()

