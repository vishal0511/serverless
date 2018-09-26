from __future__ import print_function
from datetime import datetime
import time
import json

def handler(event, context):
    var = gettime()
    toprint = [str(var),'Hello from Vishal']
    response = response_msg(True, json.dumps(toprint))
    return response
    
def gettime():
  return datetime.now()  

def response_msg(value, body):
    if value == True:
        response = {'statusCode': 200, 'headers': {'Content-Type': 'application/json'}, 'body': body}
    else:
        response = {'statusCode': 400, 'headers': {'Content-Type': 'application/json'}, 'body': body}
    return response


