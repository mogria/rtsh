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
	print("trying to create home dir: ", playerDir) 
	if not os.path.exists(playerDir):
		os.mkdir(playerDir)
		print("created home dir: ", playerDir)
	else:
		print("home dir already available: ", playerDir)

def createPipe(playerDir):
	queuePath = os.path.join(playerDir, "command-queue")
	print("trying to create queue: ", queuePath)
	if not os.path.exists(queuePath):
		os.mkfifo(queuePath)
		print("created queue: ", queuePath)
	else:
		print("queue already available: ", queuePath)




# ************** start

print("hello world, no just jocking going to work now...")


numberOfPlayers = len(sys.argv)
for i in range(1, numberOfPlayers):

	playerDir = sys.argv[i]
	print("player dir: ", playerDir)
	
	createPlayerHomeDir(playerDir)
	createPipe(playerDir)


print("started")	







