from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile, askopenfile

root = Tk()
root.title("Lab 6-7")

root.minsize(width=700, height=500)

text = Text(root, width=250, height=500)

scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)

text.pack()
FILE_NAME = "test2.txt"


def new_file():
    global FILE_NAME
    text.delete("1.0", END)
    FILE_NAME = "test2.txt"


def save_file():
    data = text.get("1.0", END)
    out = open(FILE_NAME, "w")
    out.write(data)
    out.close()


def save_as():
    out = asksaveasfile(mode="w", defaultextension="txt")
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        return


def open_file():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
        return
    FILE_NAME = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)


def info():
    messagebox.showinfo("Info", "Made by Filonenko wp")


def task22():
    data = text.get("1.0",END)
    num = int(data, 8)
    newNum = ''
    while num > 0:
        newNum = str(num % 5) + newNum
        num //= 5
    text.delete('1.0', END)
    text.insert("1.0",newNum)


def task34():
    data = text.get("1.0", END)
    a = data.upper()
    b = a.split()
    l = len(b)
    messagebox.showinfo("Result", l)


def task58():
    board = [['0'] * 8 for _ in range(8)]

    dct = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

    data = text.get("1.0", END)

    v = data[0]
    g = int(data[1])

    board[dct[v]][g - 1] = 'Q'

    for i in range(ord('a'), ord('h') + 1):
        for j in range(1, 9):
            if (i != ord(v) or j != g) and ((i == ord(v) or j == g) or (abs(i - ord(v)) == abs(j - g))):
                board[dct[chr(i)]][j - 1] = '×'

    board = list(zip(*board))
    data1 = []
    for x in reversed(board):
        data1.append(' '.join(x) + "\n")
    y = 1.0
    for x in range(len(data1)):
        text.insert(y, data1[x])
        y += 1


menu_bar = Menu()
file_menu = Menu(menu_bar)

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Info", command=info)
menu_bar.add_cascade(label="Task22", command=task22)
menu_bar.add_cascade(label="Task34", command=task34)
menu_bar.add_cascade(label="Task58", command=task58)


file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save as", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
root.config(menu=menu_bar)
root.mainloop()
