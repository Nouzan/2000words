import re
import shelve

pattern = re.compile(r'[a-zA-Z]+')

file = open('./pdf/text.txt', 'r')
data_file = shelve.open('data')
word_dict = {}

for line in file.readlines():
    words = pattern.findall(line)
    for word in words:
        word_real = word.lower()
        if len(word_real) > 3:
            word_dict[word_real] = word_dict.get(word_real, 0) + 1

word_list = []

for k, v in word_dict.items():
    word_list.append((v, k))

word_list.sort()

for v, k in word_list[:10]:
    print(k, v)

data_file['word_dict'] = word_dict
data_file['word_list'] = word_list
data_file.close()
