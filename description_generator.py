import openai
import random

def generate_description(base_prompt, api_key):
    """Generates a dynamic description using OpenAI API."""
    openai.api_key = api_key
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=base_prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def spawn_random_encounter():
    """Generates a random encounter."""
    encounters = [
        "A goblin appears!",
        "You found a treasure chest.",
        "The room is eerily empty.",
        "A trap is triggered!"
    ]
    return random.choice(encounters)