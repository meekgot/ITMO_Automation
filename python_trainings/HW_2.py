def arg(a=(1, 2, 3, 4)):
    return a[0]

print(arg())

def task_func(radius = 4, pi = 3.14159):
    return pi * (radius**2)

print(task_func())

def compute_surface(rad, pi=3.14159):
    return pi * rad * rad

print(compute_surface(4))