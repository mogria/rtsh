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

sys.path.insert(0, '/gamesrv/commands')
import commandFactory
from invalidGameCommandError import InvalidGameCommandError 


TICK_INTERVAL_SEC = 1
USER_RTSHSRV = "rtshsrv"
GROUP_RTSHPLAYERS = "rtshplayers"


# ************** functions

def p(*args):
	text = ""
	for i in args:
		text += str(i)
	print(text)
	sys.stdout.flush()

def removeNewLineCharacters(s):
	if s.endswith("\n"):
		s = s[:-1]
	return s

def getQueuePathFromPlayerName(playerName):
	playerDir = os.path.join("/home", playerName)
	queuePath = os.path.join(playerDir, "command-queue")
	return queuePath



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



def callCommand(commandWithArgs):
	splitter = commandWithArgs.split(" ")
	cmdName = splitter[0]
	cmdArgs = splitter[1:]
	try:
		cmdClass = commandFactory.createCommandClass(cmdName, cmdArgs)
		cmdClass.execute()
	except InvalidGameCommandError as e:
		pathToCommands = "/gamesrv/commands"
		fullPath = os.path.join(pathToCommands, commandWithArgs)
		p(os.system(fullPath))


def processCommandsFor(playerName):
	p("player: ", playerName)
	queuePath = getQueuePathFromPlayerName(playerName)
	with open(queuePath, "r") as commandQueue:
		commandsWithArgs = commandQueue.readlines()
		for command in commandsWithArgs:
			command = removeNewLineCharacters(command)
			p(command)
			callCommand(command)
	with open(queuePath, "w") as commandQueue:
		commandQueue.truncate(0)


def processAllUsersCommands():
	numberOfPlayers = len(sys.argv)
	for i in range(1, numberOfPlayers):
		playerName = sys.argv[i]
		processCommandsFor(playerName)

		
def startTickSystem():
	tick = 0
	while(True):
		time.sleep(TICK_INTERVAL_SEC)
		p("tick ", tick)
		tick += 1
		processAllUsersCommands()	
	


def main():
	p("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
	p("server: hello world, no just joking going to work now...")
	prepare()
	p("starting tick system now")
	startTickSystem()
		


# ************** start

main()


