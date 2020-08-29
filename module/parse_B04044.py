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


from config_script import *
from config_url import *

# First requst
request_obj = requests.get(\
    paramedBaseUrl(PARAM_YEAR, PARAM_3Q, PARAM_EE, PARAM_LEC_DIV2))

if request_obj.status_code == 200: print('\tResponse: [200]')
else: print('\tResponse problem occurred.')

#
# Parsing process
soup = BeautifulSoup(request_obj.text, 'html.parser')
soup = BeautifulSoup(str(soup.find_all('tr', class_='table_bg_white')), 'html.parser') # And set again, 

# The first row contains description, 
# so remove the front line.
_set = soup.find_all('td')
del _set[0]

# container
parsed_list = []

cnt = 0
container = {} 

for __set in _set:
        
    # The site has 18 columns       
    cnt = cnt + 1

    if cnt == 4: container['code'] = str(__set.text.lstrip()).rstrip()
    if cnt == 5: container['name'] = str(__set.text.lstrip()).rstrip()
    if cnt == 10: container['prof'] = str(__set.text.lstrip()).rstrip()
    if cnt == 18:
        container['seat'] = parseSeatInfo(PARAM_YEAR, PARAM_3Q, container['code'])
        parsed_list.append(copy.deepcopy(container))

        # reset
        cnt = 0
        container = {}

# Debug
for i in parsed_list:
    print(i)


