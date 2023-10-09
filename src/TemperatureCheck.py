from uagents import Context ,Model,Protocol
from src.GetWeatherData import getstored
data=getstored()
Tem_minimum=data[1].Temp_min
Tem_maximum=data[1].Tem_max

class Temperature_check(Model):
    Temperature:str
class Temperature_response(Model):
    status:bool

Check_proto=Protocol()


@Check_proto.on_message(model=Temperature_check,replies=Temperature_response)
async def handle_Temperature_check(ctx:Context,sender:str,msg:Temperature_check):
    if((float(Tem_minimum)> float(msg.Temperature)) or (float(Tem_maximum)<float(msg.Temperature))):
        status=True
    else:
        status=False
    await ctx.send(sender,Temperature_response(status=status))
    