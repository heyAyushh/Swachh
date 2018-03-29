# Garbage Classifier 
This project constitutes for garbage detection and classifier within a area using  
microsoft custom vision, Azure functions, Raspberry pi and a Camera.  
  
Use of this project lies in the urban places where people throw trash and   
garbage on street regardless of having a dustbin nearby.  
This project can detect garbages and turn the sound ON whenever it  
detects some recyclable or non recyclable stuff.   

Login to Azure portal and create a new Custom Vision Instance.  
use the dataset in this repo to train the model.  

Login to cloudmqtt.com or adafruit.io  
to setup a free instance of Mqtt broker.   
  
# In production

> Fill up and save .env file in func folder  
> Deploy func as a function app in azure portal  
> execute in bash terminal ``` export a=0``` (on Raspberry Pi)  
> execute in bash terminal ``` . ./schedule.sh```  (on Raspberry Pi)  
> execute ``` python clientMqtt.py ``` (on Raspberry Pi)  

# Testing Locally
## Setup
> Install Azure functions core  
> Fill up and save .env file  
> Enter details of blob storage account ( function storage account ) in pushblob.py  
## Run 
> execute in bash terminal ``` export a=0```  
> execute in bash terminal ``` . ./schedule.sh```  
> go in func folder and execute ``` func host start ```  

File an issue regarding this for anything :sparkles: