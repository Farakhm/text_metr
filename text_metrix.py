import re
import numpy as np
from service import index_lett, save_dict, save_file, save_matr
from service import num_freqs

def extract_text_metrix(text):
    # Определяем количество заголовков и параграфов в тексте
    r5 = ['.', '!', '?', ':', '"', ',']
    zagol = 0
    zg = []
    paragr = 0
    prg_sent = []
    sentense = []
    wrd_sent = []
    word = []
    lttr_word = []
    dic1 = {}
    dic2 = {}
    dic3 = {}
    text = text.replace('!', '.')
    text = text.replace('?', '.')
    # Многоточия - если в конце строки, тогда заменяем точкой
    text = re.sub(r'\.\.\.\n', '.\n', text)
    # Если в середине, тогда сложнее
    # Если после идет заглавная буква, тогда тоже меняем на точку
    r1 = re.findall(r'\.\.\.\s+[А-ЯЁ]', text)
    for i in range(len(r1)):
        l1 = r1[i][-1]
        text = re.sub(r'\.\.\.\s+'+l1, '. '+l1, text)
    # Если же идет что-то другое, тогда просто убираем
    text = re.sub(r'\.\.\.\s+', ' ', text)
    all_par = text.split('\n')
    for line in all_par:
        try:
            m1 = line[-1]
        except IndexError:
            continue
        try:
            m2 = line[0]
        except IndexError:
            continue
        par = line.split('.')
        if (par[0] == line) and (m1 not in r5) and (m2 != '–'):
            zagol += 1
            zg.append(line)
        else:
            paragr += 1
            num_sent = len(par) - 1
            prg_sent.append(num_sent)
            dic1.update({line:num_sent})
            for line01 in par:
                sentense.append(line01)
                num_words = line01.count(' ') + 1
                wrd_sent.append(num_words)
                dic2.update({line01:num_words})
                words = re.split(r' |–', line01)
                for line02 in words:
                    num_letts = len(line02)
                    word.append(line02)
                    dic3.update({line02:num_letts})
                    lttr_word.append(num_letts)

    sent_num = len(sentense)
    word_num = len(word)
    save_file(sentense, 'Res/sentens.txt')
    save_file(word, 'Res/wordsil.txt')
    print(zagol, 'заголовков')
    print(paragr, 'абзацев')
    print(sent_num, 'предложений')
    print(word_num, 'слов')
    save_file(zg, 'Data/zagl.txt')
    prg_sent.sort()
    wrd_sent.sort()
    lttr_word.sort()
    max_sent = prg_sent[-1]
    min_sent = prg_sent[0]
    max_word = wrd_sent[-1]
    min_word = wrd_sent[0]
    max_lettr = lttr_word[-1]
    min_lettr = lttr_word[0]
    print('Интервал количества предложений в абзаце', min_sent, max_sent)
    print('Интервал количества слов в предложении', min_word, max_word)
    print('Интервал количества букв в слове', min_lettr, max_lettr)
    save_dict(dic1, 'Res/dic01.txt')
    save_dict(dic2, 'Res/dic02.txt')
    save_dict(dic3, 'Res/dic03.txt')
    lst_dic1 = list(dic1.items())
    lst_dic1.sort(key=lambda i:i[1], reverse=True)
    lst_dic2 = list(dic2.items())
    lst_dic2.sort(key=lambda i:i[1], reverse=True)
    lst_dic3 = list(dic3.items())
    lst_dic3.sort(key=lambda i:i[1], reverse=True)
    sent_per_par = []
    sent_per_par_freq = []
    itr = min_sent
    m2 = 0
    for i in range(max_sent - min_sent):
        m1 = prg_sent.count(itr)
        m2 += m1
        sent_per_par.append(m1)
        sent_per_par_freq.append(m1/paragr)
        itr += 1
    print(m2, paragr)
    word_per_sent = []
    word_per_sent_freq = []
    itr = min_word
    m2 = 0
    for i in range(max_word - min_word):
        m1 = wrd_sent.count(itr)
        m2 += m1
        word_per_sent.append(m1)
        word_per_sent_freq.append(m1/len(sentense))
        itr += 1
    print(m2, len(sentense))
    lett_per_word = []
    lett_per_word_freq = []
    itr = min_lettr
    m2 = 0
    for i in range(max_lettr - min_lettr):
        m1 = lttr_word.count(itr)
        m2 += m1
        lett_per_word.append(m1)
        lett_per_word_freq.append(m1/len(word))
        itr += 1
    print(m2, len(word))
    a1,b1 = num_freqs(prg_sent)
    a2,b2 = num_freqs(wrd_sent)
    a3,b3 = num_freqs(lttr_word)
    print(sum(sent_per_par_freq), sum(word_per_sent_freq), sum(lett_per_word_freq))
    save_file(sent_per_par_freq, 'Res/sent_freq.txt')
    save_file(word_per_sent_freq, 'Res/word_freq.txt')
    save_file(lett_per_word_freq, 'Res/lett_freq.txt')
    save_file(sent_per_par, 'Res/sent.txt')
    save_file(a1,'Res/sent1.txt')
    save_file(word_per_sent, 'Res/word.txt')
    save_file(a2,'Res/word1.txt')
    save_file(lett_per_word, 'Res/lett.txt')
    save_file(a3,'Res/lett1.txt')
    save_file(prg_sent, 'Res/text.txt')

