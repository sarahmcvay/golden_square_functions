
def reading_time(my_string):
    if my_string == "":
        raise Exception("There is no text to read.")
    elif len(my_string.split()) < 200:
        return "This string takes less than 1 minute to read"
    elif len(my_string.split()) > 200:
        minutes = len(my_string.split()) / 200
        return f"This string takes {int(minutes)} minutes to read"
