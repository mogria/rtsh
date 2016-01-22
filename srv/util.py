import os

def getQueuePathFromPlayerName(playerName):
    playerDir = os.path.join("/home", playerName)
    queuePath = os.path.join(playerDir, "command-queue")
    return queuePath