
import re

# re.search returns True or False
if re.search("ape", "The ape was at the apex"):
    print("There is an ape")

# re.findall returns all the matches even matches within words

allApes = re.findall("ape", "The ape was at the apex")

for i in allApes:
    # prints ape and ape in apex
    print(i)

# period . after the search string allows the match to include
# any character after the search string

allApes = re.findall("ape.", "The ape was at the apex")

for i in allApes:
    # prints ape and apex
    print(i)

theStr = "The ape was at the apex"

# re.finditer returns an iterator of matching objects
for i in re.finditer("ape.", theStr):

    # span() returns a tuple with the string indexes were the
    # pattern matches. span() is a finditer method
    locTuple = i.span()

    print(locTuple)

    print(theStr[locTuple[0]:locTuple[1]])

# [] can be used for submatches within a pattern

animalStr = "Cat rat mat pat"

allAnimals = re.findall("[crmfp]at", animalStr)

for i in allAnimals:
    print(i)

# [c-mC-M]at matches anything beginning with letters c -> m
# or letter C -> M and ending in at
someAnimals = re.findall("[c-mC-M]at", animalStr)

for i in someAnimals:
    print(i)

# ^ means find any match NOT beggining with C or r

someAnimals = re.findall("[^Cr]at", animalStr)

for i in someAnimals:
    print(i)

# replaces anything in owlFood that an owl can eat

owlFood = "rat cat mat pat"

regex = re.compile("[cr]at")

owlFood = regex.sub("owl", owlFood)

print(owlFood)


# Demonstrates how \ backslashes are treated specialy in regex

randStr = "Here is \\stuff"

# prints Find \stuff : None
# \\ escapes a backslash
print("Find \\stuff :", re.search("\\stuff", randStr))

# will match as \\\\ escapes 2 backslashes
print("Find \\stuff :", re.search("\\\\stuff", randStr))

# r in front of the search string denotes a raw string
# \ are treated like other characters in a raw string and
# do not have to be escaped
print("Find \\stuff :", re.search(r"\\stuff", randStr))


#

randStr = "F.B.I. I.R.S. CIA"

# prints the number of matches found
# \. escapes the period .
# . repressents anything
print("Matches :", len(re.findall(".\..\..\.", randStr)))

# Demonstrates how to remove new lines and replace them with spaces

randStr = """This is a long
string that goes
on for many lines
"""

print(randStr)

regex = re.compile("\n")

randStr = regex.sub(" ", randStr)

print(randStr)

# \b : Backspace
# \f : Form Feed
# \r : Carriage Return
# \t : Tab
# \v : Vertical Tab

# windows amy use \r\n instead of \n

# Demonstrates matching numbers

# \d : [0-9]
# \D : [^0-9]

randStr = "12345"

# Gets 5 matches
print("Matches :", len(re.findall("\d", randStr)))

# Gets 2 matches "12" and "34"
# \d{2} is looking to match 2 digits
print("Matches :", len(re.findall("\d{2}", randStr)))

# Gets 1 match
print("Matches :", len(re.findall("\d{5}", randStr)))

numStr = "123 12345 123456 1234567"

# Gets 3 matches for numbers between 5 and 7 digits long
print("Matches :", len(re.findall("\d{5,7}", numStr)))

# \w : [a-zA-Z0-9_]
# \W : [^a-zA-Z0-9_]

phNum = "412-555-1212"

if re.search("\w{3}-\w{3}-\w{4}", phNum):
    print("It is a phone number")

# Gets any set of characters that are 2 to 20 characters long
if re.search("\w{2,20}", "Ultraman"):
    print("Is a valid name")

# \s : [\f\n\r\t\v]
# \S : [^\f\n\r\t\v]

# Gets any 2 sets of characters between 2 and 20 characters in Length
# that are seperated with a space
if re.search("\w{2,20}\s\w{2,20}", "Toshia Muramatsu"):
    print("It is valid")

