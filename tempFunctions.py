
GOOD_WEATHER = 65

#  predicate func to determine eligible weather
def isNiceWeather(num):
  return num >= GOOD_WEATHER


#  func to convert Kelvin to Fahrenheit
def convertKtoF(tempK):
  return ((tempK - 273) * 1.8) + 32
