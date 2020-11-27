l = [1, 2, 3]
print(f'l_id: {id(l)}')
l *= 2
print(f'l: {l}')
print(f'l_id: {id(l)}')

t = (1, 2, 3)
print(f't_id: {id(t)}')
t *= 2
print(f't: {t}')
print(f't_id: {id(t)}')