import tkinter as tk

janela = tk.Tk()

var_promocoes = tk.IntVar()
checkbox_promocoes = tk.Checkbutton(text = "Deseja receber e-mail promocionais", variable = var_promocoes)
checkbox_promocoes.grid(row=0,column=0)

var_politicas = tk.IntVar()
checkbox_politicas = tk.Checkbutton(text="Aceitar termos de Uso e Politicas de Privacidade",variable = var_politicas)
checkbox_politicas.grid(row = 1,column=0)

def enviar():
    if var_promocoes.get():
        print('Usuario deseja receber promoções')
    else:
        print('Usuario NÃO deseja promoções')
    if var_politicas.get():
        print("Usuario concodou com Termos de Uso e Politicas de Privacidade")
    else:
        print("Usario não concordou")
    
botao_enviar = tk.Button (text = "Enviar",command=enviar)
botao_enviar.grid(row=1,column = 0)
    
janela.mainloop()