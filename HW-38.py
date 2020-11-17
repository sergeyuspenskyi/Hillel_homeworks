class Group:

    def __init__(self, group_name, quantity):
        self.group_name = group_name
        self.quantity = quantity

    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        if len(group_name) > 6:
            raise NameError('Please put a name no longer than 6 symbols')
        self._group_name = group_name

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity <= 0:
            raise ValueError('Your group should have at least 1 student')
        self._quantity = quantity

    @classmethod
    def group_generator(cls, name, quantity):
        return cls(name, quantity)

    def __str__(self):
        """Returns information about group"""
        return f'Group {self._group_name}.\nNumber of students: {self._quantity}.'


class Student(Group):

    def __init__(self, name, age, mark, group_name, quantity):
        super().__init__(group_name, quantity)
        self.name = name
        self.age = age
        self.mark = mark

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) > 30:
            raise NameError('Please put a name no longer than 30 symbols')
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age <= 14:
            raise ValueError('Student should be at least 14 y.o')
        self._age = age

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        if mark <= -1 or mark >= 101:
            raise ValueError('Mark can`t be lower 0 or higher 100')
        self.__mark = mark

    @staticmethod
    def num_mark_to_letter_mark(mark):
        if mark >= 90:
            return 'A'
        elif 85 <= mark < 90:
            return 'B'
        elif 75 <= mark < 85:
            return 'C'
        elif 65 <= mark < 75:
            return 'D'
        elif 60 <= mark < 65:
            return 'E'
        else:
            return 'Fx'

    def __str__(self):
        """Returns information about student and his/her group"""
        return f'Student: {self._name}.\nAge: {self._age}.\nMark: {Student.num_mark_to_letter_mark(self.mark)}\n' \
               f'{super().__str__()}'


# Example of Student
john_wick = Student('John Wick', 20, 88, '101-A', 30)
print(john_wick)
