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
    "Trout", "Carp", "Eel", "Sting Ray", "Salmon", "Crab",
    "Guppy", "Shark", "Sea Horse", "Sea Snake", "Sponge",
    "Starfish", "Squirrel", "Squid", "Plankton", "Lobster"
]

COMMON_DESCRIPTIONS = [
    "A fairly common fish found.",
    "A peaceful swimmer that keeps to itself.",
    "Spends most of its day looking for snacks.",
    "Lives in a pineapple under the sea."
]

UNCOMMON_DESCRIPTIONS = [
    "A sturdy fish known to put up a decent fight.",
    "Prefers quiet coves and shaded waters.",
    "Not rare, but it's something I guess.",
    "Really loves Texas for some reason."
]

RARE_DESCRIPTIONS = [
    "Its scales shimmer like stardust under moonlight.",
    "Said to appear only when the waters fall silent.",
    "Finding one is considered a very good omen.",
    "Said to be looking for a secret formula."
]

LEGENDARY_DESCRIPTIONS = [
    "Legends claim it guides lost sailors to safety.",
    "Its presence seems to change the mood of the water.",
    "Said to have lived for centuries beneath the waves.",
    "Cover your ears, this one plays the clarinet, horribly."
]

MYTHIC_DESCRIPTIONS = [
    "A mythical creature most people only hear about in stories.",
    "Glows softly as if carrying ancient light inside... or it swallowed your tamagotchi.",
    "Old sailors insist this fish can change a person’s fate.",
    "Who you calling pinhead?"
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