def extract_text_freqs(text):
    # На вход подается нормализованный текст. Нам необходимо оставить в нем только 
    # слова и посчитать их безусловную и условную частоту.
    # Сначала убираем все лишнее (заглавные буквы, знаки препинания, переводы строк и пр.)
    text = text.lower()
    signs = ['.', ',', '!', '?', '"', '’', '–', '(', ')', ';', ':']
    for sign in signs:
        text = text.replace(sign, ' ')
    save_file(text, 'Res/tmp.txt')
    text = text.replace('\n', ' ')
    text = re.sub(r'\s+', ' ', text)
    text = text.split()
    text.sort(key=lambda i:len(i))
    max_len_of_word = len(text[-1])
    num_words_per_len = np.zeros((max_len_of_word), dtype=int)
    for word in text:
        i = len(word) - 1
        num_words_per_len[i] += 1
    a1 = num_words_per_len[0]
    one_lett = text[0:a1]
    m = a1
    a2 = num_words_per_len[1]
    two_lett = text[m:m+a2]
    m = m + a2
    a3 = num_words_per_len[2]
    three_lett = text[m:m+a3]
    m = m + a3
    a4 = num_words_per_len[3]
    four_lett = text[m:m+a4]
    m = m + a4
    all_other_lett = text[m:]
    # Считаем частоты однобуквенных слов
    one_lett_freq = np.zeros((33), dtype=float)
    dop1 = 1/a1
    for sign in one_lett:
        one_lett_freq[index_lett(sign)] += dop1
    save_file(one_lett_freq, 'Res/Freqs/onelett.txt')
    # считаем частоты двухбуквенных слов
    # для этого сначала нужно определить частоту первых букв
    twolett_first = np.zeros((33), dtype=float)
    twolett_second = np.zeros((33,33), dtype=float)
    dop2 = 1/a2
    for tlw in two_lett:
        twolett_first[index_lett(tlw[0])] += dop2
        twolett_second[index_lett(tlw[0])][index_lett(tlw[1])] += dop2
    save_matr(twolett_first, 'Res/Freqs/twolett_first.txt')
    save_matr(twolett_second, 'Res/Freqs/twolett_second.txt')
    # считаем частоты трехбуквенных слов
    # Здесь необходимо сначала вычислить частоту первых, затем частоту 
    # вторых, и только потом - частоту третьих букв
    threelett_first = np.zeros((33), dtype=float)
    threelett_second = np.zeros((33,33), dtype=float)
    threelett_third = np.zeros((33,33,33), dtype=float)
    dop3 = 1/a3
    for thr in three_lett:
        threelett_first[index_lett(thr[0])] += dop3
        threelett_second[index_lett(thr[0])][index_lett(thr[1])] += dop3
        threelett_third[index_lett(thr[0])][index_lett(thr[1])][index_lett(thr[2])] += dop3
    save_matr(threelett_first, 'Res/Freqs/threelett_first.txt')
    save_matr(threelett_second, 'Res/Freqs/threelett_second.txt')
    save_matr(threelett_third, 'Res/Freqs/threelett_third.txt')
    # считаем частоты четырехбуквенных слов
    # Аналогично тому, что мы указывали выше
    fourlett_first = np.zeros((33), dtype=float)
    fourlett_second = np.zeros((33,33), dtype=float)
    fourlett_third = np.zeros((33,33,33), dtype=float)
    fourlett_fourth = np.zeros((33,33,33,33), dtype=float)
    dop4 = 1/a4
    for fur in four_lett:
        fourlett_first[index_lett(fur[0])] += dop4
        fourlett_second[index_lett(fur[0])][index_lett(fur[1])] += dop4
        fourlett_third[index_lett(fur[0])][index_lett(fur[1])][index_lett(fur[2])] += dop4
        fourlett_fourth[index_lett(fur[0])][index_lett(fur[1])][index_lett(fur[2])][index_lett(fur[3])] += dop4
    save_matr(fourlett_first, 'Res/Freqs/fourlett_first.txt')
    save_matr(fourlett_second, 'Res/Freqs/fourlett_second.txt')
    save_matr(fourlett_third, 'Res/Freqs/fourlett_third.txt')
    save_matr(fourlett_fourth, 'Res/Freqs/fourlett_fourth.txt')
    # Все остальные слова анализируем "скопом", вычисляя условные вероятности их
    # следования друг за другом
    # При этом очевидно, что для трехбуквенных слов актуальна будет глубина в три буквы следования, 
    # а для четырехбуквенных - в четыре. То есть их мы также будем рассматривать по отдельности
    fivelett_first = np.zeros((33), dtype=float)
    fivelett_second = np.zeros((33,33), dtype=float)
    fivelett_third = np.zeros((33,33,33), dtype=float)
    fivelett_fourth = np.zeros((33,33,33,33), dtype=float)
    fivelett_fifth = np.zeros((33,33,33,33,33), dtype=float)
    num_per_five = 0
    num_cycles = len(num_words_per_len) - 4
    for i in range(num_cycles):
        num_per_five += num_words_per_len[i + 4]*(i + 1)
    dop5 = 1/num_per_five
    for oth in all_other_lett:
        k1 = len(oth)
        for i in range(k1 - 4):
            fivelett_first[index_lett(oth[0+i])] += dop5
            fivelett_second[index_lett(oth[0+i])][index_lett(oth[1+i])] += dop5
            fivelett_third[index_lett(oth[0+i])][index_lett(oth[1+i])][index_lett(oth[2+i])] += dop5
            fivelett_fourth[index_lett(oth[0+i])][index_lett(oth[1+i])][index_lett(oth[2+i])][index_lett(oth[3+i])] += dop5
            fivelett_fifth[index_lett(oth[0+i])][index_lett(oth[1+i])][index_lett(oth[2+i])][index_lett(oth[3+i])][index_lett(oth[4+i])] += dop5
    save_matr(fivelett_first, 'Res/Freqs/fivelett_first.txt')
    save_matr(fivelett_second, 'Res/Freqs/fivelett_second.txt')
    save_matr(fivelett_third, 'Res/Freqs/fivelett_third.txt')
    save_matr(fivelett_fourth, 'Res/Freqs/fivelett_fourth.txt')
    save_matr(fivelett_fifth, 'Res/Freqs/fivelett_fifth.txt')
