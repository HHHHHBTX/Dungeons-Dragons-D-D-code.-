class Location:
    def __init__(self, name, description, connections):
        self.name = name
        self.description = description
        self.connections = connections
        self.visited = False

locations = {
    "room_1": Location("room_1", "A dark dungeon entrance.", {"north": "room_2"}),
    "room_2": Location("room_2", "A brightly lit hall with chandeliers.", {"south": "room_1", "east": "room_3"}),
    "room_3": Location("room_3", "A mysterious library filled with ancient books.", {"west": "room_2"})
}

def move_player(current_location, direction):
    """Moves the player to a connected location if possible."""
    if direction in locations[current_location].connections:
        return locations[current_location].connections[direction]
    return current_location