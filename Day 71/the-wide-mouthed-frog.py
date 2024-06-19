"""
The wide-mouth frog is particularly in the eating habits of the other creatures.

He just can't stop asking the creatures he encounterswhat they like to eat. But, then he meets the alligators who just LOVES to eat wide mouthed frogs!

Whn he meets the alligator, it then makes a tiny mouth.

Your goal in this kata is to create complete the mouth_size method, this method takes ine argument animal which corresponds to the animal ecountered by the frog. If this one is an alligator (case-insensitive) return small otherwise return wide
"""

def mouth_size(animal: str) -> str:
    return 'small' if animal.lower() == 'alligator' else 'wide'