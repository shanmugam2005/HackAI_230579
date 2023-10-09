from enum import Enum
import requests
from uagents import Context ,Model,protocol


City_name=input("Enter the city name: ")
tem_min=input("Enter preffered temperature minimum: ")
tem_max=input("Enter preffered temperature maximum: ")


base_url="https://api.openweathermap.org/data/2.5/weather"
api_key="e95f4af021fdb8cdf90c73a028154f7e"
A={
    "q":City_name,
    "appid":api_key,
    "units":"metric"
}
response=requests.get(base_url,A)
data=response.json()
tem=data['main']['temp']


class TemperatureAssign(Model):
    Location:str
    Temp_min:str
    Tem_max:str

class Original_Temperature(str,Enum):
    temperature=tem
    
def getstored():
    Data={
        1:TemperatureAssign(Location=City_name,Temp_min=tem_min,Tem_max=tem_max)
    }
    return Data
def Tem():
    return tem


    
    



