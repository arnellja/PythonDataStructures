class Course(object):
    """constructs an individual course"""

    def __init__(self, number = 0, name = "Empty", credit_hour = 0.00, grade = 0.00, next = None): # initializer for the Course Class.
        self.number = number # default value for class number is 0.
        self.name = name # default value for class name is "Empty".
        self.credit_hour = credit_hour # default value for credit hours is 0.00.
        self.grade = grade # default value for grade is 0.00.
        self.next = next # default value for next is None.


    def number(self): # accessor method for number.
        return self.number

    def name(self): # accessor method for name.
        return self.name

    def credit_hour(self): # accessor method for credit hours.
        return self.credit_hour

    def grade(self): # accessor method for grade.
        return self.grade

    def next(self): # accessor method for next.
        return self.next

    def __str__(self): # to String method for Course Class.
        return ('cs{}, {}, {}, {}'.format(self.number,self.name,self.credit_hour, self.grade))
