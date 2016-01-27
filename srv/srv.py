##################################################
#
# needs at least one arguments. (player name)
#
##################################################


import sys
import os
import pwd
import grp
import subprocess
import stat
import shutil

from printWithFlush import p
from util import getQueuePathFromPlayerName
from tickSystem import TickSystem
from model.resources import Resources
from model.storage import Storage
from model.world import World
from model.slaveunit import SlaveUnit

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

def initializePlayerGameObjects(world, num, playerName):
    start_position = world.start_coordinates[num]
    resources = Resources(owner=playerName, gold=200, position=start_position)
    Storage(resources).write(make_dirty=True)
    slave = SlaveUnit(position=start_position, owner=playerName)
    Storage(slave).write(make_dirty=True)

def changeToLowerPriviledgedUser():
    p("trying to change user to ", USER_RTSHSRV)
    p(subprocess.check_output("whoami"))
    gid = grp.getgrnam(GROUP_RTSHPLAYERS).gr_gid
    os.setgid(gid)
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

    world = Storage.from_file(World.STORAGE_LOCATION).read()
    for i in range(0, numberOfPlayers - 1):
        initializePlayerGameObjects(world, i, sys.argv[i + 1])
    p("done with preparation")


def main():
    p("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    p("server: hello world, no just joking going to work now...")
    prepare()
    p("starting tick system now")
    players = sys.argv[1:]
    ts = TickSystem(players)
    ts.start()


# ************** start

main()
