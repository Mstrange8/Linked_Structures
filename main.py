""" Name: Matthew Strange
    Class: CS2420
    Date: 02/06/2021

    Description: Driver file for courselist.py and course.py
"""

from course import Course
from courselist import CourseList


def main():
    my_list = CourseList()
    with open('data.txt', "r") as f:
        courses = f.readlines()

    for course in courses:
        course = course.strip().split(',')
        my_list.insert(Course(course[0], course[1], course[2], course[3]))

    print(my_list)
    print("Current List: ({})".format(my_list.find_size()))
    print(my_list.__str__())
    print("Cumulative GPA: {:.3f}".format(my_list.calculate_gpa()))

    my_list.is_sorted()
    my_list.remove_all(1030)
    print(my_list.__str__())


if __name__ == "__main__":
    main()
