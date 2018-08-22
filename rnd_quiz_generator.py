#! python3
# rnd_quiz_generator.py - Creates quizzes with questions and answers in random order, along with the answer key.

import random

# The quiz email_data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
capitals_items = list(capitals.items())

# Generate 35 quiz files.
for quiz_num in range(35):
    # Create the quiz and answer key files.
    quiz_file = open(f'capitalsquiz{quiz_num + 1}.txt', 'w')
    answer_key_file = open(f'capitalsquiz_answers{quiz_num + 1}.txt', 'w')

    # Write out the header for the quiz.
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + f'State Capitals Quiz (Form {quiz_num + 1})')
    quiz_file.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys())  # get all STATES in a list (STATES are KEYS: CAPITALS are VALUES)
    random.shuffle(states)  # randomize the order of the states

    # Loop through all 50 states, making a question for each.
    for question_num in range(50):

        # Get right and wrong answers.
        correct_answer = capitals[states[question_num]]  # for ex. capitals['Georgia'] results in 'Atlanta', 1
        wrong_answers = list(capitals.values())  # get a complete list of answers (list of capitals), 50
        del wrong_answers[wrong_answers.index(correct_answer)]  # remove the right answer (for ex. index 'Atlanta'), 50
        wrong_answers = random.sample(wrong_answers, 3)  # pick 3 random ones from 49 wrong ones, 49

        answer_options = wrong_answers + [correct_answer]  # 3 random wrong capitals + 1 right one
        random.shuffle(answer_options)  # randomize the order of the answers, so the right answer is not always D!!!

        # Write the question and answer options to the quiz file. '\n' is always necesarry in .write() for a new line
        quiz_file.write(f'{question_num + 1}. What is the capital of {states[question_num]}?\n')
        for i in range(4):  # goes throw integers 0 to 3 (0, 1, 2, 3) therefore 4x
            quiz_file.write(f'    {"ABCD"[i]}. {answer_options[i]}\n')  # 0 = A, 1 = B, 2 = C, 3 = D this is "array".
        quiz_file.write('\n')

        # Write out the answer key to a file.
        answer_key_file.write(f'{question_num + 1}. {"ABCD"[answer_options.index(correct_answer)]}\n')
        # another array, correct answer is for ex. 'Atlanta' and its index is for ex. 2 (from 0 to 3), then
        # answer_options.index('Atlanta') = 2
        # 2 = C
    quiz_file.close()
    answer_key_file.close()


# There is a cool way to cut arrays in python: for [1, 2, 3, 4, 5, 6, 7, 8, 9][1:-2] result is [2, 3, 4, 5, 6, 7].
