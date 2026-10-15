# Лабораторная работа №3

### Овчаренко Анна Сергеевна
### БИВТ-26-6-2
---
## Задание А
```
import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str: 
    if casefold: 
        text = text.casefold() 
    else: 
        text = text.lower()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    return ' '.join(text.split())
def tokenize(text: str) -> list[str]: 
    return re.findall(r'\w+(?:-\w+)*', text)
def count_freq(tokens: list[str]) -> dict[str, int]: 
    freq = {} 
    for w in tokens: 
        freq[w] = freq.get(w, 0) + 1 
    return freq
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]: 
    pairs = sorted(freq.items(), key=lambda p: (-p[1], p[0])) 
    return pairs[:n]
if __name__ == "__main__":
    a = [
        "ПрИвЕт\nМИр\t",
        "ёжик, Ёлка",
        "Hello\r\nWorld",
        "  двойные   пробелы  "
    ]
    b = [
        "привет мир",
        "hello,world!!!",
        "по-настоящему круто",
        "2025 год",
        "emoji 😀 не слово"
    ]
    c = [
        ["a","b","a","c","b","a"],
        ["bb","aa","bb","aa","cc"]
    ]
    for i in a:
        print(f"{i} -> {normalize(i)}")
    for i in b:
        print(f"{i} -> {tokenize(i)}")
    for i in c:
        freq = count_freq(i)
        print(f"{i} -> {freq}; top_n({i}) -> {top_n(freq, 2)}")
```
**Вывод**
![результат вывода](images/lab_03/1.png)
