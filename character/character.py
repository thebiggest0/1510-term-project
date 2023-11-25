"""
ADD A DOCSTRING
"""


def creat_character(name):
    """
    Create a character with specified attributes.
    """
    character_info = {
        'name': name,
        'level': 1,
        'experience': 0,
        'hp': 50,
        'str': 15,
        'int': 15,
        'dex': 15,
        'x-coordinate': 0,
        "y-coordinate": 0
    }
    return character_info


def level_up(character_info):
    """
    Increase level of the character.
    """
    experience_deduction = [100,200,300,500]
    character_info['experience'] -= experience_deduction[character_info['level'] - 1]
    character_info['level'] += 1
    print(f"Congratulations! You've leveled up.")
    return character_info

def main():


if __name__ == "__main__":
    main()
