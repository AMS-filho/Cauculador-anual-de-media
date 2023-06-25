print('\033[33m-=\033[m' * 20)
print('Cauculador de Media Anual')
print('\033[33m-=\033[m' * 20)
materia = str(input('Materia:'))
print('\033[33m-=\033[m' * 20)
n1 = float(input('Nota da 1° prova da 1° unidade: '))
n2 = float(input('Nota da 2° prova da 1° unidade: '))
m1 = (n1 + n2) / 2
if m1 < 7:
    print('A sua media é \033[31m{}\033[m.'.format(m1))
    print('\033[31mPRECISA MELHORAR! Esta abaixo da media\033[m')
if m1 == 7:
    print('A sua media é \033[34m{}\033[m.'.format(m1))
    print('\033[34mBOA! Esta na media!\033[m')
if m1 > 7:
    print('A sua media é \033[32m{}\033[m.'.format(m1))
    print('\033[32mPARABÉNS! Esta acima da media!\033[m')
print('\033[33m-=\033[m' * 20)
n3 = float(input('Nota da 1° prova da 2° unidade: '))
n4 = float(input('Nota da 2° prova da 2° unidade: '))
m2 = (n3 + n4) / 2
if m2 < 7:
    print('A sua media é \033[31m{}\033[m.'.format(m2))
    print('\033[31mPRECISA MELHORAR! Esta abaixo da media\033[m')
if m2 == 7:
    print('A sua media é \033[34m{}\033[m.'.format(m2))
    print('\033[34mBOA! Esta na media!\033[m')
if m2 > 7:
    print('A sua media é \033[32m{}\033[m.'.format(m2))
    print('\033[32mPARABÉNS! Esta acima da media!\033[m')
print('\033[33m-=\033[m' * 20)
n5 = float(input('Nota da 1° prova da 3° unidade: '))
n6 = float(input('Nota da 2° prova da 3° unidade: '))
m3 = (n5 + n6) / 2
if m3 < 7:
    print('A sua media é \033[31m{}\033[m.'.format(m3))
    print('\033[31mPRECISA MELHORAR! Esta abaixo da media\033[m')
if m3 == 7:
    print('A sua media é \033[34m{}\033[m.'.format(m3))
    print('\033[34mBOA! Esta na media!\033[m')
if m3 > 7:
    print('A sua media é \033[32m{}\033[m.'.format(m3))
    print('\033[32mPARABÉNS! Esta acima da media!\033[m')
print('\033[33m-=\033[m' * 20)
n7 = float(input('Nota da 1° prova da 4° unidade: '))
n8 = float(input('Nota da 2° prova da 4° unidade: '))
m4 = (n7 + n8) / 2
if m4 < 7:
    print('A sua media é \033[31m{}\033[m.'.format(m4))
    print('\033[31mPRECISA MELHORAR! Esta abaixo da media\033[m')
if m4 == 7:
    print('A sua media é \033[34m{}\033[m.'.format(m4))
    print('\033[34mBOA! Esta na media!\033[m')
if m4 > 7:
    print('A sua media é \033[32m{}\033[m.'.format(m4))
    print('\033[32mPARABÉNS! Esta acima da media!\033[m')
print('\033[33m-=\033[m' * 20)
ma = m1 + m2 + m3 + m4
if ma < 28:
    print('A sua media anual foi \033[31m{}\033[m'.format(ma))
    print('\033[31mJa era, Reprovou de ano\033[m')
if ma > 28:
    print('A sua media anual foi \033[32m{}\033[m' .format(ma))
    print('\033[32mParabés, Voce passou de ano!\033[m')
print('\033[33m-=\033[m' * 20)
