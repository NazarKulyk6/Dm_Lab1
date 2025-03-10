from tkinter import *
import random

a = set()
b = set()
c = set()
u = set()


def a_rand(text, min_entry, max_entry, root):
    a.clear()
    num = int(text.get())
    min_value = int(min_entry.get())
    max_value = int(max_entry.get())
    a.update(random.sample(range(min_value, max_value + 1), num))
    Label(root, bg="#98E5FE", text=str(a), font="Arial 12").place(x=315, y=440)

def b_rand(text, min_entry, max_entry, root):
    b.clear()
    num = int(text.get())
    min_value = int(min_entry.get())
    max_value = int(max_entry.get())
    b.update(random.sample(range(min_value, max_value + 1), num))
    Label(root, bg="#98E5FE", text=str(b), font="Arial 12").place(x=315, y=470)

def c_rand(text, min_entry, max_entry, root):
    c.clear()
    num = int(text.get())
    min_value = int(min_entry.get())
    max_value = int(max_entry.get())
    c.update(random.sample(range(min_value, max_value + 1), num))
    Label(root, bg="#98E5FE", text=str(c), font="Arial 12").place(x=315, y=500)

def u_gen(min_entry, max_entry):
    u.clear()
    min_val = int(min_entry.get())
    max_val = int(max_entry.get())
    for i in range(min_val, max_val + 1):
        u.add(i)

def a_write(input, root):
    for i in input.get().split(','):
        a.add(int(i))
    Label(root, bg="#98E5FE", text=str(a), font="Arial 12").place(x=315, y=440)

def b_write(input, root):
    b.clear()
    for i in input.get().split(','):
        b.add(int(i))
    Label(root, bg="#98E5FE", text=str(b), font="Arial 12").place(x=315, y=470)

def c_write(input, root):
    c.clear()
    for i in input.get().split(','):
        c.add(int(i))
    Label(root, bg="#98E5FE", text=str(c), font="Arial 12").place(x=315, y=500)

def step1(a, b, u):
    not_b = u - b
    res = a & not_b
    return(res)

def step2(a, b, u):
    not_a = u - a
    res = not_a & b
    return(res)

def step3(b, c, u):
    not_c = u - c
    res = not_c | b
    return(res)

def step4(a, b, u):
    not_a = u - a
    not_b = u - b
    res = (a & not_b) | (not_a & b)
    return(res)

def step5(b, c, u):
    not_c = u - c
    res = not_c & (not_c | b)
    return(res)

def step6(a, b, c, u):
    not_a = u - a
    not_b = u - b
    not_c = u - c
    res = ((a & not_b) | (not_a & b)) & (not_c & (not_c | b))
    return(res)

def step1_simple(a, b, u):
    not_a = u - a
    not_b = u - b
    res = (a & not_b) | (b & not_a)
    return(res)

def step2_simple(a, b, c, u):
    not_a = u - a
    not_b = u - b
    not_c = u - c
    res = ((a & not_b) | (b & not_a)) & not_c
    return(res)

def z_my_calc(a, b, u):
    not_a = u - a
    not_b = u - b
    res = not_b - not_a
    return(res)

def z_calc(a, b, u):
    not_a = u.difference(a)
    not_b = u.difference(b)
    res = not_b.difference(not_a)
    return(res)
