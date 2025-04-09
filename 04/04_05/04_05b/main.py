def has_unique_characters(data):
    chars = set()
    for i in data:
        chars.add(i)
    if len(data) != len(chars):
        return False
    else:
        return True

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
