''' Steam Bio Tool By Andrew Ault
3/27/18
Easily and quickly format your Steam Bio and info box!
'''
tool = 0
checkinput = True
print("Welcome to the Steam Bio Tool v0.1")
input()
print("Press 'Enter' after each line of text appears to read the directions")
input()
print("Options for formatting: Header, Bold, Underline, Italic, Strike, Spoiler, URL")
input()
while checkinput:
    tool = input(str("Enter Which format tool you would like to use:")).lower()
    if tool == "header" or tool == "bold" or tool == "underline" or tool == "italic" or tool == "strike" or tool == "spoiler" or tool == "url":
        checkinput = False
checkinput = True
if tool == "header":
    print("works :D")
if tool == "bold":
    print("confirmed")
if tool == "underline":
    print("confirmed")
if tool == "italic":
    print("confirmed")
if tool == "strike":
    print("confirmed")
if tool == "spoiler":
    print("confirmed")
if tool == "url":
    print("confirmed")
