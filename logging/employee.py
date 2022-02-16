import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('Employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info(f'Created Employee: {self.fullname} {self.email}')

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'


emp1 = Employee("Mick", "Brown")
emp2 = Employee("Dave", "Burke")
emp3 = Employee("Paul", "Travis")