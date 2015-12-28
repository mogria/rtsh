##################################################
#
# needs 2 arguments.
# both beeing one players home directory.
#
##################################################


import sys
import os

# ************** functions

def createPlayerHomeDir(playerDir):
	if not os.path.exists(playerDir):
		os.mkdir(playerDir)

def createPipe(playerDir):
	queuePath = os.path.join(playerDir, "command-queue")
	if not os.path.exists(queuePath):
		os.mkfifo(queuePath)


# ************** start

print("hello world, no just jocking getting to work now...")

playerDir1 = sys.argv[1]
playerDir2 = sys.argv[2]

createPlayerHomeDir(playerDir1)
createPipe(playerDir1)

createPlayerHomeDir(playerDir2)
createPipe(playerDir2)

print("started")	







