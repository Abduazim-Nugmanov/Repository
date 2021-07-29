dict = {'name': ['Amin', 'Roman', 'Iroda'],
        'sex': ['m', 'm', 'f'],
        'age': ['16,19,27']}
while True:
    name = input('Введите свое имя')
    if name == "Amin":
        age = input ('16')
        sex = input ('m')
    if name == 'Roman':
        age = input ('19')
        sex = input ('m')
    if name == "Iroda":
        age = input ('27')
        sex = input ('f')
print(dict.items())
for e in dict:
    print(e)
