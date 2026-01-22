import json
from editor.strings import MAIN_OPTIONS
from shared import prompt, cls

locations = []

def create_character():
    name = prompt("Character name?")
    location = None
    if len(locations) == 0:
        print("The character can't be placed in a location, since you haven't made any. You can associate the character with a location later if you want.")
    else:
        ans = yes_no("Add the character to a location?")
        if ans:
            location = get_locations()
    responses = character_responses()

    character = {
        "name": name,
        "responses": responses,
        "location": location
    }

    cls()
    print(character)

    write_data_json(f"character_{name}", character)

def character_responses():
    responses = dict()
    ans = yes_no("Add a response to a question for this character?")
    while ans:
        topic = prompt("What should the response be in regards to? (i.e., if asked via \"talk to {{character}} about ____)")
        response = prompt("What should the character's response be?")
        dependent = yes_no("Is this response dependent on a condition?")
        condition = None
        if dependent:
            condition = get_condition()
        responses[topic] = {
            "response": response,
            "condition": condition
        }
        ans = yes_no("Add another response?")

    return responses
    

def get_condition():
    return "test-condition"

def get_locations():
    print(locations)
    return "test-location"

# returns true if "y" is typed, and false if "n" is typed
def yes_no(question):
    answer = None
    while answer != "y" and answer != "n":
        answer = prompt(f"{question} y/n").lower()
        if answer != "y" and answer != "n":
            print("Please enter either y or n")
    return answer == "y"

def write_data_json(filename, data): 
    with open(f'{filename}.json', 'w') as f:
        json.dump(data, f)


# main loop
def main_loop():
    command = prompt(f"What do you want to do?\n{MAIN_OPTIONS}")
    match command:
        case "c":
            create_character()
        case "1":
            create_character()