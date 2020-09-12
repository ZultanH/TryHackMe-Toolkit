"""
Import Modules
"""
import os
from os import system, popen
from sys import argv
from time import sleep
import random

"""
Colors List
"""
cyan 	= "\033[0;96m"
green 	= "\033[0;92m"
white 	= "\033[0;97m"
red 	= "\033[0;91m"
blue 	= "\033[0;94m"
yellow 	= "\033[0;33m"
magenta = "\033[0;35m"
colorTuple = (cyan, green, white, red, blue, yellow, magenta)
barLine = "------------------------------"

bannerLines = (
    '  _______         _    _            _    __  __        _______          _ _    _ _   ',
    ' |__   __|       | |  | |          | |  |  \/  |      |__   __|        | | |  (_) |  ',
    '    | |_ __ _   _| |__| | __ _  ___| | _| \  / | ___     | | ___   ___ | | | ___| |_ ',
    "    | | '__| | | |  __  |/ _` |/ __| |/ / |\/| |/ _ \    | |/ _ \ / _ \| | |/ / | __|",
    '    | | |  | |_| | |  | | (_| | (__|   <| |  | |  __/    | | (_) | (_) | |   <| | |_ ',
    '    | | |  | |_| | |  | | (_| | (__|   <| |  | |  __/    | | (_) | (_) | |   <| | |_ ',
    '    |_|_|   \__, |_|  |_|\__,_|\___|_|\_\_|  |_|\___|    |_|\___/ \___/|_|_|\_\_|\__|',
    '             __/ |                                                                   ',
    '            |___/                                                                    ',
    'Orpheus#5400'
)

def printBanner():
    for line in bannerLines:
        color = colorTuple[random.randint(0, len(colorTuple))]
        print("{} {}\n".format(color, line))

def get_processes():
    output = popen('ps aux').read()
    headers = [h for h in ' '.join(output[0].strip().split()).split() if h]
    raw_data = map(lambda s: s.strip().split(None, len(headers) - 1), output[1:])
    return [dict(zip(headers, r)) for r in raw_data]

def getProcessByName(procName):
    output = popen('ps aux | grep {}'.format(procName)).read()
    headers = [h for h in ' '.join(output[0].strip().split()).split() if h]
    raw_data = map(lambda s: s.strip().split(None, len(headers) - 1), output[1:])
    return [dict(zip(headers, r)) for r in raw_data]

def isProcessRunning(procId):
    cmd = "ps -p {} >/dev/null && echo 1 || echo 2".format(procId)
    return popen(cmd).read() == '1'

def killProcessById(procId):
    cmd = "pkill -9 {}".format(procId)
    output = popen(cmd).read()

def getRunLevel():
    output = popen("whoami").read()
    return output


def main():
    printBanner()

if __name__ == "__main__":
    main()
