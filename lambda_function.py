import json
import requests
from constants import WEBSOCKET_BASE_URL

def lambda_handler(event, context):
    print("DEBUG: event:", event)
    body = json.loads(event.get("body", "{}"))
    chat_id = body.get('chat_id')
    token = body.get('token')
    action = body.get('action')
    message = body.get('message')
    
    headers = {
        "Authorization": f"Bearer {token}"
    }

    print("DEBUG: chat_id:", chat_id)
    print("DEBUG: token:", token)
    
    if action == "chat_history":
        url = f"{WEBSOCKET_BASE_URL}/api/chat-history/{chat_id}/"
        print("DEBUG: url:", url)
        response = requests.get(url, headers=headers)
        print("DEBUG: response:", response.text)
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(response.json()),
            "isBase64Encoded": False
        }
        
    elif action == "chat":
        url = f"{WEBSOCKET_BASE_URL}/api/chat-response/"
        payload = {
            "chat_id": chat_id,
            "message": message
        }
        print("DEBUG: url:", url)
        response = requests.post(url, json=payload, headers=headers)
        print("DEBUG: response:", response.text)
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(response.json()),
            "isBase64Encoded": False
        }

    return {
        "statusCode": 400,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"error": "Invalid input"})
    }
