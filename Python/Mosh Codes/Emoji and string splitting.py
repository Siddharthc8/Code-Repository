message = input ("›")
words = message.split(' ')   # Split and stored in list/array
emojis = {
    ":)": "😊",      # Ctrl + Cmd + space to bring up emoji
    ":(": "😔"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "    # Default to be the actual word getting in

print(output)