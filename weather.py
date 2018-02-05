import requests
import json
import notify2
# Get info from Dark Sky, only daily forcasts by exclude minutely and hourly forecasts:
r = requests.get("https://api.darksky.net/forecast/2b41959f8298b697485d46bea2477504/41.443234,-81.774603?exclude=minutely,hourly")

# Get response and convert to json
def get_weather():
    if r.status_code != 200:
        print "Shit's broke!!"
    else:
        weather = r.json()
        return weather
print get_weather()

# Parse the JSON payload
def parse_weather():
    weather = get_weather()
    #return weather["hourly"]["data"][0]['precipType']
    global current_temp
    global summary
    global current_icon
    global future_summary
    global future_icon
    global alert
    current_temp = weather["currently"]["temperature"]
    summary = weather["currently"]["summary"]
    current_icon = weather["currently"]["icon"]
    future_summary = weather["daily"]["summary"]
    future_icon = weather["daily"]["icon"]
    alert = weather["alerts"][0]["description"]

#{u'currently': {u'ozone': 366.78, u'windGust': 5.39, u'temperature': 36.33, u'dewPoint': 34.33, u'nearestStormDistance': 23, u'humidity': 0.92, u'nearestStormBearing': 321, u'summary': u'Mostly Cloudy', u'apparentTemperature': 36.33, u'pressure': 1007.64, u'windSpeed': 2.97, u'precipProbability': 0, u'visibility': 4.69, u'cloudCover': 0.78, u'time': 1517774124, u'windBearing': 286, u'precipIntensity': 0, u'uvIndex': 1, u'icon': u'partly-cloudy-day'}, u'daily': {u'icon': u'snow', u'data': #[{u'apparentTemperatureMinTime': 1517803200, u'precipType': u'snow', u'temperatureLow': 15.42, u'precipIntensityMaxTime': 1517760000, u'temperatureMin': 20.7, u'temperatureHigh': 36.66, u'summary':


print parse_weather()


# Logic for notification icon based on icon from payload:

def get_icon(input):
    if input == "clear-day":
        return "/home/joe/weatherpy/icons/sun.png"
    elif input == "clear-night":
        return "/home/joe/weatherpy/icons/moon.png"
    elif input == "rain" or input == "sleet":
        return "/home/joe/weatherpy/icons/drizzle.png"
    elif input == "snow":
        return "/home/joe/weatherpy/weatherpy/icons/snow.png"
    elif input == "wind":
        return "/home/joe/weatherpy/weatherpy/icons/wind.png"
    elif input == "fog":
        return "/home/joe/weatherpy/weatherpy/icons/fog.png"
    elif input == "cloudy":
        return "/home/joe/weatherpy/weatherpy/icons/cloudy.png"
    elif input == "partly-cloudy-day":
        return "/home/joe/weatherpy/weatherpy/icons/partlycloudy_day.png"
    elif input == "partly-cloudy-night":
        return "/home/joe/weatherpy/weatherpy/icons/partlycloudy_night.png"
    else:
        return "/home/joe/weatherpy/weatherpy/icons/sun.png"

# Message for notification bubble
w_message = "It is currently %s degress" % current_temp + " with " + summary
current_image = get_icon(current_icon)
future_message = future_summary
future_icon = get_icon(future_icon)
alert_message = alert

# Check if there are alerts:
def check_alerts(alert):
    try:
        alert
    except NameError:
        return alert


# Create the notificaiton bubble:

def sendalert(title, message, image):
    notify2.init("Test")
    notice = notify2.Notification(title, message, image)
    notice.show()
    title = "ALERT!"
    return
sendalert("ALERT!", alert, future_icon)


def sendweather(title, message, image):
    notify2.init("Test")
    notice = notify2.Notification(title, message, image)
    notice.show()
    title = "Current Weather"
    #message = parse_weather()
    return
sendweather("Current Weather", w_message, current_image)

def sendtomweather(title, message, image):
    notify2.init("Test")
    notice = notify2.Notification(title, message, image)
    notice.show()
    title = "Tomorrow's weather"
    return
sendtomweather("This week: ", future_message, future_icon)

'''
DOESn't work :(
def sendalert(title, message, image):
    notify2.init("Test")
    notice = notify2.Notification(title, message, image).set_urgency(URGENCY_CRITICAL)
    notice.show()
    title = "ALERT!"
    return
sendalert("Current Alert!", alert, future_icon)
'''
