from micrograd import Value
a = Value(2.0)
b = Value(3.0)
c = a * b
c.backward()
print(a.grad)   # 期望 3.0
print(b.grad)   # 期望 2.0