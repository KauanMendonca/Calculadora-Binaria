    # Tkinter
import tkinter
from tkinter import *
from tkinter import ttk

    # Cores 
co0 = "#444466"  # Preta
co1 = "#feffff"  # Branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5=  "#e89613"  # laranja

janela = Tk()
janela.title('')
janela.geometry('400x310')
janela.configure(bg=co1)

style = ttk.Style()
style.theme_use('clam')
ttk.Separator(janela,orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=190)

# divindo a janela em dois frames

frame_cima = Frame(janela, width=400, height=60, bg=co1, pady=0, padx=0)
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=400, height=300, bg=co1, pady=12, padx=20)
frame_baixo.grid(row=2, column=0, sticky=NW)

# Configurando frame cima
app_nome = Label(frame_cima, text="Conversor de base numerica", relief=FLAT, anchor="center", font=('System 20'), bg=co2, fg=co1)
app_nome.place(x=10, y=15)

# Frame Baixo
bases = ['BINARIO', 'OCTAL', 'DECIMAL', 'HEXADECIMAL']

combo = ttk.Combobox(frame_baixo, width=12, justify=CENTER, font=('Ivy 12 bold'))
combo['values'] = (bases)
combo.place(x=35, y=10)

e_valor = Entry(frame_baixo, width=9, justify='center', font=("",13), highlightthickness=1, relief='solid')
e_valor.place(x=160,y=10)

b_converter = Button(frame_baixo, text="CONVERTER", relief=RAISED,overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co4)
b_converter.place(x=247, y=10)

l_binario = Label(frame_baixo, text="BINARIO",width=12, relief=FLAT, anchor="nw", font=('Verdana 13'), bg=co5, fg=co1)
l_binario.place(x=35, y=60)
l_binario = Label(frame_baixo, text="",width=13,relief=FLAT, anchor="center", font=('Verdana 13'), fg=co4)
l_binario.place(x=170, y=60)

l_octal = Label(frame_baixo, text="OCTAL",width=12, relief=FLAT, anchor="nw", font=('Verdana 13'), bg=co5, fg=co1)
l_octal.place(x=35, y=100)
l_octal = Label(frame_baixo, text="",width=13,relief=FLAT, anchor="center", font=('Verdana 13'), fg=co4)
l_octal.place(x=170, y=100)

l_decimal = Label(frame_baixo, text="DECIMAL",width=12, relief=FLAT, anchor="nw", font=('Verdana 13'), bg=co5, fg=co1)
l_decimal.place(x=35, y=140)
l_decimal = Label(frame_baixo, text="",width=13,relief=FLAT, anchor="center", font=('Verdana 13'), fg=co4)
l_decimal.place(x=170, y=140)

l_hexadecimal = Label(frame_baixo, text="HEXADECIMAL",width=12, relief=FLAT, anchor="nw", font=('Verdana 13'), bg=co5, fg=co1)
l_hexadecimal.place(x=35, y=180)
l_hexadecimal = Label(frame_baixo, text="",width=13,relief=FLAT, anchor="center", font=('Verdana 13'), fg=co4)
l_hexadecimal.place(x=170, y=180)


janela.mainloop()
