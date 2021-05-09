from datetime import date
import requests, json

def city():
    api_key = "6f7b49df81ed5a5169db6228fa0ffd7a"
    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # Give city name
    city_name = input("Enter city name : ")
    # complete_url variable to store
    # complete url address
    complete_url = base_url + "q=" + city_name+"&appid="+api_key 
    # get method of requests module
    # return response object
    response = requests.get(complete_url)
    # json method of response object 
    # convert json format data into
    # python format data
    x = response.json()
    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
        # store the value of "main"
        # key in variable y
        y = x["main"]
      
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
      
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]
      
        # store the value corresponding
        # to the "humidity" key of y
        current_humidiy = y["humidity"]
      
        # store the value of "weather"
        # key in variable z
        z = x["weather"]
      
        # store the value corresponding 
        # to the "description" key at 
        # the 0th index of z
        weather_description = z[0]["description"]
      
        # print following values
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) + 
              "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
              "\n humidity (in percentage) = " +
                        str(current_humidiy) +
              "\n description = " +
                        str(weather_description)+"\n")  
    else:
        print(" City Not Found ")
        
botname = "noobbot- "
today = date.today()
name = input(botname+"Enter your name\n").upper()
print("welcome to noobbot-"+name+"\n"+str(today))

while 1:
    a = input(botname+"Enter your queries or type 'bye' to exit\n")
    if "help" in a.lower():
        print(botname+"How can i help you")
    elif "date" in a.lower():
        print(today)

    elif "hi" in a.lower():
        print(botname+"hii "+name)

    elif "complain" in a.lower():
        print(botname+"Our authorities will contact you shortly")


    elif "product" in a.lower():
        print(botname+"We have a wide range of products available")

    elif "weather" in a.lower():
        print(botname+"Enter your city to know the weather details\n")
        city()

    elif "mood" in a.lower():
        print(botname+"I am Happy today")

    elif ("bye" or "exit") in a.lower():
        print(botname+"See you Later "+name)
        break
    else:
        print("invalid Command")

