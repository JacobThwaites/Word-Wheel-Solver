from get_solution import get_solution

def process_user_input():
    hub_letter = prompt_for_hub_letter()
    outer_letters = prompt_for_outer_letters()
    solution = get_solution(hub_letter, outer_letters)
    print(solution)

def prompt_for_hub_letter():
    hub_letter = input('Please enter the hub letter: ')

    if len(hub_letter) != 1:
        print(f'Invalid input: Hub letter must be 1 letter, {len(hub_letter)} provided.')
        return prompt_for_hub_letter()

    return hub_letter

def prompt_for_outer_letters():
    outer_letters = input('Please enter the outer letters (enter as a single string e.g. "abcdefgh"): ')

    if len(outer_letters) != 8:
        print(f'Invalid input: 8 outer letters are required, {len(outer_letters)} provided.')
        return prompt_for_outer_letters()

    return outer_letters