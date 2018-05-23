from twilio.rest import Client as twilioClient


#  following object abstracts away all imports/methods
#  in order to only have to import the object
class TwilioUser():

  #  connects client to Twilio using info from account
  def __init__(self, accountID, keyID):
    self.twilioCli = twilioClient(accountID, keyID)

  #  sends text to user's number
  def sendText(self, text, userNum, twilioNum):
    self.twilioCli.messages.create(body=text, from_=twilioNum, to=userNum)
