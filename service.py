import numpy as np
import re
import math
from random import random
from random import seed
from random import randint

def word_count(text, num_of_lett):
    reg_var = r'\b\w{%d}\b' % num_of_lett
    wrd = re.findall(reg_var, text)
    m = len(wrd)
#    print('Всего ',m,' слов из ', num_of_lett, ' букв')
    wrdsl = set(wrd)
    wrd = list(wrdsl)
    m = len(wrd)
    wrd.sort()
#    print('Из них ',m, ' уникальных')
    return wrd,m

def word_count_f(text, num_of_lett):
    reg_var = r'\b\w{%d}\b' % num_of_lett
    wrd = re.findall(reg_var, text)
    m = len(wrd)
    wrdsl = set(wrd)
    wrd = list(wrdsl)
    n = len(wrd)
    wrd.sort()
    return m,n

def word_count_p(text, num_of_lett):
    reg_var = r'\b\w{%d}\b' % num_of_lett
    wrd = re.findall(reg_var, text)
    return wrd

def index_lett(lett1):
    a = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя"
    res = a.find(lett1)
    return res

def boostr(freqs):
    nums = len(freqs)
    seed()
    r = random()
    l = 0
    res = randint(0,32)
    for i in range(nums):
        l = l + freqs[i]
        if l >= r:
            res = i
            break
    return res

def init_signs():
    f = open('format.mod','r')
    r = f.read()
    f.close()
    r1 = r.split('\n')
    return r1[0],r1[1],r1[2],r1[3],r1[4],r1[5]


def fdiff(tx1,tx2):
    res = True
    m = min(len(tx1), len(tx2))
    if (abs(len(tx1) - len(tx2)) > 4):
        res = False
    else:
        for i in range(m):
            if tx1[i] != tx2[i]:
                res = False
                break
    return res

def fsquar(tx1,tx2):
    res = True
    m1 = len(tx1)
    m2 = len(tx2)
    if m1 <= m2:
        rx1 = tx1
        rx2 = tx2
    else:
        rx1 = tx2
        rx2 = tx1
#  rx1 всегда самая короткая
#  не рассчитываем для коротких слов
    if (max(m1,m2) < 5):
        res = False
    else:
        rx1 = tx1[:-2]
        res = fdiff(rx1,rx2)
    return res

def differen(tx1,tx2):
    res = False
    m = min(len(tx1), len(tx2))
    i = 0
    n = 1
    while tx1[i] == tx2[i]:
        i = i + 1
        if i == m:
            break
    n = i
    if m - n < 3 and n > 2:
        res = True
    return res 

def ext_root(name):
    voc_lett = ['у','е','ё','ы','а','о','э','я','и','ю']
    if name[len(name) - 1] in voc_lett:
        name_fir = name[0:-1]
    else:
        name_fir = name
    return name_fir

def eq_root(root, name):
    k = len(root)
    if name[0:k] == root:
        return True
    else:
        return False


def norm_text(g, filename):
    g = g.replace('…', '...')
    g = g.replace('_', ' ')
    g = g.replace('c', 'с')
    g = g.replace('C', 'С')
    g = g.replace('T', 'Т')
    g = g.replace('a', 'а')
    g = g.replace('A', 'А')
    g = g.replace('e', 'е')
    g = g.replace('E', 'Е')
    g = g.replace('X', 'Х')
    g = g.replace('x', 'х')
    g = g.replace('O', 'О')
    g = g.replace('o', 'о')
    g = g.replace('P', 'Р')
    g = g.replace('p', 'р')
    g = g.replace('y', 'у')
    g = g.replace('m', 'т')
    g = g.replace('-', '–')
    g = g.replace('—', '–')
    g = g.replace('\'', '’')
    g = g.replace('«', '"')
    g = g.replace('»', '"')
    g = g.replace('“', '"')
    g = g.replace('„', '"')
    g = g.replace('”', '"')
    g = g.replace('“', '"')
    g = g.replace('‘', '"')
    g = g.replace('`', 'ё')
    g = g.replace('о?л', 'ол')    
    g = g.replace('у?ю', 'ую')
    g = g.replace('о?н', 'он')
    g = g.replace('б?л', 'бол')
    g = g.replace('и?м', 'им')
    g = g.replace('В?р', 'Вор')
    g = g.replace('р?н', 'рон')
    g = g.replace('о?к', 'ок')
    g = g.replace('&#243;', 'о')
    g = g.replace('&#769;', '')
    g = g.replace('&gt;', '')
    g = g.replace('#8209;', '–')
    g = g.split('\n')

    f = open(filename, 'w')
    for line in g:
        s = re.sub(r'^\s+\b', '', line)
        line = re.sub(r'\s+', ' ', s)
        if len(line) > 1:
            f.write(line.lstrip() + '\n')
    f.close()

