"""
Import Modules
"""
import os
from os import system, popen
from sys import argv
import sys
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
    "  _____         _  _         _   __  __       _____         _ _   _ _",
    " |_   _| _ _  _| || |__ _ __| |_|  \/  |___  |_   _|__  ___| | |_(_) |_",
    "   | || '_| || | __ / _` / _| / / |\/| / -_)   | |/ _ \/ _ \ | / / |  _|",
    "   |_||_|  \_, |_||_\__,_\__|_\_\_|  |_\___|   |_|\___/\___/_|_\_\_|\__|",
    "           |__/                                                         ",
    'Orpheus#5400'
)
commandArray = []

class Command:
    def __init__(self, name, func, helpText = ""):
        self.name = name
        self.func = func
        commandArray.append(self)

    def run(self):
        self.func()

    def toJSON(self):
        return {
            'name': self.name, 
            'func': self.func,
        }
    
"""
Function Definitions
"""
def printBanner():
    for line in bannerLines:
        color = colorTuple[random.randint(0, len(colorTuple) - 1)]
        print("{} {}\n".format(color, line))

def warn(string):
    print(yellow + "[!] " + string) 

def error(string):
    print(red + "[!] " + string)

def info(string):
    print(blue + "[i] " + string)

def success(string):
    print(green + "[i] " + string)

def getProcesses():
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

def handleCommand(cmdName):
    for cmdClass in commandArray:
        cmdDict = cmdClass.toJSON()
        if cmdDict['name'] == cmdName:
            cmdDict['func']()
    main()

"""
Command Definitions
"""
def listProcsCmd():
    print("Processes: ")
    runningProcs = getProcesses()
    for _dict in runningProcs:
        print(_dict)


def createCommands():
    commands = [
        Command("list_processes", listProcsCmd)
    ]

def main():
    while True:
        try:
            cmdName = input("Enter Command: ")
            handleCommand(cmdName)
        except KeyboardInterrupt:
            info("Exiting...")
            sys.exit()
    
if __name__ == "__main__":
    printBanner()
    createCommands()
    main()
