string = input()

while "ZZZZ" in string:
    string = string.replace("RRR", "Z", 1)
    string = string.replace("ZZZZ", "R", 1)

while string.find("ZZZZ") != -1:
    string = string.replace("RRR", "Z", 1)
    string = string.replace("ZZZZ", "R", 1)

while string.count("ZZZZ") != 0:
    string = string.replace("RRR", "Z", 1)
    string = string.replace("ZZZZ", "R", 1)

print(string)
