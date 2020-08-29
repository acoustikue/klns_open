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


from config_script import *
from config_url import *

# module call
import module.parse as ps
import module.logger as lg

# main
# DIV2
fetched_list_b04044 = ps.parse(PARAM_YEAR, PARAM_3Q, PARAM_EE, PARAM_LEC_DIV2)
fetched_list_b04045 = ps.parse(PARAM_YEAR, PARAM_3Q, PARAM_EE, PARAM_LEC_DIV1)

old_list_b04044 = lg.loadLogFile(lg.LOG_FILE_B04044)
old_list_b04045 = lg.loadLogFile(lg.LOG_FILE_B04045)

# Parameter: -
# Returns: list
# Author: acoustikue
def compare(fetched, old):

    # This function returns altered information.

    mod_info_list = []

    for old_subj in old:
        for fet_subj in fetched:

            if old_subj['code'] == fet_subj['code']:
                if old_subj['seat'] != fet_subj['seat']:
                    mod_info_list.append(copy.deepcopy(fet_subj))

    return mod_info_list












