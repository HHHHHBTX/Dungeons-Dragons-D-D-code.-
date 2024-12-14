import random

def combat(player, npc):
    """Handles player vs NPC combat."""
    while player["hp"] > 0 and npc["hp"] > 0:
        player_roll = random.randint(1, 6) + player["attack"]
        npc_roll = random.randint(1, 6) + npc["attack"]
        npc["hp"] -= player_roll
        print(f"You hit the NPC for {player_roll} damage!")
        if npc["hp"] <= 0:
            return "You won the battle!"
        player["hp"] -= npc_roll
        print(f"The NPC hit you for {npc_roll} damage!")
    return "You lost the battle."

def skill_check(difficulty):
    """Performs a skill check based on a roll."""
    roll = random.randint(1, 10)
    return roll >= difficulty