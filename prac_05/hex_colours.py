"""Program will get colour name from user and if in dictionary will return the value"""

# For ease of use, I have removed the number from the colour name
HEX_COLOUR_DICT = {"aquamarine": "#458b74",
                   "brown": "#ee3b3b",
                   "cadetblue": "#5f9ea0",
                   "cornsilk": "#cdc8b1",
                   "firebrick": "#b22222",
                   "gainsboro": "#dcdcdc",
                   "khaki": "#f0e68c",
                   "lavender": "#e6e6fa",
                   "maroon": "#b03060",
                   "orchid": "#da70d6"}

colour_name = input("Enter colour name: ")
while colour_name != "":
    try:
        print("{} - {}".format(colour_name, HEX_COLOUR_DICT[colour_name.lower()]))
    except KeyError:
        print("No {} in dictionary!".format(colour_name))
    colour_name = input("Enter colour name: ")
print("Farewell!")
