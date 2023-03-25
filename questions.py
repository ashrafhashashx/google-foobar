def asking_for_information():
    print('مرحبا ، بدي أحكي معك.')
    name = input(' اشو اسمك؟')
    print(' كيفك يا ', name)
    age = int(input(' شقد عمرك؟'))
    if age < 0:
        print('شي مستحيل!')
    elif age < 15:
        print('أنت صغير بالعمر')
    elif age < 75:
        print('ماشي  الحال')
    elif age < 120:
        print('أنت كبير بالعمر')
    else:
        print('هاد الشي غير محتمل!')

def asking_for_money(name):
    print(' معلم ، ', name)
    money = float(input(' شقد معك مصاري؟'))
    if money < 50:
        print('يا حرام ما معك مصاري كتير :(')
    else:
        print('خرج تديّني 50 دولار؟')

# [1,2,3,4] 10
# [11,12,13,14]
def z(m, n):
    m2 = []
    for i in m:
        m2.append(i + n)
    return m2

def print_array_of_array(m):
    for i in m:
        for j in i:
            print(j, ' ', end='')
        print()
    print('----------------------------')

