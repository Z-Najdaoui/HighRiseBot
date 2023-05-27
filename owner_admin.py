from game import getSettings
from gameloop import getNextSettings
import json

#set data setting in setting.json
async def rWriteSettings(newSettings):
    with open("./settings.json","w") as f:
        json.dump(newSettings,f)

#set data in nextSetting.josn
async def rWriteNextSettings(newSettings):
    with open("./data/nextSettings.json","w") as f:
        json.dump(newSettings,f)

# add admin to setting.json and nextSetting.json
async def addAdmin(username,id):
    sett = getSettings()
    nextSett = await getNextSettings()
    sett['admins'][username] = id
    nextSett['admins'][username] = id
    await rWriteSettings(sett)
    await rWriteNextSettings(nextSett)

# remove admin from setting.json and nextSetting.json
async def removeAdmin(username):
    sett = getSettings()
    nextSett = await getNextSettings()
    del sett['admins'][username]
    del nextSett['admins'][username]
    await rWriteSettings(sett)
    await rWriteNextSettings(nextSett)



# return true if id of user in admin list in settings.json
async def isAdmin(user):
    sett = getSettings()
    try:return sett['admins'][user.username] == user.id
    except:return False

# return true if id of user is id owner in settings.json
async def isOwner(user):
    sett = getSettings()
    try:return sett['owner'][user.username] == user.id
    except:return False


