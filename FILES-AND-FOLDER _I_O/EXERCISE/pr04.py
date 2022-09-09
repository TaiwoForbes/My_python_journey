""" A file contains a word "Donkey" multiple times. You need to write a program
    which replaces this word with ##### by updating the same file
"""
with open("word_donkey.txt" , "r") as f:
    word = f.read()
    if 'Donkey' in word:
        text = word.replace('Donkey' , "#####")
        with open('word_donkey.txt', 'w') as f:
            f.write(text)



