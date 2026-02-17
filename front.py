import tkinter as tk

def limpar_placeholder(event):
    if caixa_texto.get("1.0", "end-1c") == "20 Mountain\n2 BLACK LOTUS\n1 aang's journey":
        caixa_texto.delete("1.0", "end") 
        caixa_texto.config(fg="#333333")

def restaurar_placeholder(event):
    if not caixa_texto.get("1.0", "end-1c").strip():
        caixa_texto.insert("1.0", "20 Mountain\n2 BLACK LOTUS\n1 aang's journey")
        caixa_texto.config(fg="#937460")
def pegar_texto():
    # '1.0' significa: linha 1, caractere 0 (o início)
    # tk.END significa: até o final do conteúdo
    user_input = caixa_texto.get("1.0", tk.END)
    print(user_input)        
janela = tk.Tk()
janela.title("BRASIL proxy")
janela.geometry("340x320")
janela.configure(bg='#938f71')
janela.resizable(False, False)


digite = tk.Label(janela, text="Digite seu deck:", font=('Planewalker', 10, 'bold'), 
                  fg='#2c2c2c', bg='#938f71')
digite.grid(row=0, column=0, sticky="w", padx=10, pady=(15, 5))

caixa_texto = tk.Text(janela, 
                      width=42, 
                      height=10, 
                      font=("Planewalker", 11),
                      bg='#a59075', 
                      fg='#937460',
                      bd=0, 
                      highlightthickness=2,
                      highlightbackground="#7a765a", 
                      highlightcolor="#3d3b2e",
                      padx=10, 
                      pady=10)

caixa_texto.grid(row=1, column=0, padx=10, pady=10)

caixa_texto.insert("1.0", "20 Mountain\n2 BLACK LOTUS\n1 aang's journey")
caixa_texto.bind("<FocusIn>", limpar_placeholder)
caixa_texto.bind("<FocusOut>", restaurar_placeholder)

enviar_botao = tk.Button(janela,text='ENVIAR',font=('Planewalker', 10, 'bold'),
                   fg='#2c2c2c', bg='#938f71',
                   bd=0, 
                    highlightthickness=2,
                    highlightbackground="#7a765a", 
                    highlightcolor="#3d3b2e",
                    padx=10, 
                    pady=10,
                    command=pegar_texto)
enviar_botao.grid(row=2, column=0, padx=10, pady=10)

janela.mainloop()
