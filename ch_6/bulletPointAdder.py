#! pythoun3
#
# Program to take multiple lines of text on the clipboard and 
# prepend an asterisk to each line so that they are a bulleted
# list in WIki markdown.

import pyperclip

text = pyperclip.paste()

lines = text.split("\n")
for i in range(len(lines)):
	lines[i] = "* " + lines[i]

text = "\n".join(lines)

pyperclip.copy(text)