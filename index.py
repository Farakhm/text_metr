import datetime
from lett_metr import lett_metrix
from word_metr import word_metrix
from sintext import sintes
from text_metrix import extract_text_metrix
from text_metrix import extract_text_freqs
from service import norm_text

t1 = datetime.datetime.now()
# Открываем текст
f = open('Data/first.txt', 'r')
g = f.read()
f.close()

filename = 'Data/norm_text.txt'
norm_text(g, filename)

f = open(filename, 'r')
g = f.read()
f.close()
#extract_text_metrix(g)
extract_text_freqs(g)

# Снимаем различные метрики текста

#lett_metrix(g)
#word_metrix(g)

#sintes()

#name_metrix(g)

t2 = datetime.datetime.now()
print('That s all! Work time:', t2 - t1)



