import time, shelve
from translate import translate2


def do(start=0, end=1):
    data = shelve.open('data')
    word_list = data['word_list']
    for v, word in word_list[start: end]:
        trans = (None, None)
        try:
            result = translate2(word)
        except Exception:
            result = {}
        if result.get('errorCode', None) == '0':
            trans = (result.get('basic', {}).get(
                'explains', [None])[0],
                result.get('translation', None)
            )
        print(word, trans)
        word_trans_dict[word] = trans
        data['word_trans_dict'] = word_trans_dict
        data.update()
        time.sleep(1)
    data.close()


if __name__ == '__main__':
    begin = 5407
    period = 1000
    while True:
        data = shelve.open('data')
        word_trans_dict = data['word_trans_dict']
        data.close()
        start = len(word_trans_dict) + begin
        print('[START]:', start)
        do(start, start + period)
        flag = input('Continue?(y/n)')
        if flag.lower() == 'n':
            break
