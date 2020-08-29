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


from module.compare import *
from module.logger import *

from module.fcm import *



# Main
# First compare the two.

print(PROJECT_BANNER)

fcm_message_list_b04044 = compare(fetched_list_b04044, old_list_b04044)
fcm_message_list_b04045 = compare(fetched_list_b04045, old_list_b04045)


if fcm_message_list_b04044:

    title = '전기전자공학부 [전선] 신청인원 변동'
    body = ''

    for _list in fcm_message_list_b04044:
        body += (_list['name'] + ': ' + _list['seat'] + '\n')

    notifyMultipleDevice(title, body, '')



if fcm_message_list_b04045:
    title = '전기전자공학부 [전필] 신청인원 변동'
    body = ''

    for _list in fcm_message_list_b04045:
        body += (_list['name'] + ': ' + _list['seat'] + '\n')

    notifyMultipleDevice(title, body, '')



# Notify





