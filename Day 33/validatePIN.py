import re
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

print(validate_pin("1234"))