##################################################
#
# needs at least one arguments. (player name)
#
##################################################


import sys
import os
import pwd
import subprocess
import time
import stat
import shutil
import glob

from printWithFlush import p
from util import getQueuePathFromPlayerName
from model.storage import Storage
from commandQueueProcessor import CommandQueueProcessor

TICK_INTERVAL_SEC = 1
USER_RTSHSRV = "rtshsrv"
GROUP_RTSHPLAYERS = "rtshplayers"


# ************** functions

def createPlayer(playerName):
    p("trying to create player: ", playerName)
    wasSuccessfull = subprocess.call(["/home/create-player.sh", playerName]) == 0
    if wasSuccessfull:
        p("created player: ", playerName)
    else:
        p("player already available: ", playerName)


def createPipe(playerName):
    queuePath = getQueuePathFromPlayerName(playerName)
    pipe = open(queuePath, "w+")
    pipe.close()
    userRWGroupWOnly = stat.S_IREAD | stat.S_IWRITE | stat.S_IWGRP
    os.chmod(queuePath, userRWGroupWOnly)
    shutil.chown(queuePath, USER_RTSHSRV, GROUP_RTSHPLAYERS)
    p("created queue: ", queuePath)


def changeToLowerPriviledgedUser():
    p("trying to change user to ", USER_RTSHSRV)
    p(subprocess.check_output("whoami"))
    uid = pwd.getpwnam(USER_RTSHSRV).pw_uid
    os.setuid(uid)
    p(subprocess.check_output("whoami"))
    p("changed user")


def prepare():
    numberOfPlayers = len(sys.argv)
    for i in range(1, numberOfPlayers):
        playerName = sys.argv[i]
        p("player name: ", playerName)
        createPlayer(playerName)
        createPipe(playerName)

    changeToLowerPriviledgedUser()
    p("done with preparation")



def processAllUsersCommands():
    numberOfPlayers = len(sys.argv)
    for i in range(1, numberOfPlayers):
        playerName = sys.argv[i]
        cqp = CommandQueueProcessor(playerName)
        cqp.processCommands()



def getAllUnitFiles():
    units = []
    for unitFile in glob.glob("/world/**/unit*.json", recursive=True):
        s = Storage(unitFile)
        u = s.read()
        units.append(u)
    return units


def moveUnits():
    unitFiles = getAllUnitFiles()
    for f in unitFiles:
        with Storage(f) as u:
            u.move()


def startTickSystem():
    tick = 0
    while (True):
        time.sleep(TICK_INTERVAL_SEC)
        p("tick ", tick)
        tick += 1
        processAllUsersCommands()
        moveUnits()



def main():
    p("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    p("server: hello world, no just joking going to work now...")
    prepare()
    p("starting tick system now")
    startTickSystem()


# ************** start

main()
