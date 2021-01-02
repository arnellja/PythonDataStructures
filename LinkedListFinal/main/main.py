from test_linked_lists import unittest # used for implementing the unit test.
import gettext # used to access text from file.
from courselist import CourseList # import CourseList Class
from course import Course # import Course class.
def main ():

    filePath = "data.txt" # path of file to access.
    file = open(filePath) # opens file.
    lines = len(file.readlines()) # accesses number of lines in data file.
    file = open(filePath) # reopens data file.
    number = 0 # temporary variable for class number.
    name = " " # temporary variable for class name.
    credit = 0 # temporary variable for credit hours.
    grade = 0.0 # temporary variable for grades.
    schedule = CourseList(None) # empty CourseList object.

    for x in range(lines - 1): # for loop parsing each line of data file.
        firstLine = file.readline()
        comma = firstLine.index(',')
        number = firstLine[0:comma] # accesses class number.
        firstLine = firstLine[comma + 1:len(firstLine)]
        comma = firstLine.index(',')
        name = firstLine[0:comma] # accesses class name.
        firstLine = firstLine[comma + 1:len(firstLine)]
        comma = firstLine.index(',')
        credit = firstLine[0:comma] # accesses credit hours.
        firstLine = firstLine[comma + 1:len(firstLine)]
        grade = firstLine # accesses grade.
        

        schedule.insert(Course(int(number), name, float(credit), float(grade), None)) # inserts a Course object into the CourseList object using parsed data.

    firstLine = file.readline() # repeats parsing process for last line of the data file.
    comma = firstLine.index(',')
    number = firstLine[0:comma]
    firstLine = firstLine[comma + 1:len(firstLine)]
    comma = firstLine.index(',')
    name = firstLine[0:comma]
    firstLine = firstLine[comma + 1:len(firstLine)]
    comma = firstLine.index(',')
    credit = firstLine[0:comma]
    firstLine = firstLine[comma + 1:len(firstLine)]
    grade = firstLine

    schedule.insert(Course(int(number), name, int(credit), float(grade), None)) # inserts last Course object.
    print("Current List: (", schedule.size(), ")") # prints out current CourseList object size.
    print("\n")


    print(schedule) # prints current CourseList with inserted courses.


    print("\n\n\n")
    print("Cumulative GPA: ", schedule.calculate_gpa()) # prints out cumulative GPA.

