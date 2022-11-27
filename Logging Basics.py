## Logging is a means of tracking events that happen when some software runs ##
## Logging is important for software developing, debugging, and running ##
## Logging has 5 standard Logging levels: - ##
    #DEBUG: - Detailed Information, typically of interest only when diagonsing problems
    #INFO: - confirmation that things are working as expect
    #WARNING: - An indictaion that something unexpected happened, or indicative of some problem in the near future 
    #(example: -  disk space low). The software is still working as expected
    #ERROR: - Due to more serious problem, the software has not been able to perfrom some function
    #CRITICAL: - A serious error, indicating that the program itself may be unable to continue running
## The defult level for logging is set to warning, i.e. it will capture everything that is warning or above(error & critical)

import logging
import logging2
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('test.log')
logger.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# logging.basicConfig(filename='test.log', level=logging.DEBUG,
#  format='%(asctime)s:%(levelname)s:%(message)s') #to set the level we use basic config.
                                                              #to create a log file we use filename= a new file will be created and prin the output there
                                                           #if there is change it will print the previous output and the latest one too
                                                              #To change the logging format we use 'format' keyword                                                              #
def add(a, b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    # try: 
    #     result = a / b
    # except ZeroDivisionError:
    #     logger.exception('Sorry not divisible')
    # else:
    #     return result
    return a//b

num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1,num_2,add_result))

sub_result = subtract(num_1,num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1,num_2,sub_result))
                                        # The debug won't print anything as the default level is warning and above, but this can 
                                        # be printed if we set the logging to the specific level. 
mul_result = multiply(num_1,num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1,num_2,mul_result))

div_result = divide(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1,num_2,div_result))


# add_result = add(num_1, num_2)
# logging.warning('Add: {} + {} = {}'.format(num_1,num_2,add_result))

# sub_result = subtract(num_1,num_2)
# logging.warning('Sub: {} - {} = {}'.format(num_1,num_2,add_result))
                                            #This will print the desired output because the logging level is set to warning
# mul_result = multiply(num_1,num_2)
# logging.warning('Mul: {} * {} = {}'.format(num_1,num_2,add_result))

# div_result = divide(num_1, num_2)
# logging.warning('Div: {} / {} = {}'.format(num_1,num_2,add_result))



