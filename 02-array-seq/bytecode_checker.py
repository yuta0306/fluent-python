s = [1, 2, 3]
a = 1
b = 4
import dis

print(dis.dis('s[a] += b'))