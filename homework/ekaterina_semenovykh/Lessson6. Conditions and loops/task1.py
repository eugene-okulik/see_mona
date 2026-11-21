text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
result = []
words = text.split()
for word in words:
    if word[-1] in ".,":
        result.append(word[:-1] + 'ing' + word[-1])
    else:
        result.append(word + 'ing')
print(" " .join(result))
