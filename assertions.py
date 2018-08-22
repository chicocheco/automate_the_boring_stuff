pod_bay_door_status = 'open'
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'
pod_bay_door_status = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'  # This is what will cause it failed.
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'  # Because here it is not 'open' anymore.


# The assert + A condition (that is, an expression that evaluates to True or False) + A comma +
# A string to display when the condition is False

# “I assert that this condition holds true, and if not, there is a bug somewhere in the program.”
# Unlike exceptions, your code should not handle assert statements with try and except;
# if an assert fails, your program should crash.
