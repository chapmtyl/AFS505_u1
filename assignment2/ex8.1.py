formatter = "{} {} {} {}" # this defines formatter

print(formatter.format(1, 2, 3, 4)) # this prints formatter with the values in format
print(formatter.format("one", "two", "three", "four")) # this prints formatter with the values in format
print(formatter.format(True, False, False, True)) # this prints formatter with the values in format
print(formatter.format(formatter, formatter, formatter, formatter)) # this prints formatter with the values in format
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
)) # this prints formatter with the values in format
