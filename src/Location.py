from uagents import Context,Model,Protocol



    
class Location_Check(Model):
    location:str

class Location_response(Model):
    status:bool

Temp_proto=Protocol()

@Temp_proto.on_message(model=Location_Check,replies={Location_response})
async def handle_Location_check(ctx:Context, sender:str ,msg:Location_Check):
    if(ctx.storage.has(msg.location)):
        status=True
        ctx.logger.info("sssssss")
    else:
        status=False
    await ctx.send(sender,Location_response(status=status))
    
    
        




