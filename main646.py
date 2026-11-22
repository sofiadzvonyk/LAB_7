def check(x, y, xc, yc, r):
    return ["NO", "YES"][(x - xc)**2 + (y - yc)**2 <= r**2]
x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
print(check(x, y, xc, yc, r))