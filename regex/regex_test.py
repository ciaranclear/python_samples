import re

"""
[ ]		Match what is in the brackets
[^ ]	Match anything not in the brackets
( )		Return surrounded submatch
.		Match any 1 characcter or space
+		Match 1 or more of what preceeds
?		Match 0 or 1
*		Match 0 or more
*?		Lazy match the smallest match
\b 		Word boundary
\B 		Not a word boundary
^		Beggining of a string
$		End of string
\n 		Newline
\d 		Any 1 number
\D 		Anything but a number
\w 		Same as [a-zA-Z0-9_]
\W 		Same as [^a-zA-Z0-9_]
\s 		Same as [\f\n\r\t\v]
\S 		Same as [^\f\n\r\t\v]
{5}		Match 5 of what preceeds the curly brackets
{5,7}	Match 5 to 7 in length of what preceeds
{$m}	Allow ^ on multiline string
"""

"""
finditer() returns re objects with info such as span, start and end.
findall() returns a list with the strings of matches of the groups
          and not the entire string.
          If there are no groups defined it will return all of the
          matches in a list of strings.
match()   returns the first match or None and only returns a match
          at the beggining of a string.
search()  search is like match but will search the entire string.

flags	  re.compile(r'start', re.IGNORECASE)
		  re.compile(r'start', re.I)	shorthand for above IGNORECASE
"""

randStr = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

Meta Characters (Need to be escaped)
    . [ ] { } ( ) \\ ^ $ | ? * +

coreyms.com

321-555-1234
123.555.1234
123*555*1234
800-555-1234
700-555-1234

Mr. Schafer
Mr. Smith
Ms Davis
Mrs. Robinson
Mr. T

bat
mat
cat
sat

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

