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

from pyfcm import FCMNotification


# for import from parent directory
sys.path.append( 
    os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))) )


from config_script import *
from config_url import *

# Global
SERVER_KEY_FILE = FCM_DIR + 'server_key.klns'
DEVICE_TOKEN_FILE = FCM_DIR + 'device_token.klns'

SERVER_KEY = ''
DEVICE = []

# Parameter: -
# Returns: list
# Author: acoustikue
def _loadDeviceToken(token_file_addr):

    device_token_list = []

    if os.path.isfile(token_file_addr):
        with open(token_file_addr, "r", encoding="utf-8") as token_file: # Read file.

            _list = token_file.readlines() # Read api key

            for user in _list:
                device_token_list.append(str(user).rstrip('\n')) # Remove \n 
                print('\tFCM ' + str(user)[0:19] + '... sent.')

    return device_token_list


# Parameter: -
# Returns: list
# Author: acoustikue
def _loadServerKey(key_file_addr):
    
    # local
    server_key = ''

    if os.path.isfile(key_file_addr):
        with open(key_file_addr, "r", encoding="utf-8") as key_file: # Read file.
            
            server_key = key_file.readline().rstrip('\n')

    else: print('\tNo server key file exists.')

    return server_key


# Global ready
FCM_SERVICE = FCMNotification(api_key=_loadServerKey(SERVER_KEY_FILE))
DEVICE_LIST = _loadDeviceToken(DEVICE_TOKEN_FILE)


def notifyMultipleDevice(title, body, action):

    FCM_SERVICE.notify_multiple_devices(registration_ids=DEVICE_LIST,\
        message_title=title,\
            message_body=body, click_action=action)



# notifyMultipleDevice('샘플', '바디', '액션')















