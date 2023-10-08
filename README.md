# Temperature_Alert_Agent111111

uAgents is a library developed by Fetch.ai that allows for creating autonomous AI agents in Python. With simple and expressive decorators, you can have an agent that performs various tasks on a schedule or takes action on various events.

# Step 1: Prerequisites
     Before starting, you'll need the following:
            Python (3.8+ is recommended)
            Poetry (a packaging and dependency management tool for Python
            Uagent Library
# Step 2: Set up .env file
        To run the demo, you need API keys from:
                OpenWeatherAPI
                
        OpenWeatherAPI
              Visit OpenAI.
              Sign up or log in.
              Navigate to the API section to obtain your API key.

# Step 3: Run the main script
          To run the project and its agents:
                         poetry run python main.py
          You need to look for the following output in the logs:
                         Adding top destinations agent to Bureau: {top_dest_address}

# Step 4: Set up the client script
          
    from uagents import Agent, Context, Bureau,Model
    from uagents.setup import fund_agent_if_low
    from src.GetWeatherData import TemperatureAssign,Original_Temperature,getstored,Tem
    from src.TemperatureCheck import Temperature_check,Temperature_response,Check_proto
    from src.Location import Location_Check,Location_response,Temp_proto

    GetWeatherData This to get collection of data from a OpenWeatherAPI.
                     TemperatureAssign     ===>  This Model to Assign Location,Minimum Temperature ,Maximum Temperature User defined value.
                     Original_Temperature  ===>  This Model to get a Temperature from defined Location.
                     getstored             ===>  This Function to stored user defined value.
                     Tem                   ===>  This Function to return a actual Temperature of a Location.
    TemperatureCheck This to Check wheather Temperature is Normal or Not.
    Location This to Checl Already Location is present or not.

    This Code Send Alerting Message to particular period time.User also defined a value period of interval.

# Step 5: Run the client script

    Open a New Terminal on your system just type a below command to run an Temperature_Alert_Agent


                        python main.py 
                             or
               poetry run python top_dest_client.py


     Once you hit enter, a request will be sent to the Temperature_agent, and you will be able to see your results in the console!



                     
                







  

                