def save_file(arr, filename):
    f = open(filename, 'w')
    for line in arr:
        if type(line) == str:
            f.write(line + '\n')
        else:
            f.write(str(line) + '\n')
    f.close()

def save_file2(arr2, filename):
    f = open(filename, 'w')
    m1, m2 = arr2.shape
    for i in range(m1):
        for j in range(m2):
            f.write(str(arr2[i][j]) + '\n')
    f.close()

def save_file3(arr3, filename):
    f = open(filename, 'w')
    m1, m2, m3 = arr3.shape
    for i in range(m1):
        for j in range(m2):
            for k in range(m3):
                f.write(str(arr3[i][j][k]) + '\n')
    f.close()

def save_file4(arr4, filename):
    f = open(filename, 'w')
    m1, m2, m3, m4 = arr4.shape
    for i in range(m1):
        for j in range(m2):
            for k in range(m3):
                for l in range(m4):
                    f.write(str(arr4[i][j][k][l]) + '\n')
    f.close()

def save_file5(arr5, filename):
    f = open(filename, 'w')
    m1, m2, m3, m4, m5 = arr5.shape
    for i in range(m1):
        for j in range(m2):
            for k in range(m3):
                for l in range(m4):
                    for v in range(m5):
                        f.write(str(arr5[i][j][k][l][v]) + '\n')
    f.close()

def num_freqs(lst_r):
    lst_r.sort()
    num_all = sum(lst_r)
    max_r = lst_r[-1]
    min_r = lst_r[0]
    lst_num = []
    lst_freq = []
    itr = min_r
    m2 = 0
    for i in range(max_r - min_r):
        m1 = lst_r.count(itr)
        m2 += m1
        lst_num.append(m1)
        lst_freq.append(m1/num_all)
        itr += 1
    return lst_num, lst_freq

def save_dict(dic, flnm):
    lst_dic = list(dic.items())
    lst_dic.sort(key=lambda i:i[1], reverse=True)
    f = open(flnm, 'w')
    for line in lst_dic:
        f.write(str(line[1]) + ' : ' +  line[0] + '\n')
    f.close()

def create_weights(shp):
    num_shp = len(shp)
    nk = np.ones((num_shp), dtype=int)
    for i in range(num_shp):
        nk[i] = math.prod(shp[(i+1):])
    return nk

def save_matr(arr, flnm):
    f = open(flnm, 'w')
    shp = arr.shape
    num_shp = len(shp)
    num_el = 1
    for el in shp:
        f.write(str(el) + ' ')
        num_el *= el
    f.write('\n')
    tmp_arr = np.reshape(arr, num_el)
    nk = create_weights(shp)
    for counter in range(num_el):
        if tmp_arr[counter] != 0:
            indexes = np.zeros((num_shp), int)
            dop = counter
            for i in range(num_shp):                
                indexes[i] = dop//nk[i]
                dop = dop % nk[i]
            str_to_file = ''
            for i in range(num_shp):
                str_to_file += str(indexes[i]) + ' '
            str_to_file += str(tmp_arr[counter]) + '\n'
            f.write(str_to_file)
    f.close()


def load_matr(flnm):
    f = open(flnm, 'r')
    shapr = f.readline().split()
    shp = []
    for line in shapr:
        shp.append(int(line))
    num_shp = len(shp)
    num_el = 1
    for el in shp:
        num_el *= el
    tmp_arr = np.zeros((num_el), dtype=float)
    nk = create_weights(shp)
    lines = f.readlines()
    for line in lines:
        line = line.split()
        indx = 0
        for i in range(num_shp):
            indx += int(line[i])*nk[i]
        tmp_arr[indx] = float(line[len(line) - 1])
    res = tmp_arr.reshape(shp)
    f.close()
    return res
