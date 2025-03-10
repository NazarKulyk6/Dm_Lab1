from main import *
from window2 import second_win
from window3 import third_win
from window4 import fourth_win
from window5 import fifth_win
from tkinter import *

root = Tk()
root.title("Головне вікно")
root.configure(bg="#98E5FE")
root.geometry("750x550")


def a_set():
    a_rand(input_a, min_u, max_u, root)
    u_gen(min_u, max_u)

def b_set():
    b_rand(input_b, min_u, max_u, root)
    u_gen(min_u, max_u)

def c_set():
    c_rand(input_c, min_u, max_u, root)
    u_gen(min_u, max_u)

def a_w():
    a_write(enter_a, root)

def b_w():
    b_write(enter_b, root)

def c_w():
    c_write(enter_c, root)

Button(root, bg="#FFFFFF", text="Вікно 2", font="Arial 12", command=second_win).place(x=650,y=170)
Button(root, bg="#FFFFFF", text="Вікно 3", font="Arial 12", command=third_win).place(x=650,y=230)
Button(root, bg="#FFFFFF", text="Вікно 4", font="Arial 12", command=fourth_win).place(x=650,y=290)
Button(root, bg="#FFFFFF", text="Вікно 5", font="Arial 12", command=fifth_win).place(x=650,y=350)

Label(root, text="Кулик Назар Ярославлвич", font="Arial 14", bg="#98E5FE").place(x=5, y=5)
Label(root, text="Студент групи ІО-" + "43", font="Arial 14", bg="#98E5FE").place(x=5, y=30)
Label(root, text="Номер у списку: " + "15", font="Arial 14", bg="#98E5FE").place(x=5, y=55)
Label(root, text="Варіант: " + str((25 + 33 % 60) % 30 + 1), font="Arial 14", bg="#98E5FE").place(x=5, y=80)

Label(root, bg="#98E5FE", text="Потужність", font="Arial 14").place(x=40, y=110)
Label(root, bg="#98E5FE", text="А:", font="Arial 12").place(x=25, y=145)
Label(root, bg="#98E5FE", text="В:", font="Arial 12").place(x=25, y=175)
Label(root, bg="#98E5FE", text="С:", font="Arial 12").place(x=25, y=205)
input_a = Entry(root, width=12, font="Arial 12")
input_a.place(x=80, y=145)
input_b = Entry(root, width=12, font="Arial 12")
input_b.place(x=80, y=175)
input_c = Entry(root, width=12, font="Arial 12")
input_c.place(x=80, y=205)

Label(root, bg="#98E5FE", text="Діапазон універсальної множини", font="Arial 14").place(x=295, y=110)
Label(root, bg="#98E5FE", text="U:", font="Arial 12").place(x=290, y=145)
Label(root, bg="#98E5FE", text="(", font="Arial 14").place(x=325, y=140)
Label(root, bg="#98E5FE", text=";", font="Arial 14").place(x=415, y=140)
Label(root, bg="#98E5FE", text=")", font="Arial 14").place(x=505, y=140)
min_u = Entry(root, width=7, font="Arial 12")
min_u.place(x=340, y=145)
max_u = Entry(root, width=7, font="Arial 12")
max_u.place(x=435, y=145)


Label(root, bg="#98E5FE", text="Випадкова генерація", font="Arial 14").place(x=40, y=400)
Button(root, width=15, bg="#FFFFFF", text="Сформувати A", font="Arial 12", command=a_set).place(x=50, y=440)
Button(root, width=15, bg="#FFFFFF", text="Сформувати B", font="Arial 12", command=b_set).place(x=50, y=470)
Button(root, width=15, bg="#FFFFFF", text="Сформувати C", font="Arial 12", command=c_set).place(x=50, y=500)

Label(root, bg="#98E5FE", text="Ручний ввід", font="Arial 14").place(x=40, y=245)
Label(root, bg="#98E5FE", text="А:", font="Arial 12").place(x=25, y=295)
Label(root, bg="#98E5FE", text="В:", font="Arial 12").place(x=25, y=325)
Label(root, bg="#98E5FE", text="С:", font="Arial 12").place(x=25, y=355)
enter_a = Entry(root, width=25, font="Arial 12")
enter_a.place(x=80, y=295)
enter_b = Entry(root, width=25, font="Arial 12")
enter_b.place(x=80, y=325)
enter_c = Entry(root, width=25, font="Arial 12")
enter_c.place(x=80, y=355)
Button(root, width=17, bg="#FFFFFF", text="Підтвердити", font="Arial 12", command=a_w).place(x=340, y=290)
Button(root, width=17, bg="#FFFFFF", text="Підтвердити", font="Arial 12", command=b_w).place(x=340, y=320)
Button(root, width=17, bg="#FFFFFF", text="Підтвердити", font="Arial 12", command=c_w).place(x=340, y=350)

Label(root, bg="#98E5FE", text="Множини", font="Arial 14").place(x=295, y=400)
Label(root, bg="#98E5FE", text="A:", font="Arial 12").place(x=280, y=440)
Label(root, bg="#98E5FE", text="B:", font="Arial 12").place(x=280, y=470)
Label(root, bg="#98E5FE", text="C:", font="Arial 12").place(x=280, y=500)
root.mainloop()
