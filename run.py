import os, sys, platform
os.system('clear')
try:os.system('rm -rf KAIDO')
except:pass
try:os.system('rm -rf RAND')
except:pass
os.system("pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests")
try:os.system('git pull')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    print("\x1b[1;93mDOWNLOADING UPDATE...\x1b[1;92m\n")
    os.system('curl -L https://github.com/KAIDO-143/config/blob/main/KAIDO?raw=true -o KAIDO')
    #os.system('unzip NILLXD > /dev/null')
    #os.remove('NILLXD')
    os.system('chmod 777 KAIDO && ./KAIDO')
elif bit == '32bit':
    exit("\x1b[1;91mSORRY BRO 32 BIT NOT SUPPORTED\x1b[1;97m")
