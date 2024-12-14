import state_manager
import map_generator
import description_generator
import game_logic

# Initial state
state_file = "game_state.json"
state = state_manager.load_state(state_file)
if not state:
    state = {
        "locations": {
            "room_1": {
                "description": "A dark dungeon entrance.",
                "state": {"door_locked": True, "npc_alive": True}
            },
            "room_2": {
                "description": "A brightly lit hall with chandeliers.",
                "state": {"door_locked": False, "npc_alive": True}
            },
            "room_3": {
                "description": "A mysterious library filled with ancient books.",
                "state": {"door_locked": False, "npc_alive": False}
            }
        },
        "player": {
            "hp": 30,
            "xp": 0,
            "inventory": ["torch"],
            "attack": 5
        }
    }
    state_manager.save_state(state, state_file)

current_location = "room_1"

while True:
    location = state["locations"].get(current_location)
    if location is None:
        print(f"Error: Location {current_location} not found.")
        break

    # Display the current location description
    print(location["description"])

    # Generate a random encounter
    encounter = description_generator.spawn_random_encounter()
    print(f"Encounter: {encounter}")

    # Player action
    action = input("Enter action (north, attack, skill, save, quit): ")
    if action in ["north", "south", "east", "west"]:
        # Move to a new location
        new_location = map_generator.move_player(current_location, action)
        if new_location != current_location:
            current_location = new_location
            print(f"You moved to {current_location}.")
        else:
            print("You cannot move in that direction.")
    elif action == "attack":
        # Simplified combat logic
        npc = {
            "hp": 10,  # NPC's health
            "attack": 3  # NPC's attack power
        }
        result = game_logic.combat(state["player"], npc)
        print(result)
        if result == "You won the battle!":
            state["player"]["xp"] += 10  # Gain XP after winning
    elif action == "skill":
        success = game_logic.skill_check(6)
        print("Skill check successful!" if success else "Skill check failed.")
    elif action == "save":
        state_manager.save_state(state, state_file)
        print("Game saved.")
    elif action in ["quit", "exit"]:
        print("Exiting game. Goodbye!")
        break
    else:
        print("Invalid action.")