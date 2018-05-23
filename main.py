from twilioFile import TwilioUser
from facebookFile import FbClient
import tempFunctions as tf
import requests

#  blocked for privacy lol
#  preset values/constants
ACCOUNT_SID = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
AUTH_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
MY_NUMBER = "xxxxxxxxxxx"
TWILIO_NUMBER= "xxxxxxxxxxx"
FB_GROUP_ID = "xxxxxxxxxxxxxx"
WEATHER_PROMPT = "Binghamton is "


def main():

  userTwilio = TwilioUser(ACCOUNT_SID, AUTH_TOKEN)
  
  userFacebook = FbClient('binghamton.breakdance@gmail.com', 'x')
  
  practiceAlert = ""

  r = requests.get(\
    "http://api.openweathermap.org/data/2.5/weather?zip=13902,us&appid=3d298f06e5b1a45ff332fdf6545cc8a4")

  #  parses json to find temp
  jsonData = r.json()
  tempKelvin = jsonData['main']['temp']
  weatherNum = tf.convertKtoF(float(tempKelvin))

  #  based on weather, will send one of two messages (valid or invalid)
  if tf.isNiceWeather(weatherNum):
    practiceAlert += "Time to session outside!"

    userFacebook.sendFbMessage("Yo outside session today!", FB_GROUP_ID)

  else:
    practiceAlert += "It's too cold to practice outside..."

    userFacebook.sendFbMessage("Session in Fine Arts...lesgoo", FB_GROUP_ID)

  
  userTwilio.sendText(WEATHER_PROMPT + bingWeather\
           ".\n\n" + practiceAlert, MY_NUMBER, TWILIO_NUMBER)

  userFacebook.logout()

  
main()

