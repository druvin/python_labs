import sys
from text import normalize, tokenize, count_freq, top_n

text = sys.stdin.read()
words = tokenize(normalize(text))
freq = count_freq(words)

print(f'Всего слов: {len(words)}')
print(f'Уникальных слов: {len(freq)}')
print('Топ-5:')

for word, count in top_n(freq):
    print(f'{word}:{count}')