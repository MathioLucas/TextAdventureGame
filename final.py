from fastapi import FastAPI
from pydantic import BaseModel
import random

# Constants
MAP_WIDTH = 5
MAP_HEIGHT = 5
TERRAIN_TYPES = ["Forest", "River", "Mountain", "Plains"]

# Initialize App
app = FastAPI()

# Game State
game_state = {
    "player_position": [0, 0],
    "inventory": [],
    "map": [[random.choice(TERRAIN_TYPES) for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
}

# Models
class MoveRequest(BaseModel):
    direction: str

# Helper Functions
def move_player(direction):
    y, x = game_state["player_position"]
    if direction == "north" and y > 0:
        game_state["player_position"][0] -= 1
    elif direction == "south" and y < MAP_HEIGHT - 1:
        game_state["player_position"][0] += 1
    elif direction == "west" and x > 0:
        game_state["player_position"][1] -= 1
    elif direction == "east" and x < MAP_WIDTH - 1:
        game_state["player_position"][1] += 1
    else:
        return "You can't move in that direction!"
    return "Moved successfully."

def random_event():
    events = [
        "You found a treasure chest with a shiny sword!",
        "A wild goblin attacks! Prepare for battle.",
        "You meet a wandering merchant who offers you supplies.",
        "The area is calm and peaceful. Nothing happens.",
        "You discover an ancient ruin with mysterious carvings."
    ]
    return random.choice(events)

# API Endpoints
@app.get("/map")
def get_map():
    """Returns the game map and player position."""
    return {
        "map": game_state["map"],
        "player_position": game_state["player_position"]
    }

@app.get("/inventory")
def get_inventory():
    """Returns the player's inventory."""
    return {"inventory": game_state["inventory"]}

@app.post("/move")
def move(move_request: MoveRequest):
    """Handles player movement."""
    direction = move_request.direction.lower()
    if direction not in ["north", "south", "east", "west"]:
        return {"message": "Invalid direction! Use north, south, east, or west."}

    move_message = move_player(direction)
    event = random_event()

    if "treasure chest" in event:
        game_state["inventory"].append("Shiny Sword")

    return {
        "move_message": move_message,
        "event": event,
        "player_position": game_state["player_position"],
        "inventory": game_state["inventory"]
    }

@app.get("/status")
def get_status():
    """Returns the current game status."""
    return {
        "player_position": game_state["player_position"],
        "inventory": game_state["inventory"],
        "map": game_state["map"]
    }

# To run the server: Use `uvicorn filename:app --reload`
