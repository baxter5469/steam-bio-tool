''' Steam Format Tool By Andrew Ault v1.2
3/27/18
Easily and quickly format your Steam Bio and info box!
'''
import tkinter as tk
tool = 0
checkinput = True
print("Welcome to the Steam Format Tool v1.2")
print("Press 'Enter' after each line of text appears to read the directions")
input()
print("Options for formatting: Header, Bold, Underline, Italic, Strike, Spoiler, URL")
input()
print("If you would like to do multiple formats just go through the program again and copy the first formatted text.")
input()
while checkinput:
    tool = input(str("Enter Which format tool you would like to use:")).lower()
    if tool == "header" or tool == "bold" or tool == "underline" or tool == "italic" or tool == "strike" or tool == "spoiler" or tool == "url":
        checkinput = False
checkinput = True
if tool == "header":
    headerin = input("Enter what text you would like to be Header: ")
    print("Copy this into your steam bio or info box: " + "[h1]" + headerin + "[/h1]")
    input()
if tool == "bold":
    boldin = input("Enter what text you would like to be Bold: ")
    print("Copy this into your steam bio or info box: " + "[b]" + boldin + "[/b]")
    input()
if tool == "underline":
    underin = input("Enter what text you would like to be Underlined: ")
    print("Copy this into your steam bio or info box: " + "[u]" + underin + "[/u]")
    input()
if tool == "italic":
    italicin = input("Enter what text you would like to be Italic: ")
    print("Copy this into your steam bio or info box: " + "[i]" + italicin + "[/i]")
    input()
if tool == "strike":
    strikein = input("Enter what text you would like to be Striked: ")
    print("Copy this into your steam bio or info box: " + "[strike]" + strikein + "[/strike]")
    input()
if tool == "spoiler":
    spoilerin = input("Enter what text you would like to have Spoiler: ")
    print("Copy this into your steam bio or info box: " + "[spoiler]" + spoilerin + "[/spoiler]")
    input()
if tool == "url":
    urlin = input("Enter the url you would like to be linked: ")
    urlname = input("Enter the name you would like the URL to be linked as: ")
    print("Copy this into your steam bio or info box: " + "[url=" + urlin + "]" + urlname + "[/url]")
    input()