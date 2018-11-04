print('Загадано четырехбуквенное слово из букв А,E,Н,О,С,Т.')
print('Отгадай!')

import random
letters = ['А', 'Е', 'Н', 'О', 'С', 'Т']
word = ''
letter = ''
for x in range(4):
    letter = random.choice(letters)
    if letter in word:
        while letter in word:
            letter = random.choice(letters)
        else:
            word = word + letter
    else:
        word = word + letter

k = 0
a = 0
userword = ''
num = 1
while word != userword:
    userword = input()
    userword = userword.upper()
    print('Попытка №', num, userword)
    for i in range(len(word)):
        if word[i] == userword[0] or word[i] == userword[1]\
                or word[i] == userword[2] or word[i] == userword[3]:
            k += 1
    num += 1
    if num > 10:
        print('Вы проиграли! Слово:', word)
        break
    for i in range(4):
        if word[i] == userword[i]:
            a += 1
    print('На своем месте:', a)
    print('На чужом месте:', k-a)
    a = 0
    k = 0
else:
    print('Вы выиграли!')



