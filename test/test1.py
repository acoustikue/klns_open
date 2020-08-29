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

# for import from parent directory
sys.path.append( 
    os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))) )

import requests
from bs4 import BeautifulSoup # parser






if __name__ == '__main__':

    from config_script import *
    from config_url import *


    request_obj = requests.get('https://kupis.konkuk.ac.kr/sugang/acd/cour/time/SeoulTimetableInfo.jsp?openSust=127110&ltYy=2019&ltShtm=B01012&pobtDiv=B04045')

    if request_obj.status_code == 200:
        print('\tResponse: [200]')

    else:
        print('\tResponse problem occurred.')

    soup = BeautifulSoup(request_obj.text, 'html.parser')
    soup = BeautifulSoup(str(soup.find_all('tr', class_='table_bg_white')), 'html.parser') # And set again, 

    #print(soup.find_all('td'))
    _set = soup.find_all('td')
    del _set[0]

    info_list = []

    cnt = 0
    form = {}

    for __set in _set:
        
        # 18 cols
        
        
        cnt = cnt + 1

        if cnt == 4:
            form['code'] = str(__set.text.lstrip()).rstrip()
        if cnt == 5: 
            form['name'] = str(__set.text.lstrip()).rstrip()
        if cnt == 10:
            form['prof'] = str(__set.text.lstrip()).rstrip()
        if cnt == 18:
            cnt = 0
            form['seat'] = parseSeatInfo('2019', 'B01012', form['code'])

            info_list.append(copy.deepcopy(form))
            form = {}

    for i in info_list:
        print(i)











