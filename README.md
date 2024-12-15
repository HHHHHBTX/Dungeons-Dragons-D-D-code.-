# Dungeons & Dragons (D&D) AI Dungeon Master

## Project Overview  
This project implements an AI-driven Dungeon Master (DM) for a text-based Dungeons & Dragons game. The AI dynamically generates room descriptions, handles encounters, and ensures the game world persists across player sessions. This project adheres to simplified D&D mechanics, balancing creative storytelling with consistent state management.

---

## Features  
### 1. **World Memory**  
- Tracks player actions and saves states, such as:  
   - NPC defeated  
   - Unlocked doors  
   - Player inventory and HP  
- Ensures continuity across game sessions with persistent state management.

### 2. **Map Generation and Navigation**  
- The game world is structured as interconnected rooms (a grid/node-based map).  
- Players can move in directions like `north`, `south`, `east`, or `west` based on available connections.  

### 3. **Dynamic Descriptions and Interactions**  
- **OpenAI Integration**: The program uses OpenAI's GPT model to generate immersive and unique room descriptions.  
- Randomized encounters (e.g., goblins, treasure chests, empty rooms) enhance the experience.  

### 4. **Simplified D&D Mechanics**  
- **Combat**: NPCs and players roll a six-sided die (1d6) plus attack power to determine damage.  
- **Skill Checks**: Players roll a ten-sided die (1d10) for risky actions like unlocking doors. Success depends on the difficulty.  
- **Inventory**: Simple items like health potions or keys with straightforward effects.  
- **Leveling (Optional)**: Players gain experience points (XP) for key actions and level up at 50 XP.  

---

## File Structure  
- **`main.py`**: The main game loop, integrating all components.  
- **`state_manager.py`**: Handles saving and loading the game state (`game_state.json`).  
- **`map_generator.py`**: Defines the game world, including room connections and movement logic.  
- **`description_generator.py`**: Generates room descriptions and random encounters using OpenAI's GPT API.  
- **`game_logic.py`**: Implements combat, skill checks, and inventory use.  
- **`game_state.json`**: Saves the current state of the game world and player progress.  

---

## Prerequisites  
1. Python 3.8 or higher  
2. OpenAI API key  

### Install Dependencies  
Run the following command to install required libraries:  
```bash
pip install openai
