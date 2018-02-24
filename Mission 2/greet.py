def greet(name, language):
    # fill in your code here
    # return the string at the end, do not print it!
    if language == 'English':
        return "Nice to meet you", name
    elif language == 'Klingon':
        return "nuqueH" + name
    elif language == 'Elvish':
        return 'Gi suilon' + name

print(greet('Bob', 'English'))
