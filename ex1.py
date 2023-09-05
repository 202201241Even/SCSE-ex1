def replace_word(word, text):
    count = 0
    replaced_text = ""
    for word_in_text in text.split():
        if word_in_text.strip(".,!?") == word:
            count += 1
            if count % 2 == 0:
                replaced_text += "pathetic "
            else:
                replaced_text += "marvellous "
        else:
            replaced_text += word_in_text + " "
    return replaced_text.strip()

with open("file_to_read.txt", "r") as file:
    text = file.read()

total_count = text.count("terrible")
replaced_text = replace_word("terrible", text)

with open("result.txt", "w") as file:
    file.write(replaced_text)

print(f"The number of occurrences of the word--terrible is: {total_count}")
