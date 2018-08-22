#! python3
# pyautogui_form_filler.py - Automatically fills in the form.

import pyautogui
import time

form_data = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4,
              'comments': 'Tell Bob I said hi.'},
             {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
              'comments': 'n/a'},
             {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1,
              'comments': 'Please take the puppets out of the break room.'},
             {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5,
              'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
             ]

pyautogui.PAUSE = 0.5

# Set these to the correct coordinates for your computer.
name_field = (384, 313)
background = (1134, 613)  # Random point in the background.
background_color = (232, 238, 247)  # Random point in the background.
submit_another_link = (483, 215)

for person in form_data:
    # Give the user a chance to kill the script.
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)

    # Wait until the form page has loaded.
    while not pyautogui.pixelMatchesColor(background[0], background[1], background_color):
        time.sleep(0.5)

    print(f'Entering {person["name"]} info...')
    pyautogui.click(name_field[0], name_field[1])

    # Fill out the Name field.
    pyautogui.typewrite(person['name'] + '\t')

    # Fill out the Greatest Fear(s) field.
    pyautogui.typewrite(person['fear'] + '\t')

    # Fill out the Source of Wizard Powers field.
    if person['source'] == 'wand':
        pyautogui.typewrite(['down', '\t'])
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', '\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', '\t'])
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])

    # Fill out the Robocop field.
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])  # Simulates the spacebar.
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])

    # Fill out the Additional Comments field.
    pyautogui.typewrite(person['comments'] + '\t')

    # Click Submit.
    pyautogui.press('enter')

    # Wait until form page has loaded.
    print('Clicked Submit.')
    time.sleep(5)

    # Click the Submit another response link.
    pyautogui.click(submit_another_link[0], submit_another_link[1])
