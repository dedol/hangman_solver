# Hangman solver algorithm
Iterative algorithm for solving words in Hangman game.

- Two arguments are presented at the input: word masks (unknown letters are replaced by asterisk) and letters that are not in the word.
- The result of the work is the most likely letter that will be in the word.
- Regular expressions are used to quickly search for words in the dictionary (dict.txt file).
- The algorithm can work with words in any language, provided that the appropriate dictionary is used.


# Алгоритм для отгадывания слова
Итерационный алгоритм разгадывания слов при игре в Виселицу. 

- На вход подается два аргумента: маска слова (неизвестные буквы заменяются символом звездочки) и отсутствующие в слове буквы. 
- Результатом работы является наиболее вероятная буква, которая может быть в слове.
- Для быстрого поиска слов в словаре (файл dict.txt) используются регулярные выражения.
- Алгоритм может работать со словами на любом языке, при условии использования соответствующего словаря.