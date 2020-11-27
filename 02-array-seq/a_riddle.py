t = (1, 2, [30, 40])
try:
    t[2] += [50, 60]
except Exception as e:
    print('An error occured')
    print(e)

print(t)