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

from config_script import *
from config_url import *

from module.logger import *
from module.parse import *


# Main
# First compare the two.

print(PROJECT_BANNER)

fetched_list_b04044 = parse(PARAM_YEAR, PARAM_3Q, PARAM_EE, PARAM_LEC_DIV2)
fetched_list_b04045 = parse(PARAM_YEAR, PARAM_3Q, PARAM_EE, PARAM_LEC_DIV1)

saveLogFile(LOG_FILE_B04044, fetched_list_b04044)
saveLogFile(LOG_FILE_B04045, fetched_list_b04045)

# Notify





