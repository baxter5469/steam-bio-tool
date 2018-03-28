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
    headerin = input("Enter what text you would like to be Header: ")
    print("Copy this into your steam bio or info box: " + "[h1]" + headerin + "[/h1]")
if tool == "bold":
    boldin = input("Enter what text you would like to be Bold: ")
    print("Copy this into your steam bio or info box: " + "[b]" + boldin + "[/b]")
if tool == "underline":
    underin = input("Enter what text you would like to be Underlined: ")
if tool == "italic":
    italicin = input("Enter what text you would like to be Italic: ")
if tool == "strike":
    strikein = input("Enter what text you would like to be Striked: ")
if tool == "spoiler":
    spoilerin = input("Enter what text you would like to have Spoiler: ")
if tool == "url":
    urlin = input("Enter the url you would like to be linked: ")
    urlname = input("Enter the name you would like the URL to be linked as: ")