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
        my_list.insert(Course(int(course[0]), course[1], float(course[2]), float(course[3])))

    print("Current List: ({})".format(my_list.size()))
    print(my_list.__str__())
    print("Cumulative GPA: {:.3f}".format(my_list.calculate_gpa()))


if __name__ == "__main__":
    main()