https://www.google.com
http://coreyms.com
http://youtube.com
https://www.nasa.gov
"""

sentence = "Start a sentence and bring it to an end"

def p(pattern, string):
    matches = pattern.finditer(string)
    for match in matches:
        print(match)

if __name__ == "__main__":

    print(randStr)

    print("\n## Find 'abc' in randStr ##")

    pat = re.compile(r"abc")
    p(pat, randStr)

    print("\n## '.' will match everything ##")
    pat = re.compile(r'.')
    p(pat, randStr)

    print("\n## '\\.' will match the '.' character ##")
    pat = re.compile(r'\.')
    p(pat, randStr)

    print("\n## Find 'coreyms.com' ##")
    pat = re.compile(r'coreyms\.com')
    p(pat, randStr)

    print("\n## '\\w' will match all word charaters (a-z,A-Z,0-9,_) ##")
    pat = re.compile(r'\w')
    p(pat, randStr)

    print("\n## '\\W' will match all non word characters including escaped characters ##")
    pat = re.compile(r'\W')
    p(pat, randStr)

    print("\n## '\\s' will match all whitespace (space, tab, newline) ##")
    pat = re.compile(r'\s')
    p(pat, randStr)

    print("\n## '\\S' will match all non whitespace characters ##")
    pat = re.compile(r'\S')
    p(pat, randStr)

    print("\n## '\\bHa' finds both matches of Ha in randStr ##")
    pat = re.compile(r'\bHa')
    p(pat, randStr)

    print("\n## '\\BHa' finds one match of Ha in randStr ##")
    pat = re.compile(r'\BHa')
    p(pat, randStr)

    print("\n## '^Start' finds 'Start' in sentence ##")
    pat = re.compile(r'^Start')
    p(pat, sentence)

    print("\n## 'end$' finds 'end' in sentence ##")
    pat = re.compile(r'end$')
    p(pat, sentence)

    print("\n## '\\d\\d\\d' finds non overlapping groups of 3 digits ##")
    pat = re.compile(r'\d\d\d')
    p(pat, randStr)

    print("\n## '\\d\\d\\d.\\d\\d\\d.\\d\\d\\d\\d' finds groups of phone numbers ##")
    pat = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
    p(pat, randStr)

    print("\n## '\\d\\d\\d[-.]\\d\\d\\d[-.]\\d\\d\\d\\d' finds phone numbers seperated by '-' or '.' ##")
    pat = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
    p(pat, randStr)

    print("\n## '[89]00[-.]\\d\\d\\d[-.]\\d\\d\\d\\d' finds phone numbers starting with 800 or 900 ##")
    pat = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
    p(pat, randStr)

    print("\n## '[1-5]' finds digits between 1 to 5 ##")
    pat = re.compile(r'[1-5]')
    p(pat, randStr)

    print("\n## '[a-z]' finds characters between a to z lowercase ##")
    pat = re.compile(r'[a-z]')
    p(pat, randStr)

    print("\n## '[a-zA-Z]' finds characters between a to z and A to Z ##")
    pat = re.compile(r'[a-zA-Z]')
    p(pat, randStr)

    print("\n## '[^a-zA-Z]' negates upper and lowercase characters finds everything else ##")
    pat = re.compile(r'[^a-zA-Z]')
    p(pat, randStr)

    print("\n## '[^b]at' finds words ending in 'at' but not beginning with 'b' ##")
    pat = re.compile(r'[^b]at')
    p(pat, randStr)

    print("\n## 'Mr\\.?' finds all 'Mr' or 'Mr.' as '?' finds 0 or 1 '.' ##")
    pat = re.compile(r'Mr\.?')
    p(pat, randStr)

    print("\n## 'Mr\\.?\\s[A-Z]' finds 'Mr' or 'Mr.' followed by a space followd by first uppercase char of name ##")
    pat = re.compile(r'Mr\.?\s[A-Z]')
    p(pat, randStr)

    print("\n## 'Mr\\.?\\s[A-Z]\\w+' finds 'Mr' or 'Mr.' followed by a space followed by any number of word characters ##")
    pat = re.compile(r'Mr\.?\s[A-Z]\w+')
    p(pat, randStr)

    print("\n## 'Mr\\.?\\s[A-Z]\\w*' finds 'Mr' or 'Mr.' followed by a space followed by zero or more word characters ##")
    pat = re.compile(r'Mr\.?\s[A-Z]\w*')
    p(pat, randStr)

    print("\n## 'M(r|s|rs)\\.?\\s[A-Z]\\w*' finds all names beggining with 'Mr' 'Mr.' 'Ms' 'Ms.' 'Mrs' 'Mrs.' ##")
    pat = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
    p(pat, randStr)

    print("\n## '[a-zA-Z]+@[a-zA-Z]+\\.com' finds 'CoreyMSchafer@gmail.com' ##")
    pat = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')
    p(pat, randStr)

    print("\n## '[a-zA-Z]+@[a-zA-Z]+\\.(com|edu)' finds 'CoreyMSchafer@gmail.com' 'corey.schafer@university.edu' ##")
    pat = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.(com|edu)')
    p(pat, randStr)

    print("\n## '[a-zA-Z0-9.-]+@[a-zA-Z-]+\\.(com|edu|net)' finds CoreyMSchafer@gmail.com' 'corey.schafer@university.edu' 'corey-321-schafer@my-work.net' ##")
    pat = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
    p(pat, randStr)

    print("\n## '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+' should find any email address ##")
    pat = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    p(pat, randStr)

    print("\n## 'https?://(www\\.)?(\\w+)(\\.\\w+)' should find all urls")
    pat = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
    p(pat, randStr)

    print("\n## get the sub url names ##")
    pat = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
    subbed_urls = pat.sub(r'\2\3', randStr)
    print(subbed_urls)

    plugStr1 = "AB,CD,EF,GH,IJ,KL,MN,OP,QR,ST,UV,WX,YZ"
    plugStr2 = "AB, CD, EF, GH, IJ, KL, MN, OP, QR, ST, UV, WX, YZ"
    plugStr3 = "A B,CD , EF,gh,IJ,KL,MN,OP,QR,ST  ,UV,WX;YZ"
    #pat = re.compile(r'([a-zA-Z]*){2}\s*,')
    pat = re.compile(r'([a-zA-Z])\s*([a-zA-Z])\s*')
    print(plugStr1)
    p(pat, plugStr1)
    print(plugStr2)
    p(pat, plugStr2)
    print(plugStr3)
    p(pat, plugStr3)
    
    match_list = []
    cleaned = []
    matches = pat.finditer(plugStr3)
    for match in matches:
        print(match.group())
        match_list.append(match.group())

    pat = re.compile(r'[a-zA-Z]')
    for match in match_list:
        clean = re.findall(pat, match)
        print(clean)
        cleaned.append(clean)
    print(cleaned)
    
    uhrStr1 = "A 01A, B 02A, C 03A, D 04A, E 05A, F 06A, G 07A, H 08A, I 09A, J 10A, K 01B, L 02B, M 03B, N 04B, O 05B, P 06B, Q 07B, R 08B, S 09B, T 10B"
    uhrStr2 = "A01A, B02A, C03A, D04A, E05A, F06A, G07A, H08A, I09A, J10A, K01B, L02B, M03B, N04B, O05B, P06B, Q07B, R08B, S09B, T10B"
    uhrStr3 = "01AA, 02AB, 03AC, 04AD, 05AE, 06AF, 07AG, 08AH, 09AI, 10AJ, 01BK, 02BL, 03BM, 04BN, 05BO, 06BP, 07BQ, 08BR, 09BS, 10BT"
    uhrStr4 = "A 1A, B 2A, C 3A, D 4A, E 5A, F 6A, G 7A, H 8A, I 9A, J 10A, K 1B, L 2B, M 3B, N 4B, O 5B, P 6B, Q 7B, R 8B, S 9B, T 10B"
    uhrStr5 = "A1A, B2A, C3A, D4A, E5A, F6A, G7A, H8A, I9A, J10A, K1B, L2B, M3B, N4B, O5B, P6B, Q7B, R8B, S9B, T10B"
    uhrStr6 = "1AA, 2AB, 3AC, 4AD, 5AE, 6AF, 7AG, 8AH, 9AI, 10AJ, 1BK, 2BL, 3BM, 4BN, 5BO, 6BP, 7BQ, 8BR, 9BS, 10BT"
    pat = re.compile(r'[a-zA-Z]\s*\d+[a-zA-Z]\s*')

    match_list = []
    cleaned = []
    matches = pat.finditer(uhrStr5)
    for match in matches:
        print(match)
        match_list.append(match.group())

    pat = re.compile(r'([a-zA-Z])\s*(\d+[a-zA-Z])')
    for match in match_list:
        clean = [pat.sub(r'\1',match),pat.sub(r'\2',match)]
        print(clean)
        cleaned.append(clean)
    print(cleaned)

    letlist = []
    lets = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y"
    pat = re.compile(r'([a-zA-Z])*[\s,;]')
    subbed = pat.sub(r'\1', lets)
    matches = pat.finditer(lets)
    for match in matches:
        print(match)
        print(match.span())
        print(help(match))
        letlist.append(match.group())
    print(letlist)
    print(subbed)