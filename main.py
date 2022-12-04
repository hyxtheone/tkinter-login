import os
from tkinter import ttk
from ttkthemes import themed_tk as tk
from PIL import Image, ImageTk


def logar():
    dbr = open('db.txt', 'r')
    password = senha.get()
    user = login.get()
    for line in dbr:
        if user + ':' + password == ':' or user + ':' + password == user + ':' or user + ':' + password == ':' + password:
            resultado['text'] = 'Digite um login válido!'
        elif user + ':' + password in line:
            resultado['text'] = 'Login aprovado'
            janela.destroy()

            janela2 = tk.ThemedTk()
            janela2.title('Foto')

            img = Image.open('images/result.jpg')
            tkimage = ImageTk.PhotoImage(img)
            ttk.Label(janela2, image=tkimage).pack()

            janela2.mainloop()

        else:
            resultado['text'] = 'Dados incorretos!'
    db.close()


def register():
    dba = open('db.txt', 'a')
    dbr = open('db.txt', 'r')
    password = senha.get()
    user = login.get()
    for line in dbr:
        if user + ':' + password == ':' or user + ':' + password == user + ':' or user + ':' + password == ':' + password:
            resultado['text'] = 'Digite um login válido!'
        elif user in line:
            resultado['text'] = 'Esse usuário já existe!'
        elif user + ':' + password not in line:
            dba.write('\n' + user + ':' + password)
            dba.write('\n' + user)
            resultado['text'] = 'Registrado com sucesso!'
        else:
            resultado['text'] = 'Esse login já existe!'
    dba.close()
    dbr.close()


janela = tk.ThemedTk()
janela.title('Login/Registo')
janela.geometry('275x150')
janela.resizable(False, False)
janela.get_themes()
janela.set_theme('yaru')
janela.configure(bg='white')
janela.iconbitmap('images/favicon.ico')

janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=3)


login = ttk.Entry(janela)
login.grid(column=1, row=2, sticky='E', padx=5, pady=5)

senha = ttk.Entry(janela)
senha.grid(column=1, row=3, sticky='E', padx=5, pady=5)

frase_login = ttk.Label(janela, text='User:')
frase_login.grid(column=0, row=2, sticky='W', padx=5, pady=5)

frase_senha = ttk.Label(janela, text='Senha:')
frase_senha.grid(column=0, row=3, sticky='W', padx=5, pady=5)

register_button = ttk.Button(janela, text='Registrar', command=register)
register_button.grid(column=0, row=4, sticky='W', padx=5, pady=5)

login_button = ttk.Button(janela, text='Logar', command=logar)
login_button.grid(column=1, row=4, sticky='E', padx=5, pady=5)

resultado = ttk.Label(janela, text='')
resultado.grid(column=0, row=0, padx=3, pady=5)

try:
    db = open('db.txt', 'r')
    db.close()
except FileNotFoundError:
    db = open('db.txt', 'a')
    db.write('\n')
    db.close()
    janela.destroy()
    os.startfile('main.pyw')

janela.mainloop()
