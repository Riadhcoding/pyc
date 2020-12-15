import compileall
import os,sys,time
from datetime import datetime
a = datetime.now().strftime('%Y-%m-%d %H:%M')
os.system('git pull')
logo = """
\033[1;34m                       dP   dP                         
\033[1;34m                       88   88                         
\033[1;37m   88d888b. dP    dP d8888P 88d888b. .d8888b. 88d888b. 
\033[1;37m   88'  `88 88    88   88   88'  `88 88'  `88 88'  `88 
\033[1;33m   88.  .88 88.  .88   88   88    88 88.  .88 88    88 
\033[1;33m   88Y888P' `8888P88   dP   dP    dP `88888P' dP    dP 
\033[1;34m   88            .88                                   
\033[1;34m   dP        d8888P           

\033[1;34m   dP    8888b          
\033[1;37m   88 o  88             
\033[1;33m   88 dP 88aaa  .d8888b. 
\033[1;33m   88 88 88     88ooood8 
\033[1;37m   88 88 88     88 \033[1;31m    Created by Riad
\033[1;34m   dP dP dP     `88888P
"""
os.system('clear')
print(logo)
print('\033[1;36m+++++++++++++++++++++++++++++++++++++++++++++++++++++++'),time.sleep(0.3)
print('\033[1;31m[1] \033[1;36mEncrypt | py to pyc'),time.sleep(0.3)
print('\033[1;31m[2] \033[1;35mDecode  | pyc to py'),time.sleep(0.3)
print('\033[1;36m+++++++++++++++++++++++++++++++++++++++'+a),time.sleep(0.3)
choose =input('\n\033[1;31m[?]Choose : \033[1;37m')
if choose =='1':
    file_py = input(" \033[1;32mFile >\033[1;37m")
    compileall.compile_file(file_py)
    print('\033[1;31msuccess encrypt')
    print("\033[1;36mSave to /sdcard/__pycache__")
elif choose =='2':
    file_pyc = input('\033[1;32mFile >\033[1;37m')
    com = f'uncompyle6 {file_pyc} > {file_pyc}_dec.py'
    os.system(com)
    print('\033[1;31mdecoding success')
else:
    print('\033[1;31mplease choose 1 or 2 !')


