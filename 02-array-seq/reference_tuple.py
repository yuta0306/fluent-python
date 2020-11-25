def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

tf = (10, 'alpha', (1, 2))
tm = (10, 'alpha', [1, 2])

print(f'tf:{fixed(tf)}')
print(f'tm:{fixed(tm)}') 

new_tf = tuple(tf)
new_tm = tuple(tm)

print(f'tf == new_tf? {tf == new_tf}')
print(f'tm == new_tm? {tm == new_tm}')

