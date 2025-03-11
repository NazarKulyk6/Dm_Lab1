from main import *
from tkinter import *
from PIL import Image, ImageTk


def third_win():
    root2 = Toplevel()
    root2.title("Вікно 3")
    root2.geometry("500x350")

    gif_path = "17xe.gif"
    gif = Image.open(gif_path)

    target_size = (500, 350)

    frames = []
    try:
        while True:
            frame = gif.copy().convert("RGBA").resize(target_size, Image.LANCZOS)  # Масштабування
            frames.append(ImageTk.PhotoImage(frame))
            gif.seek(len(frames))
    except EOFError:
        pass

    gif.close()

    bg_label = Label(root2)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def update_frame(index=0):
        frame = frames[index]
        bg_label.config(image=frame)
        root2.after(100, update_frame, (index + 1) % len(frames))

    update_frame()

    def st1():
        result = step1_simple(a, b, u)
        Label(root2, bg="#0e427d", text=str(result), font="Arial 12").place(x=130, y=100)

    def st2():
        result = step2_simple(a, b, c, u)
        Label(root2, bg="#0e427d", text=str(result), font="Arial 12").place(x=130, y=125)
        Label(root2, bg="#0e427d", text=str(result), font="Arial 12").place(x=70, y=250)

    def save_result_d_simple():
        result = step2_simple(a, b, c, u)
        save_res = open("D_simple.txt", "w+")
        save_res.write(str(result))
        save_res.close()

    Label(root2, bg="#0e427d", text="A:", font="Arial 12").place(x=10, y=10)
    Label(root2, bg="#0e427d", text=str(a), font="Arial 12").place(x=100, y=10)
    Label(root2, bg="#0e427d", text="B:", font="Arial 12").place(x=10, y=35)
    Label(root2, bg="#0e427d", text=str(b), font="Arial 12").place(x=100, y=35)
    Label(root2, bg="#0e427d", text="C:", font="Arial 12").place(x=10, y=60)
    Label(root2, bg="#0e427d", text=str(c), font="Arial 12").place(x=100, y=60)
    Label(root2, bg="#0e427d", text="¬C:", font="Arial 12").place(x=10, y=60)
    Label(root2, bg="#0e427d", text=str(u-c), font="Arial 12").place(x=100, y=60)
    Label(root2, bg="#0e427d", text="A △ B:", font="Arial 12").place(x=10, y=100)
    Label(root2, bg="#0e427d", text="(A △ B) ∩ ¬C:", font="Arial 12").place(x=10, y=125)
    Label(root2, bg="#0e427d", text="D = ", font="Arial 12").place(x=30, y=250)

    Button(root2, bg="#4274ad", width=10, text="Крок 1", font="Arial 12", command=st1, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=30, y=200)
    Button(root2, bg="#4274ad", width=10, text="Крок 2", font="Arial 12", command=st2, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=150, y=200)

    Button(root2, bg="#4274ad", width=30, text="Зберегти результат у файл D_simple.txt", font="Arial 12", command=save_result_d_simple, highlightbackground="#051e3b", highlightthickness=2, bd=0).place(x=30, y=280)
