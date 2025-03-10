from main import *
from tkinter import *


def third_win():
    root2 = Toplevel()
    root2.title("Вікно 3")
    root2.configure(bg="#98E5FE")
    root2.geometry("500x350")


    def st1():
        result = step1_simple(a, b, u)
        Label(root2, bg="#98E5FE", text=str(result), font="Arial 12").place(x=130, y=100)

    def st2():
        result = step2_simple(a, b, c, u)
        Label(root2, bg="#98E5FE", text=str(result), font="Arial 12").place(x=130, y=125)
        Label(root2, bg="#98E5FE", text=str(result), font="Arial 12").place(x=70, y=250)

    def save_result_d_simple():
        result = step2_simple(a, b, c, u)
        save_res = open("D_simple.txt", "w+")
        save_res.write(str(result))
        save_res.close()

    Label(root2, bg="#98E5FE", text="A:", font="Arial 12").place(x=10, y=10)
    Label(root2, bg="#98E5FE", text=str(a), font="Arial 12").place(x=100, y=10)
    Label(root2, bg="#98E5FE", text="B:", font="Arial 12").place(x=10, y=35)
    Label(root2, bg="#98E5FE", text=str(b), font="Arial 12").place(x=100, y=35)
    Label(root2, bg="#98E5FE", text="C:", font="Arial 12").place(x=10, y=60)
    Label(root2, bg="#98E5FE", text=str(c), font="Arial 12").place(x=100, y=60)
    Label(root2, bg="#98E5FE", text="¬C:", font="Arial 12").place(x=10, y=60)
    Label(root2, bg="#98E5FE", text=str(u-c), font="Arial 12").place(x=100, y=60)
    Label(root2, bg="#98E5FE", text="A △ B:", font="Arial 12").place(x=10, y=100)
    Label(root2, bg="#98E5FE", text="(A △ B) ∩ ¬C:", font="Arial 12").place(x=10, y=125)
    Label(root2, bg="#98E5FE", text="D = ", font="Arial 12").place(x=30, y=250)

    Button(root2, bg="#FFFFFF", width=10, text="Крок 1", font="Arial 12", command=st1).place(x=30, y=200)
    Button(root2, bg="#FFFFFF", width=10, text="Крок 2", font="Arial 12", command=st2).place(x=150, y=200)

    Button(root2, bg="#FFFFFF", width=30, text="Зберегти результат у файл D_simple.txt", font="Arial 11", command=save_result_d_simple).place(x=30, y=280)
