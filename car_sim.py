#! Python 3.6

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}


def switch_lights(stoplight):  # The name of the dictionary 'market_2nd' changes to 'stoplight' here.
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
    # Check if there is 'red' in values in the the dictionary 'stoplight' and print out the dictionary. FAILS.


switch_lights(market_2nd)

# Assertions are for development, not the final product.
# Assertions can be disabled by passing the -O option when running Python.

