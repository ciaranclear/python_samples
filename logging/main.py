import logging
from employee import Employee

# DEBUG:    Detailed information only when debugging
# INFO:     Confirmation that things are working as they should
# WARNING:  Indication that something unexpected happened but software is still working as expected
# CRITICAL: Serious error indicating that program may not be able to continue working

# Default logging level is warning

# Logging prints to console if no logfile is set
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('main.log') # file handler outputs to log file
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

stream_handler = logging.StreamHandler() # stream handler outputs to the console only
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        # logger.error("error message")
        logger.exception(f"Tried to divide {x} by zero")
        # logger.exception includes traceback
    else:
        return result


num_1 = 5
num_2 = 0

add_result = add(num_1, num_2)
print(f"num1:{num_1} added to num2:{num_2} result{add_result}")
logger.debug(f"num1:{num_1} added to num2:{num_2} result{add_result}")

sub_result = sub(num_1, num_2)
print(f"num1:{num_1} subtracted from num2:{num_2} result{sub_result}")
logger.debug(f"num1:{num_1} subtracted from num2:{num_2} result{sub_result}")

mul_result = mul(num_1, num_2)
print(f"num1:{num_1} multiplied by num2:{num_2} result{mul_result}")
logger.debug(f"num1:{num_1} multiplied by num2:{num_2} result{mul_result}")

div_result = div(num_1, num_2)
print(f"num1:{num_1} divided by num2:{num_2} result{div_result}")
logger.debug(f"num1:{num_1} divided by num2:{num_2} result{div_result}")


emp1 = Employee("Mark","Reily")
emp2 = Employee("Dave","Clinton")
