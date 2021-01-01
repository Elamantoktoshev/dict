# About my family
family = {
    'Father': 'Suiunbai',
    'Mather': 'Mairam',
    'I': 'Elaman',
    'Brother': 'Baiaman',
    'Sister': 'Kyzjibek'
},
Father = {
    'name': 'Suiunbai',
    'profession': 'bilder',
    'plase work': 'Russia',
    'age': 40,
    'hobby': 'sport'
},
Mather = {
    'name': 'Mairam',
    'Profession': 'Tarbiachy',
    'palce work': 'Baldar bakchasy',
    'age': 36,
    'Hobby': 'read book'
},
Brother = {
    'name': 'Baiaman',
    'Who?': 'peple',
    'Class': 10,
    'age': 16,
    'hobby': 'Ulak'
},
Sister = {
    'name': 'Kyzjibek',
    'Who?': 'peple',
    'class': 3,
    'age': 9,
    'hobby': 'Read book'
}
# for item in family:
# print(item)
while True:
    about = input(
        "If do you want to knaw about my family, you should write <about>,about my Father <Father>, about my Mother <Mother>, about my Brother <Brother>, about my sister <Sister>: ")
    if about == 'about':
        print(family)
    elif about == 'Father':
        print(Father)
    elif about == 'Mother':
        print(Mather)
    elif about == 'Brother':
        print(Brother)
    elif about == 'Sister':
        print(Sister)
    else:
        print('please, write only this words!')
print('welcome to my family')
