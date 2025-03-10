from main import *
from tkinter import *

def second_win():
    root1 = Toplevel()
    root1.title("Вікно 2")
    root1.configure(bg="#98E5FE")
    root1.geometry("760x500")

    def st1():
        result = step1(a, b, u)
        Label(root1, bg="#98E5FE", text=str(result), font="Arial 12").place(x=340, y=160)

    def st2():
        result = step2(a, b, u)
        Label(root1, bg="#98E5FE", text=str(result), font="Arial 12").place(x=340, y=185)

    def st3():
        result = step3(b, c, u)
        Label(root1, bg="#98E5FE", text=str(result), font="Arial 12").place(x=340, y=210)

    def st4():
        result = step4(a, b, u)
        Label(root1, bg="#98E5FE", text=str(result), font="Arial 12").place(x=340, y=235)

    def st5():
        result = step5(b, c, u)
        Label(root1, bg="#98E5FE", text=str(result), font="Arial 12").place(x=340, y=260)

    def st6():
        result = step6(a, b, c, u)
        Label(root1, bg="#98E5FE", text=str(result), font="Arial 12").place(x=340, y=285)
        Label(root1, bg="#98E5FE", text=str(result), font="Arial 12").place(x=70, y=400)

    def save_result_d():
        result = step6(a, b, c, u)
        save_res = open("D.txt", "w+")
        save_res.write(str(result))
        save_res.close()

    Label(root1, bg="#98E5FE", text="A:", font="Arial 12").place(x=10, y=10)
    Label(root1, bg="#98E5FE", text=str(a), font="Arial 12").place(x=100, y=10)
    Label(root1, bg="#98E5FE", text="B:", font="Arial 12").place(x=10, y=35)
    Label(root1, bg="#98E5FE", text=str(b), font="Arial 12").place(x=100, y=35)
    Label(root1, bg="#98E5FE", text="C:", font="Arial 12").place(x=10, y=60)
    Label(root1, bg="#98E5FE", text=str(c), font="Arial 12").place(x=100, y=60)
    Label(root1, bg="#98E5FE", text="¬A:", font="Arial 12").place(x=10, y=85)
    Label(root1, bg="#98E5FE", text=str(u-a), font="Arial 12").place(x=100, y=85)
    Label(root1, bg="#98E5FE", text="¬B:", font="Arial 12").place(x=10, y=110)
    Label(root1, bg="#98E5FE", text=str(u-b), font="Arial 12").place(x=100, y=110)
    Label(root1, bg="#98E5FE", text="¬C:", font="Arial 12").place(x=10, y=135)
    Label(root1, bg="#98E5FE", text=str(u-c), font="Arial 12").place(x=100, y=135)
    Label(root1, bg="#98E5FE", text="A ∩ ¬B:", font="Arial 12").place(x=10, y=160)
    Label(root1, bg="#98E5FE", text="¬A ∩ B:", font="Arial 12").place(x=10, y=185)
    Label(root1, bg="#98E5FE", text="¬C ∪ B:", font="Arial 12").place(x=10, y=210)
    Label(root1, bg="#98E5FE", text="(A ∩ ¬B) ∪ (¬A ∩ B):", font="Arial 12").place(x=10, y=235)
    Label(root1, bg="#98E5FE", text="¬C ∩ (¬С ∪ B):", font="Arial 12").place(x=10, y=260)
    Label(root1, bg="#98E5FE", text="((A ∩ ¬B) ∪ (¬A ∩ B)) ∩ (¬C ∩ (¬С ∪ B)):", font="Arial 12").place(x=10, y=285)
    Label(root1, bg="#98E5FE", text="D = ", font="Arial 12").place(x=30, y=400)

    Button(root1, bg="#FFFFFF", width=10, text="Крок 1", font="Arial 12", command=st1).place(x=30, y=350)
    Button(root1, bg="#FFFFFF", width=10, text="Крок 2", font="Arial 12", command=st2).place(x=150, y=350)
    Button(root1, bg="#FFFFFF", width=10, text="Крок 3", font="Arial 12", command=st3).place(x=270, y=350)
    Button(root1, bg="#FFFFFF", width=10, text="Крок 4", font="Arial 12", command=st4).place(x=390, y=350)
    Button(root1, bg="#FFFFFF", width=10, text="Крок 5", font="Arial 12", command=st5).place(x=510, y=350)
    Button(root1, bg="#FFFFFF", width=10, text="Крок 6", font="Arial 12", command=st6).place(x=630, y=350)
    Button(root1, bg="#FFFFFF", width=28, text="Зберегти результат у файл D.txt", font="Arial 12", command=save_result_d).place(x=30, y=430)
