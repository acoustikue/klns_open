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

import requests
from bs4 import BeautifulSoup # parser

# from config_script import PROJECT_BANNER

# for import from parent directory
sys.path.append( 
    os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))) )


# This file includes necessary option infos.

BASE_URL = "https://kupis.konkuk.ac.kr/sugang/acd/cour/time/SeoulTimetableInfo.jsp"
SEAT_URL = "https://kupis.konkuk.ac.kr/sugang/acd/cour/aply/CourInwonInqTime.jsp"
# ?ltYy=2019&ltShtm=B01012&sbjtId=3281

# Parameters
from datetime import datetime
PARAM_NAME_YEAR = 'ltYy='
PARAM_YEAR = str(datetime.now().year)

PARAM_NAME_MAJOR = 'openSust=' # EE 127110
PARAM_EE = '127110'

PARAM_NAME_SEMESTER = 'ltShtm='

# B01011 1학기
# B01012 2학기
# B01015 동계 계절학기
# B01014 하계 계절학기
PARAM_1Q = 'B01011'
PARAM_3Q = 'B01012'
PARAM_4Q = 'B01014'
PARAM_2Q = 'B01015'

PARAM_NAME_LEC_DIV = 'pobtDiv='

PARAM_LEC_DIV1 = 'B04045'
PARAM_LEC_DIV2 = 'B04044'
# 전선 B04045
# 전필 B04044

def paramedBaseUrl(year, semester, major, lec_div):

    return BASE_URL + '?' + PARAM_NAME_YEAR + year + '&'\
        + PARAM_NAME_MAJOR + major  + '&'\
        + PARAM_NAME_SEMESTER + semester + '&'\
        + PARAM_NAME_LEC_DIV + lec_div

# openSust=127110&ltYy=2019&ltShtm=B01012&pobtDiv=B04045')


def parseSeatInfo(year, semester, subject_id):

    request_obj = requests.get(\
        SEAT_URL + '?ltYy=' + year\
            + '&ltShtm=' + semester\
                + '&sbjtId=' + subject_id)

    soup = BeautifulSoup(request_obj.text, 'html.parser')

    seat_info = soup.find_all('td', class_='table_bg_white')

    ret = str(seat_info[1].text.lstrip()).rstrip() + '/' + str(seat_info[2].text.lstrip()).rstrip()

    return ret




# 
# Parameter: -
# Returns: -
# Author: acoustikue
def showConfigUrl():

    print('URL config:')

    print('\tBASE_URL          \t' + BASE_URL)
    print('\tPARAM_NAME_YEAR     \t' + PARAM_NAME_YEAR)
    print('\tPARAM_NAME_MAJOR    \t' + PARAM_NAME_MAJOR)
    print('\tPARAM_NAME_SEMESTER\t' + PARAM_NAME_SEMESTER)
    print('\tPARAM_NAME_LEC_DIV\t' + PARAM_NAME_LEC_DIV)


# Executing this script?
if __name__ == '__main__':

    # Show configuration variables
    print('\tNone.')
    #showConfigUrl()