# + matches 1 or more characters
print("Matches :", len(re.findall("a+", "a as ape bug")))


# 1. 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
# 2. An @ symbol
# 3. 2 to 20 lowercase and uppercase letters, numbers, plus .-
# 4. A period
# 5. 2 to 3 lowercase and uppercase letters

emailList = "db@aol.com m@.com @apple.com dbe@.com eat@email.com"

print("Email Matches :", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", emailList)))


import re

# If re.search("REGEX", yourString)

# print("Matches :", len(re.findall("REGEX", yourString)))

# regex = re.compile("REGEX")

# yourString = regex.sub("substitution", yourString)

# []    : Match what is in the brackets
# [^ ]  : Match anything not in the brackets
# .     : Match any 1 character or space
# +     : Match 1 or more of what proceeds it
# ?     : Match 0 or 1 of what preceeds it
# *     : Match 0 or more of what preceeds it
# \n    : Newline
# \d    : Any 1 number
# \D    : Anything but a number
# \w    : Same as [a-zA-Z0-9_]
# \W    : Same as [^a-zA-Z0-9_]
# \s    : Same as [\f\n\r\t\v]
# \S    : Same as [^\f\n\r\t\v]
# {5}   : Match 5 of what preceeds the curly brackets
# {5,7} : Match values that are between 5 and 7 in length
# ^     : Beginning of the string
# $     : End of the string

randStr = "cat cats"

# Matches cat + 1 or more of whats inside the [] brackets ie "cat"
# The ? looks to match 0 or 1 of what preceeds it ie an s character
regex = re.compile("[cat]+s?")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)

#

randStr = "doctor doctors doctor's"

# re.compile("[doctor]+['s]*") will also work
# if a letter is repeated twice in a string it does not have to be repeated
# twice in a [string]
regex = re.compile("[doctr]+['s]*")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)

# Match any characters and spaces accross newlines

randStr = """Just some words
and some more\r
and more
"""

# Match 1 or more [chars spaces] and 0 or 1 [\r] and \n
regex = re.compile("[\w\s]+[\r]?\n")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)

# Greedy and lazy matching

# Greedy match

randStr = "<name>Life on Mars</name><name>Freaks and Geeks</name>"

# Match everything including the tags
# the * is greedy and grabs the biggest match
regex = re.compile("<name>.*</name>")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)

# Lazy match

randStr = "<name>Life on Mars</name><name>Freaks and Geeks</name>"

# Match everything including the tags
# the ? makes the * lazy and grabs the first match
regex = re.compile("<name>.*?</name>")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)

# Sub expressions

randStr = "<name>Life on Mars</name><name>Freaks and Geeks</name>"

# Sub matches everything between the tags
regex = re.compile("<name>(.*?)</name>")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)

# Demonstrates word boundary \b operator

randStr = "ape at the apex"

# Matches word ape only and not start of apex
regex = re.compile(r"\bape\b")

matches = re.findall(regex, randStr)

print(len(matches))

for i in matches:
    print(i)

# Demonstrates string boundaries

# Start of string

randStr = "Match everything up to @"

# Matches everything up to the @ symbol
# The start of the string ^ followed by any number of characters .*
# Up to anything but the @ symbol [^@]
regex = re.compile(r"^.*[^@]")

matches = re.findall(regex, randStr)

print(len(matches))

for i in matches:
    print(i)

# End of string

randStr = "@ Get this string"

# Matches everthing after the @ and a space
# Ignore the @ and a space [^@\s] and get every character .* up
# to the end of the string $
regex = re.compile(r"[^@\s].*$")

matches = re.findall(regex, randStr)

print(len(matches))

for i in matches:
    print(i)

#

randStr = """Ape is big
Turtle is slow
Cheetah is fast
"""

# Matches first word on each line
# (?m) targets each line
# The start of the string ^
# Any number of characters .*
# First match or lazy match ?
# Up to a space
regex = re.compile(r"(?m)^.*?\s")

