import random
from game_data import data
import art
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def randomise_elements():
    """
    Returns a list of all elements in randomised order - ready to be used in game.
    """
    elements_to_compare = data.copy()
    random.shuffle(elements_to_compare)

    return elements_to_compare


def compare_elements(element_one, element_two):
    """
    Returns the element with more followers in list format ('A' or 'B' as a result and the winner element itself)
    """
    if element_one["follower_count"] > element_two["follower_count"]:
        return ["A", element_one]
    elif element_one["follower_count"] < element_two["follower_count"]:
        return ["B", element_two]


# Main game loop - recursively comparing elements, asking player for input and determining if player is right,
# or ending the game if guess was wrong. Calculating score by recursively passing it as parameter.
def game(elements_to_compare, total_score, previous_element):
    score = total_score

    list_of_elements = elements_to_compare
    element_one = previous_element
    element_two = list_of_elements.pop()

    print(f"Compare A: {element_one['name']}, a {element_one['description']}, from {element_one['country']}.")
    print(art.vs)
    print(f"Compare B: {element_two['name']}, a {element_two['description']}, from {element_two['country']}.")

    winner_element = compare_elements(element_one, element_two)
    player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if player_choice == winner_element[0]:
        score += 1
        clear()
        print(art.logo)
        print(f"You're right! Current score: {score}")
        game(list_of_elements, score, winner_element[1])
    else:
        clear()
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")


print(art.logo)
list_of_elements_for_game_loop = randomise_elements()
game(list_of_elements_for_game_loop, 0, list_of_elements_for_game_loop.pop())
