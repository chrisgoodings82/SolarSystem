#chat.py
import long_responses as long
import re

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
    # Salutations
    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words= ['how'])

    # Direct Responses
    response(f"response | {long.R_PLUTO}", ['is', 'pluto', 'a', 'planet'], required_words= ['pluto', 'planet'])
    
    # Display all data about all planets
    response(f"display | all | all | all", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'planets'], required_words= ['planets'])

    # Display data about mercury
    response(f"display | all | all | mercury", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'mercury'], required_words= ['mercury'])
    response(f"display | fact | mass | mercury", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'mercury'], required_words= ['mercury'])
    response(f"display | fact | distance | mercury", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'mercury'], required_words= ['mercury'])
    response(f"display | fact | satellites | mercury", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'mercury'], required_words= ['mercury'])
    response(f"display | fact | moons | mercury", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'mercury'], required_words= ['mercury', 'moons'])
    response(f"display | fact | radius | mercury", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'mercury'], required_words= ['mercury'])

    # Display data about venus
    response(f"display | all | all | venus", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'venus'], required_words= ['venus'])
    response(f"display | fact | mass | venus", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'venus'], required_words= ['venus'])
    response(f"display | fact | distance | venus", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'venus'], required_words= ['venus'])
    response(f"display | fact | satellites | venus", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'venus'], required_words= ['venus'])
    response(f"display | fact | moons | venus", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'venus'], required_words= ['venus', 'moons'])
    response(f"display | fact | radius | venus", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'venus'], required_words= ['venus'])

    # Display data about earth
    response(f"display | all | all | earth", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'earth'], required_words= ['earth'])
    response(f"display | fact | mass | earth", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'earth'], required_words= ['earth'])
    response(f"display | fact | distance | earth", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'earth'], required_words= ['earth'])
    response(f"display | fact | satellites | earth", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'earth'], required_words= ['earth'])
    response(f"display | fact | moons | earth", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'earth'], required_words= ['earth', 'moons'])
    response(f"display | fact | radius | earth", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'earth'], required_words= ['earth'])

    # Display data about mars
    response(f"display | all | all | mars", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'mars'], required_words= ['mars'])
    response(f"display | fact | mass | mars", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'mars'], required_words= ['mars'])
    response(f"display | fact | distance | mars", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'mars'], required_words= ['mars'])
    response(f"display | fact | satellites | mars", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'mars'], required_words= ['mars'])
    response(f"display | fact | moons | mars", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'mars'], required_words= ['mars', 'moons'])
    response(f"display | fact | radius | mars", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'mars'], required_words= ['mars'])

    # Display data about jupiter
    response(f"display | all | all | jupiter", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'jupiter'], required_words= ['jupiter'])
    response(f"display | fact | mass | jupiter", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'jupiter'], required_words= ['jupiter'])
    response(f"display | fact | distance | jupiter", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'jupiter'], required_words= ['jupiter'])
    response(f"display | fact | satellites | jupiter", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'jupiter'], required_words= ['jupiter'])
    response(f"display | fact | moons | jupiter", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'jupiter'], required_words= ['jupiter', 'moons'])
    response(f"display | fact | radius | jupiter", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'jupiter'], required_words= ['jupiter'])

    # Display data about saturn
    response(f"display | all | all | saturn", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'saturn'], required_words= ['saturn'])
    response(f"display | fact | mass | saturn", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'saturn'], required_words= ['saturn'])
    response(f"display | fact | distance | saturn", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'saturn'], required_words= ['saturn'])
    response(f"display | fact | satellites | saturn", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'saturn'], required_words= ['saturn'])
    response(f"display | fact | moons | saturn", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'saturn'], required_words= ['saturn', 'moons'])
    response(f"display | fact | radius | saturn", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'saturn'], required_words= ['saturn'])

    # Display data about uranus
    response(f"display | all | all | uranus", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'uranus'], required_words= ['uranus'])
    response(f"display | fact | mass | uranus", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'uranus'], required_words= ['uranus'])
    response(f"display | fact | distance | uranus", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'uranus'], required_words= ['uranus'])
    response(f"display | fact | satellites | uranus", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'uranus'], required_words= ['uranus'])
    response(f"display | fact | moons | uranus", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'uranus'], required_words= ['uranus', 'moons'])
    response(f"display | fact | radius | uranus", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'uranus'], required_words= ['uranus'])

    # Display data about neptune
    response(f"display | all | all | neptune", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'neptune'], required_words= ['neptune'])
    response(f"display | fact | mass | neptune", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'neptune'], required_words= ['neptune'])
    response(f"display | fact | distance | neptune", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'neptune'], required_words= ['neptune'])
    response(f"display | fact | satellites | neptune", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'neptune'], required_words= ['neptune'])
    response(f"display | fact | moons | neptune", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'neptune'], required_words= ['neptune', 'moons'])
    response(f"display | fact | radius | neptune", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'neptune'], required_words= ['neptune'])

    # Provide comparrison data
    response(f"compare | all | all | all", ['tell', 'me', 'show', 'display', 'present', 'all', 'everything', 'about', 'relating', 'to', 'neptune'], required_words= ['neptune'])
    response(f"compare | fact | mass | all", ['tell', 'me', 'show', 'display', 'present', 'mass', 'weight', 'massive', 'about', 'relating', 'to', 'neptune'], required_words= ['neptune'])
    response(f"compare | fact | distance | all", ['tell', 'me', 'show', 'display', 'present', 'distance', 'how', 'far','from', 'the','sun', 'close', 'to', 'is', 'neptune'], required_words= ['neptune'])
    response(f"compare | fact | satellites | all", ['tell', 'me', 'show', 'display', 'present', 'how', 'many', 'moons', 'satellitees', 'orbit', 'orbiting', 'neptune'], required_words= ['neptune'])
    response(f"compare | fact | moons | all", ['what', 'are', 'list', 'show', 'display', 'the', 'moons', 'of', 'neptune'], required_words= ['neptune', 'moons'])
    response(f"compare | fact | radius | all", ['tell', 'me', 'show', 'display', 'present', 'radius', 'width', 'of', 'neptune'], required_words= ['neptune'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match                  # End: check_all_messages

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
            for item in planets:
                output += item.display_all_data()
        else:
            pl = [p for p in planets if p.name == planet]
            output += pl.display_all_data()
    else:
        if planet == "all":
            for item in planets:
                output += item.display_fact(fact)
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