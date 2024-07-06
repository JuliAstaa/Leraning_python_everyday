"""  
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application  form that will tell prospective memvers which category they will be placed.

To be a senoir, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicapa range from -2 to +26; the better the player the lower the handicap.

Input:
input will consist od a list of pairs. Each pair contain information for single potential member. Information constist of an integer for the person's age and an integer for the person's handicap.

Output:
Output will consist of a list of string values stating the respetive member is to be placed in the senior or open category

Example:
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
"""

def open_or_senior(data:list[tuple[int]]) -> list[str]:
    return ["Senior" if member[0] >= 55 and member[1] > 7 else "Open" for member in data]


print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))