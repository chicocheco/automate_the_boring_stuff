"""
PyCharm:

When a breakpoint is reached or your program is suspended, the Debug tool window becomes active
and enables you to get control over the program's execution.

A breakpoint in PyCharm is added by clicking in the gray area on the from_left (next to numbering of lines).

Run Debugger and click on the pause button.

Use always 'Step Into My Code' command. It helps skip stepping into library sources and keep focused on your own code.

The 'Force Step Into' - enables you to step into a method of a class not to be stepped into.
The classes, stepping into which is suppressed, are specified on the Debugger.
Stepping page of the Settings/Preferences dialog box.
The 'Force Step Over' - enables you to jump over the method call ignoring the breakpoints on the way.
The 'Force Run to Cursor' - enables you to jump to the cursor position ignoring existing breakpoints on the way.
"""


print('Enter the first number to add:')
first = input()
print('Enter the second number to add:')
second = input()
print('Enter the third number to add:')
third = input()
print('The sum is ' + first + second + third)
