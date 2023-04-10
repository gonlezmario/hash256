import getpass
import hashlib

repeat = True

while repeat == True:
    input_string = getpass.getpass("String to hash:")
    hash = hashlib.sha256(str.encode(input_string)).hexdigest()
    print(hash)

    length_input = getpass.getpass(
        "Enter an integer if you want to cut your hash:")
    if length_input.isdigit():
        print(hash[0:int(length_input)])

    answer = getpass.getpass("Repeat procedure (Y/N)?")

    if answer not in {"Y", "y"}:
        repeat = False
