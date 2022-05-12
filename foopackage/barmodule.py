def stupid_factorial(number):
    if(number <= 1):
        return number
    return stupid_factorial(number - 1) * number

def tool_lyrics(number):
    if(number == 0 or number == 1):
        return number
    return tool_lyrics(number - 1) + tool_lyrics(number - 2)
