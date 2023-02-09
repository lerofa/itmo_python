import string

file_path = "aristotle.txt"

sym_counter = 0
sym_without_space_counter = 0
sym_without_punctuation_counter = 0
word_counter = 0
sentence_counter = 0

punctuation_translate_table = str.maketrans({char:None for char in string.punctuation})
end_sentence_sym = ".?!"

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        sym_counter += len(line)
        sym_without_space_counter += len(line) - line.count(" ")
        sym_without_punctuation_counter += len(line.translate(punctuation_translate_table))

        word_counter += len(line.split(" "))

        for i in range(len(line)-1):
            if (line[i] not in end_sentence_sym and line[i+1] in end_sentence_sym):
                sentence_counter += 1

print(f"Всего символов: {sym_counter}")
print(f"Всего символов без пробелов: {sym_without_space_counter}")
print(f"Всего символов без знаков пунктуации: {sym_without_punctuation_counter}")
print(f"Всего слов: {word_counter}")
print(f"Всего предложений: {sentence_counter}")

