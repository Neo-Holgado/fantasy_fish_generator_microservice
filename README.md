# Fantasy Fish Generator Microservice  
### A Python-based microservice with multiple services:    
`generate_fish`: Returns a randomized fantasy fish in the form of a dictionary  
`generate_fish_list`: Returns a list of multiple randomized fantasy fish in a list of dictionaries  

## Fish Format  
All fish generated will be in the following format:  
```python
{
  "name": "__name__",
  "description": "__description__",
  "rarity": "__rarity__",
  "value": __value__    # (int)
}
```

### Example  
```python
{
  "name": "Tiny Trout",
  "description": "A small but lively trout.",
  "rarity": "Common",
  "value": 5
}
```

## Fantasy Fish Possibilities
The following are lists of the possible values for each key:
```python
# Prefix for Name
PREFIXES = [
    "Shimmering", "Ancient", "Crystal", "Shadow", "Ethereal",
    "Molten", "Void", "Glowing", "Stormforged", "Icy", "Tiny"
]

# Species for Name
SPECIES = [
    "Trout", "Carp", "Eel", "Ray", "Salmon", "Wyrm",
    "Guppy", "Finback", "Stalker", "Scale Serpent"
]

DESCRIPTIONS = [
    "A mysterious creature said to be older than time.",
    "Glows with a faint magical light.",
    "Known to appear only under a full moon.",
    "Radiates intense elemental energy.",
    "A rare fish whispered about in old legends.",
    "Found only in enchanted waters.",
    "Beautiful and dangerous in equal measure.",
    "A favorite among wizards and alchemists.",
    "Its scales shimmer with hidden power.",
    "A shy but powerful elemental fish."
]

RARITIES = ["Common", "Uncommon", "Rare", "Legendary", "Mythic"]

# Value will be anywhere between the listed values
RARITY_VALUE = {
    "Common": (5, 15),
    "Uncommon": (16, 40),
    "Rare": (41, 100),
    "Legendary": (101, 250),
    "Mythic": (251, 500)
}
```

## Using the `generate_fish` Service  
### REQUEST Format  
To use the generate_fish service, you need to send a JSON-formatted message to the server, which includes:   
1. `service_key`: identifies which service to use.  For this service, use "generate_fish"  

### Example Format  
```python
message = {"service_key": "generate_fish"}
```

### Sending the Request (Local Server)  
```python  
import zmq


# Connect to server
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5556")

# Send the request
socket.send_json(message)
```
### Response Format  
The response is formatted as follows:  
```python
response = {"response": {__fish__}}
```

### Receiving the Response  
```python
response = socket.recv_json()
print("Received response from server:")
print(response)
```

## Using the `generate_fish_list` service  
### REQUEST Format  
To use the weather_state service, you need to send a JSON-formatted message to the server, which includes:    
1. `service_key`: Identifies which service to use.  For this service, use "generate_fish_list"  
2. `list_length`: Integer which describes the number of random fantasy fish you want to generate, stored in a list  

### Example Format
```python
message = {
  "service_key": "generate_fish_list",
  "list_length": 5
}
```

### Sending the Request (Local Server)  
```python  
import zmq


# Connect to server
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5556")

# Send the request
socket.send_json(message)
```
### Response Format  
The response is formatted as follows:  
```python
response = {"response": [{__fish1__}, {__fish2__}, {__fish3__}, {__fish4__}, {__fish5__}]}
```

### Receiving the Response  
```python
response = socket.recv_json()
print("Received response from server:")
print(response)
```

## Author
Neo Holgado

## Tech Stack
- Python
- ZeroMQ (pyzmq) - Microservice communication
