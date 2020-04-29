import requests, time, datetime

URL = "http://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us&units=imperial&APPID=09110e603c1d5c272f94f64305c09436"

class weather:
    '''
    Creates an array of forcast objects for the next 5 unique days - Removes duplicates by only saving
    the first instance of unique date found.
    Prints out best contact method for each of the 5 day depending on the forcast objects temp value -
    temp above 75 will suggest text message as the best contact method.
    temp below 55 will suggest phone call as the best contact method.
    temps between, and including, 75 and 55 will suggest email as the best contact method.
    '''

    def __init__(self):
        resp = requests.get(url=URL)
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        count = 0
        if (resp.status_code == 200):
            resp = resp.json()["list"]
            forecasts = []
            for info in resp:
                day = convertEpochTimestamp(info["dt"])
                if(day != yesterday):
                    if (count != 5):
                        temp = info["main"]["temp"]
                        newForecast = forecast(day, temp)
                        forecasts.append(newForecast)
                        yesterday = day
                        count = count + 1
                        if (newForecast.temp > 75):
                            print("Text message is best for", day)
                        if(newForecast.temp < 55):
                            print("Phone call is best for", day)
                        else:
                            print("Sending an Email is best for", day)
        else:
            print("There was an error making a call to ", URL)
            print("Received error code: ", resp.status_code)

'''
method converts epoch time to standard datetime format
'''
def convertEpochTimestamp(epochValue):
    return time.strftime("%m-%d-%Y", time.localtime(epochValue))

class forecast:
    '''
    Creates a forcast object with attributes
    day: string
    temp: int
    '''

    def __init__(self, day, temp):
        self.day = day
        self.temp = temp

if __name__ == "__main__":
    print("Started Processes.")
    weather()
    print("All Done. :)")
