from tkinter import *
import pyperclip

root = Tk()
root.title("Morse Code Generator")
root.geometry("800x500")
root.resizable(0, 0)
root.configure(bg="black")


# Functions
def get_code():
    text = input_text.get()
    plain = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,:-'/?!();-a$ ")
    morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
             '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--', '....-', '.....', '-....',
             '--...', '---..', '---.', '-----', '.-.-.-', '--..--', '---...', '-....-', '.----.', '-..-.', '..--..', '-.-.--', '-.--.', '-.--.-', '-.-.-.', '-...-',
             '.--.-.', '...-..-', '/']
    code = dict(zip(plain, morse))

    text = text.upper()
    mtext = ""

    for ch in text:
        for p, m in code.items():
            if ch == p:
                mtext += m + " "
    output_text.delete(0, END)
    output_text.insert(END, mtext)


def clear1_code():
    input_text.delete(0, END)


def copy_code():
    pyperclip.copy(output_text.get())


def clear_code():
    output_text.delete(0, END)


# Labels
Label(root, text="Morse Code Generator", font="Helvetica 32 bold underline", fg="yellow", bg="black").pack()
Label(root, text="↓Enter Text↓", font=("Helvetica", 17, "bold"), fg="yellow", bg="black").place(x=325, y=105)
Label(root, text="↓Output↓", font=("Helvetica", 17, "bold"), fg="yellow", bg="black").place(x=340, y=260)
Label(root, text="Program@Paras4902", font=("Helvetica", 17, "bold"), fg="yellow", bg="black").pack(side=BOTTOM, anchor=E)


# Entries
input_text = Entry(root, font=("Helvetica", 25, "bold"), bd=10)
input_text.place(x=70, y=150, width=660)
output_text = Entry(root, font=("Helvetica", 25, "bold"), bd=10)
output_text.place(x=70, y=320, width=660)


# Buttons
Button(root, text="Clear", font=("Helvetica", 15, "bold"), bd=5, bg="grey", fg="yellow", command=clear_code).place(x=70, y=380)
Button(root, text="Copy", font=("Helvetica", 15, "bold"), bg="grey", fg="yellow", bd=5, command=copy_code).place(x=657, y=380)
Button(root, text="Clear", font=("Helvetica", 15, "bold"), bg="grey", fg="yellow", bd=5, command=clear1_code).place(x=70, y=210)
Button(root, text="Get Code", font=("Helvetica", 15, "bold"), bg="grey", fg="yellow", bd=5, command=get_code).place(x=617, y=210)
root.mainloop()
