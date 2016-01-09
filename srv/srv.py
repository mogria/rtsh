##################################################
#
# needs 2 arguments.
# both beeing one players home directory.
#
##################################################


import sys
import os
import pwd
import subprocess

# ************** functions

def createPlayer(playerName):
	print("trying to create player: ", playerName) 
	result = subprocess.call(["/home/create-player.sh", playerName])
	print(result)
	wasSuccessfull = result == 0
	print(wasSuccessfull)
	if wasSuccessfull:
		print("created player: ", playerName)
	else:
		print("player already available: ", playerName)


def createPipe(playerName):

	playerDir = os.path.join("/home", playerName)
	print("player dir: ", playerDir)

	queuePath = os.path.join(playerDir, "command-queue")
	print("trying to create queue: ", queuePath)
	if not os.path.exists(queuePath):
		

		uid = pwd.getpwnam(playerName).pw_uid
		gid = pwd.getpwnam(playerName).pw_gid
		os.mkfifo(queuePath)
		os.chown(queuePath, uid, gid)


		print("created queue: ", queuePath)
	else:
		print("queue already available: ", queuePath)


def changeToLowerPriviledgedUser():
	print("trying to change user to rtshsrv")
	print(subprocess.check_output("whoami"))
	uid = pwd.getpwnam("rtshsrv").pw_uid
	os.setuid(uid)
	print(subprocess.check_output("whoami"))
	print("changed user to rtshsrv")


def main():
	print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
	print("server: hello world, no just joking going to work now...")

	numberOfPlayers = len(sys.argv)
	for i in range(1, numberOfPlayers):

		playerName = sys.argv[i]
		print("player name: ", playerName)
	
		createPlayer(playerName)
	
		createPipe(playerName)

	changeToLowerPriviledgedUser()

	print("started")	



# ************** start

main()


