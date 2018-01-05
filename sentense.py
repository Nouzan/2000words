import shelve
import time
import re

pattern = re.compile(r'[a-zA-Z]+')

file = open('./pdf/text.txt', 'r')
data = shelve.open('data')
word_trans_dict = data['word_trans_dict']
word_list = []
sentense_list = []
raw = file.read()
raws = raw.split('.')
raw_sentense_list = []
print(len(raws))
time.sleep(1)
for s in raws:
    s = s.strip()
    s = s.replace('\n', '')
    words = pattern.findall(s)
    tran = None
    trans = None
    for i in range(len(words)):
        # words[i] = words[i].lower()
        if tran is None and words[i].lower() not in word_list:
            tran = word_trans_dict.get(words[i].lower(), None)
            trans = (tran, i)
            word_list.append(words[i].lower())
            break
    if len(s) > 0 and len(words) > 1 and len(s) <= 256:
        if tran is not None:
            tran, index = trans
            d, t = tran
            t = t[0]
            if d is not None or (not pattern.match(t)):
                ts = d
                if d is None:
                    ts = t + '*'
                if not ('名' in ts or '姓' in ts):
                    s = s.replace(words[index], words[index] + '[' + ts + ']')
                    raw_sentense_list.append((s + '.', words))

count = 0
for s, words in raw_sentense_list:
    count += 1
    print('[%s]' % count, s)

data2 = shelve.open('data2')
data2['raw_sentense_list'] = raw_sentense_list
data2.close()
