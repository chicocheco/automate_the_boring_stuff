import threading

# Correct way of passing arguments to the print function in the new thread:
thread_obj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
thread_obj.start()

# This is incorrect:
# thread_obj = threading.Thread(target=print('Cats', 'Dogs', 'Frogs', sep=' & '))

"""
It is calling the print() function and passing its return value (print()’s return value is always None)
as the target keyword argument.

WARNING!!!! To avoid concurrency issues, never let multiple threads read or write the same variables.
When you create a new Thread object, make sure its target function uses ONLY LOCAL variables in that function.
This will avoid hard-to-debug concurrency issues in your programs.
"""

