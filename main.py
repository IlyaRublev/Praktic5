print("Задание 1")
q = int(input("Введите число:"))
w = q
while q > 0:
    q = q-1
    print(q)
for e in range(w, 0, -1):
    print(e)

print("Задание 2")
j = int(input("Введите число:"))
k = 1
while k<j:
    print(k)
    k=k*2

print("Задание 3")
c = int(input("Введите число:"))
p = 0
u = 1
for t in range(c):
    p, u = u, p + u
    print(p)
