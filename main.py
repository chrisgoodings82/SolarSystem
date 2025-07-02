# Main.py
'''
The chat bot feature was developed and adapted from an online YouTube tutorial
[1] Indently (2021) "How to create an accurate Chat Bot Response System in Python Tutorial (2021)". https://www.youtube.com/watch?v=Ea9jgBjQxEs. Accessed on: 02/07/2025
'''
import planet
import re
import long_responses as long
from tabulate import tabulate

planets = []
def init_planets():
    planets.append(planet.planet("Mercury"))
    planets.append(planet.planet("Venus"))
    planets.append(planet.planet("Earth"))
    planets.append(planet.planet("Mars"))
    planets.append(planet.planet("Jupiter"))
    planets.append(planet.planet("Saturn"))
    planets.append(planet.planet("Uranus"))
    planets.append(planet.planet("Neptune"))

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Count how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculate the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    
    # Convert to a percentage
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0
    
def check_all_messages(message):
    highest_prob_list = {}

    # Helper function to generate a list of the highest probability responses
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses ------------------------------------------------------------------------------------------------------
    # Response: Action | Detail | Fact | Planet | Message
    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words= ['how'])

    response(f"response | {long.R_PLUTO}", ['is', 'pluto', 'a', 'planet'], required_words= ['pluto', 'planet'])
    response(f"display | all | all | all", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'planets'], required_words= ['planets'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def split_response(response):
    return response.split("|")
    

def display_fact(response):
    global planets
    split_response_string = split_response(response)
    fact = split_response_string[2].strip()
    planet = split_response_string[3].strip()
    output = ""
    if fact == "all":
        if planet == "all":
            for planet in planets:
                output += planet.display_all_data()
        else:
            pl = [p for p in planets if p.name == planet]
            output += pl.display_all_data()
    else:
        if planet == "all":
            for planet in planets:
                output += planet.display_fact(fact)
        else:
            pl = [p for p in planets if p.name == planet]
            output += pl.display_fact(fact)
    return output

def compare_fact(response):
    global planets
    split_response_string = split_response(response)
    fact = split_response_string[2].strip()
    planet = split_response_string[3].strip()
    planet_list = []
    if fact == "all":
        for planet in planets:
                planet_list.append(planet.export_data())
        return tabulate(planet_list, headers=['name', 'mass', 'distance', 'satellites', 'moons', 'radius'])
    else:
        for planet in planets:
                planet_list.append(planet.__getattribute__(fact))
    return tabulate(planet_list, headers=[fact])
    
def response_parser(response):
    if "display" in response:
        return display_fact(response)
    if "response" in response:
        return response[11:]
    if "compare" in response:
        return compare_fact(response)

def get_response(user_input):
    split_message = re.split(r'\s+|[?.,\';:-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    parsed_response = response_parser(response)
    return parsed_response

if __name__ == "__main__":
    
    while True:
        print('Bot: ' + get_response(input('You: ')))
   