a = int(input("podaj liczbe a :"))
b = int(input("podaj liczbe b :"))
c = int(input("podaj liczbe c :"))

maximum = max(a, b, c)
minimum = min(a, b, c)

a_max = a == maximum
b_max = b == maximum
c_max = c == maximum

a_min = a == minimum
b_min = b == minimum
c_min = c == minimum

print("a jest max: ", a_max)
print("b jest max: ", b_max)
print("c jest max: ", c_max)

print("a jest min: ", a_min)
print("b jest min: ", b_min)
print("c jest min: ", c_min)