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
    tool = input(str("Enter Which format tool you would like to use:"))
    if tool == "header" or tool == "Header":
        checkinput = False
checkinput = True
if tool == "header" or tool == "Header":
    print("works :D")
    '''if tool == "Bold" or "bold":
        print("confirmed")
    if tool == "Underline" or "underline":
        print("confirmed")
    if tool == "Italic" or "italic":
        print("confirmed")
    if tool == "Strike" or "strike":
        print("confirmed")
    if tool == "Spoiler" or "spoiler":
        print("confirmed")
    if tool == "URL" or "url":
        print("confirmed")
'''