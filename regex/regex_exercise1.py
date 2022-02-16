import regex as re


text = """
01 624 2944
01-624-2945
086 356 3646
+353 1 624 2944
+44 2 463 3456
this is a wrap around phone number 087 356
3646
my phone number is 83 836 7793
not a phone number 03884 887272 99387482 71787229 words

name: Ciaran Clear age: 41 job: none
name: Billy Connolly age: 70 job: comedian
"""


if __name__ == "__main__":

    print("PHONE NUMBERS")
    pat = r'(?<=[^\d- ])([\d-+ ]{6,16})[^\d -+]'
    matches = re.finditer(pat, text)

    for match in matches:
        num = match.group().strip()
        end = re.findall(r'\d{4}$', num)
        if len(num) <= 16 and end:
            print(num)

    print("\nNAMES AGES JOBS")
    pat = r'(?m)name:(?P<name>[a-zA-Z ]*)age:(?P<age>[0-9 ]*)job:(?P<job>[a-zA-Z ]*)'

    matches = re.finditer(pat, text)

    for match in matches:
        print(f"Name: {match.group('name').strip()}")
        print(f"Age: {match.group('age').strip()}")
        print(f"Job: {match.group('job').strip()}")
        print()
