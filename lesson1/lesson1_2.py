print('Введите время в секундах: ')
time = int(input())
h = time // 3600
mins = (time % 3600) // 60
sec = (time % 3600) % 60
if h < 10:
    h = ('0{}'.format(h))
if mins < 10:
    mins = ('0{}'.format(mins))
if sec < 10:
    sec = ('0{}'.format(sec))
print(h, mins, sec, sep=':')
