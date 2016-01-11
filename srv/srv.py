##################################################
#
# needs at least one arguments. (player name)
#
##################################################


import sys
import os
import pwd
import subprocess

# ************** functions

def p(*args):
	text = ""
	for i in args:
		text += str(i)

	print(text)
	sys.stdout.flush()


def changeOwner(path, userName):
	uid = pwd.getpwnam(userName).pw_uid
	gid = pwd.getpwnam(userName).pw_gid
	os.chown(path, uid, gid)


def createPlayer(playerName):
	p("trying to create player: ", playerName) 
	result = subprocess.call(["/home/create-player.sh", playerName])
	p(result)
	wasSuccessfull = result == 0
	p(wasSuccessfull)
	if wasSuccessfull:
		p("created player: ", playerName)
	else:
		p("player already available: ", playerName)


def getQueuePathFromPlayerName(playerName):
	playerDir = os.path.join("/home", playerName)
	queuePath = os.path.join(playerDir, "command-queue")
	return queuePath


def createPipe(playerName):
	queuePath = getQueuePathFromPlayerName(playerName)
	p("trying to create queue: ", queuePath)
	if not os.path.exists(queuePath):
		os.mkfifo(queuePath)
		changeOwner(queuePath, playerName)
		p("created queue: ", queuePath)
	else:
		p("queue already available: ", queuePath)


def changeToLowerPriviledgedUser():
	p("trying to change user to rtshsrv")
	p(subprocess.check_output("whoami"))
	uid = pwd.getpwnam("rtshsrv").pw_uid
	os.setuid(uid)
	p(subprocess.check_output("whoami"))
	p("changed user to rtshsrv")


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
	pathToCommands = "/gamesrv/commands"
	fullPath = os.path.join(pathToCommands, commandWithArgs)
	p(os.system(fullPath))


def main():
	p("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
	p("server: hello world, no just joking going to work now...")

	prepare()


	p("starting tick system now")
	
	c = 0
	while(True):
		p("iteration ", c)
		c+=1		
		numberOfPlayers = len(sys.argv)
		for i in range(1, numberOfPlayers):
			playerName = sys.argv[i]
			p("player: ", playerName)
			queuePath = getQueuePathFromPlayerName(playerName)
			with open(queuePath) as commandQueue:
				commandWithArgs = commandQueue.readline()
				callCommand(commandWithArgs)
		


# ************** start

main()


