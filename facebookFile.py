from fbchat import Client
from fbchat.models import *


#  following object abstracts away all imports/methods
#  in order to only have to import the object
class FbClient():

  #  sets Client
  def __init__(self, email, key):
    self.clientWrapper = Client(email, key)

  
  #  code under will send message to group chat
  def sendFbMessage(self, message, groupID):
    self.clientWrapper.sendMessage(message, \
                       thread_id=groupID, \
                       thread_type=ThreadType.GROUP)


  def logout(self):
    self.clientWrapper.logout()
