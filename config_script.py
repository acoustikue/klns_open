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
import platform
import copy

from config_url import showConfigUrl

# for import from parent directory
sys.path.append( 
    os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))) )


# Here the module's base directory will be set to folder where it is located.
# Every config files and other saved files must be in folder below the base directory.

PROJECT_CODE = 'klns'
PROJECT_OS = 'Windows'
PROJECT_SYS = ''
PROJECT_VERSION = '0.1.0va'

CURRENT_CODE = 'klns_w'
CURRENT_OS = str(platform.system())
CURRENT_SYS = CURRENT_OS + ' ' + str(platform.release()) + ' ' + str(platform.version())


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FCM_DIR = ''
MESSAGE_DIR = ''
LOG_DIR = ''


if CURRENT_OS == 'Windows':
    LOG_DIR = BASE_DIR + '\\log\\'
    FCM_DIR = BASE_DIR + '\\fcm\\'
    MESSAGE_DIR = BASE_DIR + '\\fcm\\message\\'
elif CURRENT_OS == 'Linux': 
    LOG_DIR = BASE_DIR + '/log/'
    FCM_DIR = BASE_DIR + '/fcm/'
    MESSAGE_DIR = BASE_DIR + '/fcm/message/'


# First!!
# Make directory if there is no db folder
if not(os.path.isdir(LOG_DIR)): os.makedirs(os.path.join(LOG_DIR))
if not(os.path.isdir(FCM_DIR)): os.makedirs(os.path.join(FCM_DIR))
if not(os.path.isdir(MESSAGE_DIR)): os.makedirs(os.path.join(MESSAGE_DIR))


PROJECT_BANNER = '[ku_ces_noty_service] ' + PROJECT_CODE + ', ' + PROJECT_VERSION
PROJECT_BANNER += (', ' + CURRENT_SYS + '\n\tCopyright (C) 2019 SukJoon Oh')



# Scripts
# platform

# Make sure to print just necessary information, for simple logs.
# print(PROJECT_BANNER)


# 
# Parameter: -
# Returns: -
# Author: acoustikue
def showConfigScript():

    #if KENS_ENABLE is True:
    #    print('\tKENS_ENABLE(1). KENS module will be loaded.')

    print('Script config:')

    print('\tPROJECT_CODE    \t' + PROJECT_CODE)
    print('\tPROJECT_OS      \t' + PROJECT_OS)
    print('\tPROJECT_SYS     \t' + PROJECT_SYS)
    print('\tPROJECT_VERSION \t' + PROJECT_VERSION)

    print('\tCURRENT_CODE    \t' + CURRENT_CODE)
    print('\tCURRENT_OS      \t' + CURRENT_OS)
    print('\tCURRENT_SYS     \t' + CURRENT_SYS)

    print('\tBASE_DIR        \t' + BASE_DIR)
    print('\tDB_DIR          \t' + DB_DIR)





# Executing this script?
if __name__ == '__main__':

    # First print banner
    print(PROJECT_BANNER)
    print('\tExecuting KnsfConfig script. Running in debug mode.\n')

    # Show configuration variables
    showConfigScript()
    
    print('')
    showConfigUrl()



