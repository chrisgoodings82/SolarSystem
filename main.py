# Main.py
'''
The chat bot feature was developed and adapted from an online YouTube tutorial [1]. The base functionality the gets the response and
checks the messages was from the tutorial. I extended it to produce a formatted string response, that is subsequently parsed to 
allow for specific information to be displayed.
[1] Indently (2021) "How to create an accurate Chat Bot Response System in Python Tutorial (2021)". https://www.youtube.com/watch?v=Ea9jgBjQxEs. Accessed on: 02/07/2025
'''
import planet
import chat

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

if __name__ == "__main__":
    init_planets()
    while True:
        print('Bot: ' + chat.get_response(input('You: ')))
   