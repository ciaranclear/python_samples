import re

randStr = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr. Smith
Ms Davis
Mrs. Robinson
Mr. T
"""

sentence = "Start a sentence and bring it to an end"

# a raw string begins with r and does not hide escape characters

pattern = re.compile(r'\d\d\d')
matches = pattern.finditer(randStr)
for match in matches:
	print(match)

