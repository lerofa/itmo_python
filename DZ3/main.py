

string = "Python is the best programming language in the world"
print(string[6:-7])

string = "Guido van Rossum is the benevolent dictator for life"
print(string[2::3])

string = "You have a problem with authority, Mr. Anderson."
uniq_chars = set(string)

d = dict(zip(uniq_chars, map(string.count, uniq_chars)))
print(d)