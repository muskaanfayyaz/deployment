from fastapi import FastAPI
import random

app = FastAPI()

jokes = [
    "Why don't skeletons fight each other? They don't have the guts!",
    "What do you call cheese that isn't yours? Nacho cheese!",
    "Why couldn't the bicycle stand up by itself? It was two tired!",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "Why do cows have hooves instead of feet? Because they lactose!"
]

@app.get("/jokes")
def get_random_joke():
    return {"joke": random.choice(jokes)}
