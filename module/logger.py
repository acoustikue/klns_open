# [Project Ku CES Noty-Service] Konkuk Univ. Class Empty Seat Notification Service for EE.
# 0.1.0va, 19.12.27. First launched.
# written by acoustikue(SukJoon Oh)
#                                 __  _ __            
#    ____ __________  __  _______/ /_(_) /____  _____ 
#   / __ `/ ___/ __ \/ / / / ___/ __/ / //_/ / / / _ \
#  / /_/ / /__/ /_/ / /_/ (__  ) /_/ / ,< / /_/ /  __/
#  \__,_/\___/\____/\__,_/____/\__/_/_/|_|\__,_/\___/ 
#                                                     
# Visual Studio Code
# 

# This project requires pyfcm library, 
# thus first install it by
# $ pip3 install pyfcm

# In initial version, many of original KENS/KNS functions are refactored, 
# since KLNS can be distinguished by only methods of sending notifications to devices.

# This is a test code.

import os, sys
import copy

import ast

# for import from parent directory
sys.path.append( 
    os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))) )


from config_script import *
from config_url import *


# Global
LOG_FILE_B04044 = LOG_DIR + 'b04044.klns'
LOG_FILE_B04045 = LOG_DIR + 'b04045.klns'


# Parameter: -
# Returns: list
# Author: acoustikue
def loadLogFile(log_file_addr):
    
    # local
    lec_list = []

    if os.path.isfile(log_file_addr):
        with open(log_file_addr, "r", encoding="utf-8") as log_file: # Read file.

            while True:
                data = log_file.readline()
                if not data: break

                lec_list.append(ast.literal_eval(data))

    else: print('\tNo server key file exists.')

    return lec_list



# Parameter: -
# Returns: list
# Author: acoustikue
def saveLogFile(log_file_addr, parsed_list):

    if os.path.isfile(log_file_addr):
        with open(log_file_addr, "w", encoding="utf-8") as log_file: # Read file.
            
            for _list in parsed_list:
                log_file.write(str(_list) + '\n')

    else: print('\tNo ' + log_file_addr + ' file exists.')










