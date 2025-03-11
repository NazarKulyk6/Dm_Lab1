from main import *
from tkinter import *
from PIL import Image, ImageTk


def second_win():
    root1 = Toplevel()
    root1.title("Вікно 2")
    root1.geometry("760x500")

    gif_path = "17xe.gif"
    gif = Image.open(gif_path)

    target_size = (760, 500)

    frames = []
    try:
        while True:
            frame = gif.copy().convert("RGBA").resize(target_size, Image.LANCZOS)  # Масштабування
            frames.append(ImageTk.PhotoImage(frame))
            gif.seek(len(frames))
    except EOFError:
        pass

    gif.close()

    bg_label = Label(root1)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def update_frame(index=0):
        frame = frames[index]
        bg_label.config(image=frame)
        root1.after(100, update_frame, (index + 1) % len(frames))

    update_frame()

    def st1():
        result = step1(a, b, u)
        Label(root1, bg="#0e427d", text=str(result), font="Arial 12").place(x=340, y=160)

    def st2():
        result = step2(a, b, u)
        Label(root1, bg="#0e427d", text=str(result), font="Arial 12").place(x=340, y=185)

    def st3():
        result = step3(b, c, u)
        Label(root1, bg="#0e427d", text=str(result), font="Arial 12").place(x=340, y=210)

    def st4():
        result = step4(a, b, u)
        Label(root1, bg="#0e427d", text=str(result), font="Arial 12").place(x=340, y=235)

    def st5():
        result = step5(b, c, u)
        Label(root1, bg="#0e427d", text=str(result), font="Arial 12").place(x=340, y=260)

    def st6():
        result = step6(a, b, c, u)
        Label(root1, bg="#0e427d", text=str(result), font="Arial 12").place(x=340, y=285)
        Label(root1, bg="#0e427d", text=str(result), font="Arial 12").place(x=70, y=400)

    def save_result_d():
        result = step6(a, b, c, u)
        save_res = open("D.txt", "w+")
        save_res.write(str(result))
        save_res.close()

    Label(root1, bg="#0e427d", text="A:", font="Arial 12").place(x=10, y=10)
    Label(root1, bg="#0e427d", text=str(a), font="Arial 12").place(x=100, y=10)
    Label(root1, bg="#0e427d", text="B:", font="Arial 12").place(x=10, y=35)
    Label(root1, bg="#0e427d", text=str(b), font="Arial 12").place(x=100, y=35)
    Label(root1, bg="#0e427d", text="C:", font="Arial 12").place(x=10, y=60)
    Label(root1, bg="#0e427d", text=str(c), font="Arial 12").place(x=100, y=60)
    Label(root1, bg="#0e427d", text="¬A:", font="Arial 12").place(x=10, y=85)
    Label(root1, bg="#0e427d", text=str(u-a), font="Arial 12").place(x=100, y=85)
    Label(root1, bg="#0e427d", text="¬B:", font="Arial 12").place(x=10, y=110)
    Label(root1, bg="#0e427d", text=str(u-b), font="Arial 12").place(x=100, y=110)
    Label(root1, bg="#0e427d", text="¬C:", font="Arial 12").place(x=10, y=135)
    Label(root1, bg="#0e427d", text=str(u-c), font="Arial 12").place(x=100, y=135)
    Label(root1, bg="#0e427d", text="A ∩ ¬B:", font="Arial 12").place(x=10, y=160)
    Label(root1, bg="#0e427d", text="¬A ∩ B:", font="Arial 12").place(x=10, y=185)
    Label(root1, bg="#0e427d", text="¬C ∪ B:", font="Arial 12").place(x=10, y=210)
    Label(root1, bg="#0e427d", text="(A ∩ ¬B) ∪ (¬A ∩ B):", font="Arial 12").place(x=10, y=235)
    Label(root1, bg="#0e427d", text="¬C ∩ (¬С ∪ B):", font="Arial 12").place(x=10, y=260)
    Label(root1, bg="#0e427d", text="((A ∩ ¬B) ∪ (¬A ∩ B)) ∩ (¬C ∩ (¬С ∪ B)):", font="Arial 12").place(x=10, y=285)
    Label(root1, bg="#0e427d", text="D = ", font="Arial 12").place(x=30, y=400)

    Button(root1, bg="#4274ad", width=10, text="Крок 1", font="Arial 12", command=st1, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=30, y=350)
    Button(root1, bg="#4274ad", width=10, text="Крок 2", font="Arial 12", command=st2, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=150, y=350)
    Button(root1, bg="#4274ad", width=10, text="Крок 3", font="Arial 12", command=st3, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=270, y=350)
    Button(root1, bg="#4274ad", width=10, text="Крок 4", font="Arial 12", command=st4, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=390, y=350)
    Button(root1, bg="#4274ad", width=10, text="Крок 5", font="Arial 12", command=st5, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=510, y=350)
    Button(root1, bg="#4274ad", width=10, text="Крок 6", font="Arial 12", command=st6, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=630, y=350)
    Button(root1, bg="#4274ad", width=28, text="Зберегти результат у файл D.txt", font="Arial 12", command=save_result_d, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=30, y=430)
