import requests
import json
import notify2
import os
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
#    alert = weather["alerts"][0]["description"]

print parse_weather()

# realtive file path for each image:
#path = os.path.dirname(os.path.realpath(__file__) + '/'
#sun = file + "icons/sun.png"

# Logic for notification icon based on icon from payload:
def get_icon(input):
    if input == "clear-day":
        return "/home/joe/weatherpy/icons/sun.png"
    elif input == "clear-night":
        return "/home/joe/weatherpy/icons/moon.png"
    elif input == "rain" or input == "sleet":
        return "/home/joe/weatherpy/icons/drizzle.png"
    elif input == "snow":
        return "/home/joe/weatherpy/icons/snow.png"
    elif input == "wind":
        return "/home/joe/weatherpy/icons/wind.png"
    elif input == "fog":
        return "/home/joe/weatherpy/icons/fog.png"
    elif input == "cloudy":
        return "/home/joe/weatherpy/icons/cloudy.png"
    elif input == "partly-cloudy-day":
        return "/home/joe/weatherpy/icons/partlycloudy_day.png"
    elif input == "partly-cloudy-night":
        return "/home/joe/weatherpy/icons/partlycloudy_night.png"
    else:
        return "/home/joe/weatherpy/icons/sun.png"

# Message for notification bubble

current_message = "It is currently %s degress" % current_temp + " with " + summary
current_image = get_icon(current_icon)
future_message = future_summary
future_icon = get_icon(future_icon)
#alert_message = alert

# Current weather bubble:
def sendweather(title, message, image):
    notify2.init("Test")
    notice = notify2.Notification(title, message, image)
    notice.show()
    title = "Current Weather"
    #message = parse_weather()
    return
sendweather("Current Weather", current_message, current_image)

# Future weather bubble:
def sendtomweather(title, message, image):
    notify2.init("Test")
    notice = notify2.Notification(title, message, image)
    notice.show()
    title = "Tomorrow's weather"
    return
sendtomweather("This week: ", future_message, future_icon)


# Below is weather alert functionality still in development:
'''
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
'''





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
