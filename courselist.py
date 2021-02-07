""" Name: Matthew Strange
    Class: CS2420
    Date: 02/06/2021

    Description: Contains Class for implementing linked list.
"""


class Node:
    """Node class for creating node object"""
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CourseList:
    """Implement linked list for course objects"""

    def __init__(self, h=None):
        self.head = h
        self._size = 0

    def insert(self, course):
        """inserts new course object into linked list"""
        new_node = Node(course)

        if self.head is None or self.head.data.number() >= new_node.data.number():
            new_node.next = self.head
            self.head = new_node
            self._size += 1
            return

        cur_node = self.head
        while cur_node.next and cur_node.next.data.number() < new_node.data.number():
            cur_node = cur_node.next
        new_node.next = cur_node.next
        cur_node.next = new_node
        self._size += 1

    def remove(self, number):
        """removes first occurrence of object in linked list"""
        prev_node = None
        cur_node = self.head
        while cur_node is not None:
            if cur_node.data.number() == number:
                if prev_node is not None:
                    prev_node.next = cur_node.next
                else:
                    self.head = cur_node.next
                self._size -= 1
                return True
            prev_node = cur_node
            cur_node = cur_node.next
        return False

    def remove_all(self, number):
        """removes all occurrences of object in linked list"""
        if self.head.data.number() == number:
            self.head = self.head.next
            self._size -= 1

        if self.head is not None:
            cur_node = self.head
            while cur_node.next is not None:
                if cur_node.next.data.number() == number:
                    cur_node.next = cur_node.next.next
                    self._size -= 1
                else:
                    cur_node = cur_node.next

    def find(self, number):
        """finds the first occurrence of the specified course in the list or returns -1"""
        cur_node = self.head
        while cur_node is not None:
            if number == cur_node.data.number():
                return cur_node.data
            cur_node = cur_node.next
        return -1

    def size(self):
        """returns the number of items in the list"""
        return self._size

    def calculate_gpa(self):
        """returns the GPA using all courses in the list"""
        cur_node = self.head
        gpa = 0
        total_credits = 0
        while cur_node is not None:
            gpa += cur_node.data.grade() * cur_node.data.credit_hr()
            total_credits += cur_node.data.credit_hr()
            cur_node = cur_node.next
        if total_credits == 0:
            return 0
        return gpa / total_credits

    def is_sorted(self):
        """returns True if the list is sorted by Course Number, False otherwise"""
        cur_list = []
        cur_node = self.head
        while cur_node is not None:
            cur_list.append(cur_node.data.number())
            cur_node = cur_node.next
        if cur_list == sorted(cur_list):
            return True
        return False

    def __str__(self):
        """returns a string with each course's data on a separate line"""
        string = ""
        cur_node = self.head
        while cur_node is not None:
            string += cur_node.data.__str__()
            cur_node = cur_node.next
        return string

    def __iter__(self):
        """iterates linked list"""
        self.iter_node = self.head
        self.iter = 0
        return self

    def __next__(self):
        """iterates linked list"""
        if self.iter_node is not None:
            result = self.iter
            self.iter += 1
            self.iter_node = self.iter_node.next
            return result
        raise StopIteration