matches = re.findall(regex, randStr)

print(len(matches))

for i in matches:
    print(i)

# Demonstrates Submatches

randStr = "My number is 412-55555-1212"

# Matches a submatch within a bigger match
regex = re.compile(r"412-(.*)")

matches = re.findall(regex, randStr)

print(len(matches))

for i in matches:
    print(i)

# Demonstrates multiple submatches

randStr = "412-555-1212 412-555-1213 412-555-1214"

# Matches the submatch starting with 412- and contains a submatch that
# has 8 characters
regex = re.compile(r"412-(.{8})")

matches = re.findall(regex, randStr)

print(len(matches))

for i in matches:
    print(i)

#

randStr = "My number is 412-555-1212"

# Matches word ape only and not start of apex
regex = re.compile(r"412-(.*)-(.*)")

matches = re.findall(regex, randStr)

print(len(matches))

print(matches[0][0])
print(matches[0][1])


import re

randStr = "the cat cat fell out the window"

# Submatches a word where that word is preceeded by the same word
# Matches a word boundary \b followed by 1 or more letters or numbers \w+
# The submatch is followed by 1 or more spaces
# The back reference \1 is to look for the same that preceeds it
regex = re.compile(r"(\b\w+)\s+\1")

matches = re.findall(regex, randStr)

print("Matches :", len(matches))

for i in matches:
    print(i)

# Demonstrates back reference

randStr = "<a href='&'><b>The Link</b></a>"

# Submatches everything between the bold tags
regex = re.compile(r"<b>(.*?)</b>")

randStr = re.sub(regex, r"\1", randStr)

print(randStr)

matches = re.findall(regex, randStr)

print("Matches :", len(matches))

for i in matches:
    print(i)

# Demonstrates multiple back references

randStr = "412-555-1212"

# Gets 2 submatches
regex = re.compile(r"([\d]{3})-([\d]{3}-[\d]{4})")

# substitutes the match with a format composed of the first and second submatch
randStr = re.sub(regex, r"(\1)\2", randStr)

print(randStr)

#

randStr = "https://www.youtube.com http://www.google.com"

# <a href='https://www.youtube.com'>www.youtube.com</a>
# <a href='https://www.google.com'>www.google.com</a>

# Submatches everything between the bold tags
regex = re.compile(r"(https?://([\w.]+))")

randStr = re.sub(regex, r"<a href='\1'>\2</a>\n", randStr)

print(randStr)

# Demonstrates look ahead
# Look ahead looks for a match but does not return it
# (?=expression) does not return what matches the expression

randStr = "One two three four"

# Matches 1 or more letters or numbers up to a word boundary but
# does not return the word boundary
regex = re.compile(r"\w+(?=\b)")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)

# Demonstrates look behind

# (?<=expression)

randStr = "1. Bread 2. Apples 3. Lettuce"

# Matches a word \w+ preceeded with a match for a number a character
# and a space
regex = re.compile(r"(?<=\d.\s)\w+")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)

# Demonstrates look ahead and look behind

randStr = "<h1>I'm Important</h1> <h1>So am I</h1>"

# Matches content between the h1 tags
regex = re.compile(r"(?<=<h1>).+?(?=</h1>)")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)

# Demonstrates negative look ahead and negative look behind

# (?!expression) : Negative Look Ahead
# (?<!expression) : Negative Look Behind

randStr = "8 Apples $3, 1 Bread $1, 1 Cereal $4"

#
regex = re.compile(r"(?<!\$)\d+")

matches = re.findall(regex, randStr)

print(len(matches))

matches = [int(i) for i in matches]

from functools import reduce

print("Total Items {}".format(reduce((lambda x, y: x + y), matches)))


import re

