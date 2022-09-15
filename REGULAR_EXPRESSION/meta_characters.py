import re
# All Meta characters are : . ^ $ * + ? {} [] \ | ()
# . Any character (Except newline character)
# ^ Start  with "^hello"
# $ Ends with "world$"
# * Zero or more occurence "aix*"
# + one or more occurence "aix+"
# {} Exactly the specified number of occurence "al{2}"
# [] A set of characters "[a-m]"
# \ Special sequence ( or escape special characters) "\d"
# | Either or false | stays
# () Capture and group
test_strings = "123abc456789abc1234ABC"
pattern = re.compile(r'\D{3}')
matches = pattern.finditer(test_strings)
for match in matches:
    print(match)

# More special characters
# \d : Matches any decimal digits (0-9)
# \D : Matches any non decimal characters
# \s : Matches any whitespace character; (space " " tab \t newline "\n")
# \S : Matches any non whitespace characers
# \w : Matches any alphanumeric (word) character; [a-zA-Z0-9]
# \W : Matches any non alphanumeric character;
# \b : Matches were the specified characters are at the begninning or at the end of a word
# \B : Matches were the specified characters are present, but NOT at the beginning or at the end of word

test_strings = "123abc456789abc1234ABC"
pattern = re.compile(r'\d')
matches = pattern.finditer(test_strings)
for match in matches:
    print(match)

