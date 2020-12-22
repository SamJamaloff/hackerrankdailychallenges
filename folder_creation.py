r"""
    I am too lazy to create folder for each day. 
    That is why I am going to write a script in order to create folders for me.

    This is 30 days of HackkerRank coding challenge that is why I need to create only 30 folder
    Each day should folder should consists of README.md and main.py file in it

    In order to that we need to run terminal commands inside pythons script
    - mkdir folder_name --> is used for creating folder with given name
    - touch xxx.yy -- > is used for creating file with name xxx with yy type
    
    OH BTW we need "CD" command too for changing the folder location
"""

import os

# So now we need to run it in a loop with all names and custom file names
# This is not human readabl format but it works ;)
for i in range(30): # because we have only 30 days for challenge
    custom_day_name = "day_" + str(i + 1)
    custom_string_for_commands = "mkdir " + custom_day_name + " && cd "+custom_day_name + " && echo > main.py && echo > README.md && cd ../" 
    os.system(custom_string_for_commands)
    