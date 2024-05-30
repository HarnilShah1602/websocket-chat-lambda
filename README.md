# Lambda Function for WebSocket Integration
This repository contains a Lambda function designed for WebSocket integration with AWS API Gateway. Below is a brief overview of what this code does:

Input Handling: The function receives WebSocket requests in the form of event objects.

Parsing: It parses the request body to extract essential parameters such as chat ID, token, action, and message.

Routing: Based on the action specified in the request, the function performs different operations:
If the action is "chat_history", it fetches chat history from the specified WebSocket endpoint.
If the action is "chat", it sends a message to the specified chat ID via the WebSocket endpoint.

HTTP Requests: The function uses the requests library to make HTTP GET or POST requests to the WebSocket endpoint, passing necessary parameters and headers.

Response Handling: It handles responses from the WebSocket endpoint, returning appropriate HTTP status codes and response bodies.

This Lambda function serves as a middleware between AWS API Gateway and the WebSocket endpoint, facilitating communication and handling various WebSocket actions.

For more details on WebSocket integration with AWS API Gateway, refer to the official documentation.

Feel free to customize and extend this code to suit your specific WebSocket integration needs! If you have any questions or need further assistance, don't hesitate to reach out.
