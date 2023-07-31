import re
# Compilation Flags:
# ASCII, A : Makes several escapes like \w, \b, \s nad \d match only on ASCII characters
# DOTALL, S : Makes . matches all character, including newlines
# IGNORECASE, I : Do case-insensitive matches.
# LOCALE, L : Do a locale-aware match. 
# MULTILINE, M : Multi-line matching, affecting ^ and $
# VERBOSE, X (for "extended") : Enable verbose REs, which can be organized more cleanly and understandably

my_string = "Hello world"
pattern = re.compile(r"World", re.I) # Note : I is abbreviated for IGNORECASE
matches = pattern.finditer(my_string)

for match in matches:
    print(match)
