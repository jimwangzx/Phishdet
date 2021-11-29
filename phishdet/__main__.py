import argparse
from phishdet.core.scanner import exe
from phishdet.core.colors import cyan, red, reset, bright

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='Specify the URL for scanning', required=True)
parser.add_argument('-ls', '--login-scan', help='Scan for login keyords', action='store_true')
args = parser.parse_args()
target = args.url
loginS = args.login_scan

print('''
 ____  _     _     _     ____       _   
|  _ \| |__ (_)___| |__ |  _ \  ___| |_ 
| |_) | '_ \| / __| '_ \| | | |/ _ \ __|
|  __/| | | | \__ \ | | | |_| |  __/ |_ 
|_|   |_| |_|_|___/_| |_|____/ \___|\__| @whoamisec''' + reset)
print(red + bright + '    :.:' + reset + 'A Phishing Detection Tool' + bright + red +':.:' + reset)

def main():
    exe(target, loginS)