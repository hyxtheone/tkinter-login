import os
from tkinter import ttk
from ttkthemes import themed_tk as tk
from PIL import Image, ImageTk
from hashlib import sha256


def logar():
    dbr = open('db.txt', 'r')
    password = senha.get()
    user = login.get()
    for line in dbr:
        if user + ':' + password == ':' or user + ':' + password == user + ':' or user + ':' + password == ':' + password:
            resultado['text'] = 'Digite um login válido!'
        elif criptografar(user, password) in line:
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
    if user + ':' + password == ':' or user + ':' + password == user + ':' or user + ':' + password == ':' + password:
        resultado['text'] = 'Digite um login válido!'
    else:
        if criptografar(user, '') in dbr:
            resultado['text'] = 'Esse usuário já existe!'
        else:
            resultado['text'] = 'Registrado com sucesso!'
            dba.write('\n' + criptografar(user, password))
            dba.write('\n' + criptografar(user, ''))
    dba.close()
    dbr.close()


def criptografar(user, password):
    senha_final = user + ':' + password
    hash_senha_final = sha256(senha_final.encode())
    return hash_senha_final.hexdigest()


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
