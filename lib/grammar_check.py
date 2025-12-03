def grammar_check(text):
    if text[0].islower():
        return False 
    elif text[-1] == ".":
        return True
    elif text[-1] == "?":
        return True
    elif text[-1] == "!":
        return True
    else: 
        return False



