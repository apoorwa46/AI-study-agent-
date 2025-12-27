import json

def save_memory(data, filename="memory.json"):
    """
    Saves learning progress locally.
    """
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
