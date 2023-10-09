

from uagents import Agent, Context, Bureau,Model
from uagents.setup import fund_agent_if_low

from src.GetWeatherData import TemperatureAssign,Original_Temperature,getstored,Tem
from src.TemperatureCheck import Temperature_check,Temperature_response,Check_proto
from src.Location import Location_Check,Location_response,Temp_proto





data=getstored()
tem=Tem()





TemperatureAgent=Agent(name="TemperatureAgent",seed="TemperatureAgent recovery phrase")
TemperatureAgent.include(Temp_proto)
TemperatureAgent.include(Check_proto)

User_alert_agent=Agent(name="User_alert_agent",seed="User_alert_agent recovery phrase")



city_name=data[1].Location
for (number, status) in data.items():
    TemperatureAgent._storage.set(number, status.dict())
    
    
fund_agent_if_low(TemperatureAgent.wallet.address())

fund_agent_if_low(User_alert_agent.wallet.address())

    
    
    
@User_alert_agent.on_interval(period=80.0,messages=Location_Check)
async def interval(ctx:Context,):
    completed=ctx.storage.get("completed")
    if not completed:
        await ctx.send(TemperatureAgent.address,Location_Check(location=city_name))
        
        
        
        
        

@User_alert_agent.on_message(Location_response,replies=Temperature_check)
async def handle_Location_response(ctx:Context,sender:str,msg:Location_response):
    if(msg.status==False):
        ctx.logger.info("The Location has already defined temp_min and tem_max")
        await ctx.send(sender,Temperature_check(Temperature=tem))
    else:
        ctx.logger.info("The Location does not have Temp_min and Temp_min")
        
        
        
        
        
    
@User_alert_agent.on_message(Temperature_response)
async def handle_temperature_response(ctx:Context,sender:str,msg:Temperature_response):
    if(msg.status):
        ctx.logger.info("The temperature is not statified your Tem_min and Tem_max data ")
    else:
        ctx.logger.info("The temperature is Normal")
    ctx.storage.set("completed",False)
    



bureau = Bureau()
bureau.add(TemperatureAgent)
bureau.add(User_alert_agent)

if __name__ == "__main__":
    bureau.run()

