from recursioncounter import RecursionCounter
from course import Course

class CourseList(object):
    """constructs a list of courses"""

    def __init__(self, head = None): # initializes CourseList object with variable head representing the head of the linked list.
        self.head = head

    def insert_recursive_helper(self, course, prevCourse, comparingCourse): # insert recursive helper method takes course being inserted with courses above and below it.
        RecursionCounter()
        if (comparingCourse == None):
            prevCourse.next = course
            return True
        elif (course.number < comparingCourse.number):
            course.next = comparingCourse
            prevCourse.next = course
            return True
        else:
            return self.insert_recursive_helper(course, comparingCourse, comparingCourse.next)

    def insert(self, course): # insert function used to insert new Courses into the acsending order of the CourseList.
        if (self.head == None):
            self.head = course
            self.head.next = None
            return True
        elif (self.head.number > course.number):
            course.next = self.head
            self.head = course
            return True
        else:
            return self.insert_recursive_helper(course, self.head, self.head.next)

    def remove(self, number): # remove method used to remove the first instance of the Course with the given number parameter.
        if (self.head == None):
            return False
        elif (self.head.number == number):
            self.head = self.head.next
        else:
            return self.remove_recursive_helper(self.head, self.head.next, number)

    def remove_recursive_helper(self, course, nextCourse, number): # recursive helper for remove function used to traverse list and find first instance of desired element.
        RecursionCounter()
        if (nextCourse == None):
            return False
        elif (nextCourse.number == number):
            course.next = nextCourse.next
            nextCourse.next = None
            return True
        else:
            return self.remove_recursive_helper(nextCourse, nextCourse.next, number)

    def remove_all(self, number): # Remove all function used to remove all instances of an element with given number parameter.
        if (self.head.next == None):
            if (self.head.number == number):
               self.head = None
               return True
        self.remove_all_at_head(self.head, number)
        return self.remove_all_helper(self.head.next, self.head, number)
    
    def remove_all_at_head(self, course, number): # used if desired Course objects are at the head and beginning of ordered linked list.
        RecursionCounter()
        if (course.number == number):
            self.head = course.next
            return self.remove_all_at_head(self.head, number)
        return True

    def remove_all_helper(self, course, prevCourse, number): # used to traverse linked list and remove all instances of Courses with given class number.
        RecursionCounter()
        if (course == None):
            return True
        if (course.number == number):
            prevCourse.next = course.next
            course.next = None
            return self.remove_all_helper(prevCourse.next, prevCourse, number)
        else:
            return self.remove_all_helper(course.next, course, number)

    def size(self): # used to access the size of the current linked list Course List.
        if (self.head == None):
            return 0
        else:
            return 1 + self.size_helper(self.head.next)

    def size_helper(self, course): # recursively traverses linked list to access its size.
        RecursionCounter()
        if (course == None):
            return 0
        else:
            return 1 + self.size_helper(course.next)

    def is_sorted(self): # used to determine if the CourseList is ordered by the class numbers.
        if (self.head.next == None):
            return True
        else:
            return self.recursive_sorted_helper(self.head)

    def recursive_sorted_helper(self, course): # recursively traverses list to determine ordering.
        RecursionCounter()
        if (course.next == None):
            return True
        elif (course.number <= course.next.number):
            return self.recursive_sorted_helper(course.next)
        else:
            return False

    def find(self, number): # used to find index of first instance of the Course with given class number.
        counter = 0
        if (self.head.number == number):
            return 0
        elif (self.head.number != number and self.head.next == None):
            return -1
        else:
            return self.find_recursive_helper(self.head.next, number, counter)

    def find_recursive_helper(self, course, number, counter): # recursively traverses the list to find desired index.
        RecursionCounter()
        counter += 1
        if (course.number == number):
            return counter
        elif (course.next == None):
            return -1
        else:
            return self.find_recursive_helper(course.next, number, counter)

    def calculate_gpa(self): # function determined the cumulative GPA of a given CourseList.
        gpaRound = 3
        totalCreditHours = self.recursive_total_credit(self.head)
        totalAccumulatedGrade = self.recursive_total_gpa(self.head)
        return round((totalAccumulatedGrade / totalCreditHours), gpaRound)

    def recursive_total_credit(self, course): # recursively accesses total credit hours of a CourseList, to use in calculating GPA.
        RecursionCounter()
        if (course.next == None):
            return course.credit_hour
        else:
            return course.credit_hour + self.recursive_total_credit(course.next)

    def recursive_total_gpa (self, course): # recursively accesses total grade points, to calculate the cumulative GPA.
        RecursionCounter()
        if (course.next == None):
            return (course.credit_hour * course.grade)
        else:
            return ((course.credit_hour * course.grade) + self.recursive_total_gpa(course.next))

    def __str__(self): # a to string method for the CourseList class.
        if (self.head == None):
            return "Course List is empty"
        elif (self.head.next == None):
            return self.head
        else:
            return '{}'.format(self.toString_recursive(self.head, self.head.next))

    def toString_recursive(self, course, nextCourse): # used to traverse Courses in the CourseList to be printed in the toString, using recursion.
        RecursionCounter()
        if (nextCourse == None):
            return course
        else:
           return '{}\n{}'.format(course, self.toString_recursive(nextCourse, nextCourse.next))

    def __iter__(self): #iterator methods.
        return self
    def __next__(self):
        return next



