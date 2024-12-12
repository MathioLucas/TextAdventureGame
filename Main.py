import random

# Game Map Constants
MAP_WIDTH = 5
MAP_HEIGHT = 5
TERRAIN_TYPES = ["Forest", "River", "Mountain", "Plains"]

# Player Starting Position
player_position = [0, 0]
inventory = []

# Procedural Map Generation
def generate_map(width, height):
    return [[random.choice(TERRAIN_TYPES) for _ in range(width)] for _ in range(height)]

game_map = generate_map(MAP_WIDTH, MAP_HEIGHT)

# Display Map Function
def display_map():
    print("\n=== GAME MAP ===")
    for y in range(MAP_HEIGHT):
        row = ""
        for x in range(MAP_WIDTH):
            if [y, x] == player_position:
                row += "[P] "
            else:
                row += f"[{game_map[y][x][0]}] "
        print(row)
    print("================\n")

# Move Player
def move_player(direction):
    global player_position
    y, x = player_position
    if direction == "north" and y > 0:
        player_position[0] -= 1
    elif direction == "south" and y < MAP_HEIGHT - 1:
        player_position[0] += 1
    elif direction == "west" and x > 0:
        player_position[1] -= 1
    elif direction == "east" and x < MAP_WIDTH - 1:
        player_position[1] += 1
    else:
        print("You can't move in that direction!")

# Random Event Generator
def random_event():
    events = [
        "You found a treasure chest with a shiny sword!",
        "A wild goblin attacks! Prepare for battle.",
        "You meet a wandering merchant who offers you supplies.",
        "The area is calm and peaceful. Nothing happens.",
        "You discover an ancient ruin with mysterious carvings."
    ]
    return random.choice(events)

# Main Game Loop
def main():
    print("Welcome to the Text Adventure Game!")
    print("Explore the map, encounter events, and gather treasures.")
    print("Type 'north', 'south', 'east', or 'west' to move.")
    print("Type 'quit' to end the game.\n")

    simulated_inputs = iter(["north", "east", "south", "quit"])

    while True:
        display_map()
        try:
            command = next(simulated_inputs).strip().lower()
        except StopIteration:
            print("No more inputs available. Exiting game.")
            break

        print(f"Command: {command}")  # Show the command being processed

        if command in ["north", "south", "east", "west"]:
            move_player(command)
            event = random_event()
            print(f"\n{event}\n")
            if "treasure chest" in event:
                inventory.append("Shiny Sword")
                print("Added Shiny Sword to your inventory!\n")
        elif command == "quit":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid command! Try again.\n")

# Run the Game
if __name__ == "__main__":
    main()
