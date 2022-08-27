"""
    A spam comment a text containing these keywords.
    "Make a lot of money", "buy now", "click this", "subscribe this"
    Write a program to detect those spams
"""

import sys
spam_word = ["buy now", "click this", "subscribe this"]
email = input("Enter your sentence:")


for word in spam_word:
    if word in email:
        print("spam present")
    
