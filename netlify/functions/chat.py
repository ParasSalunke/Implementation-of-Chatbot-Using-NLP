from http.server import BaseHTTPRequestHandler
import json
from ...app import bot  # Import your bot class

def handler(event, context):
    body = json.loads(event['body'])
    message = body.get('message', '')
    
    response = bot.get_response(message)
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'response': response
        })
    }