# [ ]   : Match what is in the brackets
# [^ ]  : Match anything not in the brackets
# ( )   : Return surrounded submatch
# .     : Match any 1 character or space
# +     : Match 1 or more of what proceeds
# ?     : Match 0 or 1
# *     : Match 0 or More
# *?    : Lazy match the smallest match
# \b    : Word boundary
# ^     : Beginning of String
# $     : End of String
# \n    : Newline
# \d    : Any 1 number
# \D    : Anything but a number
# \w    : Same as [a-zA-Z0-9_]
# \W    : Same as [^a-zA-Z0-9_]
# \s    : Same as [\f\n\r\t\v]
# \S    : Same as [^\f\n\r\t\v]
# {5}   : Match 5 of what proceeds the curly brackets
# {5,7} : Match values that are between 5 and 7 in length
# ($m)  : Allow ^ on multiline string

# Use a back reference to substitute what is between the
# bold tags and eliminate the bold tags
# re.sub(r"<b>(.*?)</b>", r"\1", randStr)

# Use a look ahead to find all characters of 1 or more
# with a word boundary, but don't return the word
# boundary
# re.findall(r"\w+(?=\b)", randStr)

# Use a look behind to find words starting with a number,
# period and space, but only return the word that follows
# re.findall(r"(?<=\d.\s)\w+", randStr)

# Use a negative look behind to only return numbers without
# a $ in front of them
# re.findall(r"(?<!\$)\d+", randStr)

# ---------- OR CONDITIONAL ----------
# You can use | to define the matches you'll except

randStr = "1. Dog 2. Cat 3. Turtle"

regex = re.compile(r"\d\.\s(Dog|Cat)")

matches = re.findall(regex, randStr)

print(len(matches))

for i in matches:
    print(i)

# ---------- PROBLEM ----------
# Create a regex that will match for 5 digit zip
# codes or zip codes with 5 digits a dash and
# then 4 digits

randStr = "12345 12345-1234 1234 12346-333"

regex = re.compile(r"(\d{5}-\d{4}|\d{5}\s)")

matches = re.findall(regex, randStr)

print(len(matches))

for i in matches:
    print(i)

# ---------- GROUP ----------
# We can use group to retrieve parts of regex
# matches
'''
bd = input("Enter your birthday (mm-dd-yyyy) : ")

bdRegex = re.search(r"(\d{1,2})-(\d{1,2})-(\d{4})", bd)

print("You were born on", bdRegex.group())
print("Birth Month", bdRegex.group(1))
print("Birth Day", bdRegex.group(2))
print("Birth Year", bdRegex.group(3))
'''

# ---------- MATCH OBJECT FUNCTIONS ----------
# There are functions that provide more information
# on your matches

match = re.search(r"\d{2}", "The 26 chickens weighed 13 lbs")

# Print the match
print("Match :", match.group())

# Print the start and ending index of the match
print("Span :", match.span())

# Print starting index of the match
print("Match :", match.start())

# Print the ending index of the match
print("Match :", match.end())

# ---------- NAMED GROUPS ----------
# You can also assign names to matches

randStr = "December 21 1974"

regex = r"^(?P<month>\w+)\s(?P<day>\d+)\s(?P<year>\d+)"

matches = re.search(regex, randStr)

print("Month :", matches.group('month'))
print("Day :", matches.group('day'))
print("Year :", matches.group('year'))

# ---------- PROBLEM ----------
# Find all of the following email addresses

randStr = "d+b@aol.com a_1@yahoo.co.uk A-100@m-b.INTERNATIONAL"

regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

matches = re.findall(regex, randStr)

print(len(matches))

for i in matches:
    print(i)

# ---------- PROBLEM ----------
# Find all of the following phone numbers and then print them

randStr = "14125551212 4125551212 (412)5551212 412 555 1212 412-555-1212 1-412-555-1212"

regex = re.compile(r"((1?)(-| ?)(\()?(\d{3})(\)|-| |\)-|\) )?(\d{3})(-| )?(\d{4}|\d{4}))")

matches = re.findall(regex, randStr)

print(len(matches))

for i in matches:
    print(i[0].lstrip())
