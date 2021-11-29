from colorama import Fore, Style, Back

red = Fore.RED
green = Fore.GREEN
cyan = Fore.CYAN
yellow = Fore.YELLOW
blue = Fore.BLUE
bright = Style.BRIGHT
reset = Style.RESET_ALL
good = (Style.BRIGHT + '[' + Fore.GREEN + 'SAFE' + Style.RESET_ALL + Style.BRIGHT + '] ' + Style.RESET_ALL)
bad = (Style.BRIGHT + '[' + Fore.RED + 'CRITICAL' + Style.RESET_ALL + Style.BRIGHT + '] ' + Style.RESET_ALL)
info = (Style.BRIGHT + '[' + Fore.YELLOW + 'INF' + Style.RESET_ALL + Style.BRIGHT + '] ' + Style.RESET_ALL)
warn = (Style.BRIGHT + '[' + Fore.CYAN + 'WARN' + Style.RESET_ALL + Style.BRIGHT + '] ' + Style.RESET_ALL)
err = (Style.BRIGHT + '[' + Fore.RED + 'ERR' + Style.RESET_ALL + Style.BRIGHT + '] ' + Style.RESET_ALL)
res = (Style.BRIGHT + '[' + Fore.GREEN + 'RES' + Style.RESET_ALL + Style.BRIGHT + '] ' + Style.RESET_ALL)