import zmq


# Set up environment and sockets
context = zmq.Context()
print("Client attempting to connect to server...")
socket = context.socket(zmq.REQ)

# Connect to server socket
socket.connect("tcp://localhost:5556")

# Setup request for generate_fish service
request = {"service_key": "generate_fish"}

# Send Request
print("Sending Request...")
socket.send_json(request)

# Get the reply
response = socket.recv_json()

# Print response
print("Received response from server:")
print(response)

# Setup request for generate_fish_list service
request = {
    "service_key": "generate_fish_list",
    "list_length": 5
}

# Send Request
print("Sending Request...")
socket.send_json(request)

# Get the reply
response = socket.recv_json()

# Print response
print("Received response from server:")
print(response)
