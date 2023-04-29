import tkinter as tk

tela = tk.Tk()
tela.geometry('1366x768+0+0')
tela.state('zoomed')
tela['bg'] = "black"
tela.title("Agenda Eletrônica 1.0")

lblcodigo = tk.Label(tela, text ="Codigo:", bg="black", fg="blue", font=('Calibri', 12), anchor = "w")
lblcodigo.place(x = 50, y = 60, width=80, height = 25)

txtcodigo = tk.Entry(tela, width = 35, font=('Calibri', 12))
txtcodigo.place(x = 150, y = 60, width = 100, height = 25)



lblnome = tk.Label(tela, text ="nome:", bg="black", fg="blue", font=('Calibri', 12), anchor = "w")
lblnome.place(x = 50, y = 100, width=80, height = 25)

txtnome = tk.Entry(tela, width = 35, font=('Calibri', 12))
txtnome.place(x = 150, y = 100, width = 150, height = 25)


lblClassificacao = tk.Label(tela, text ="Classificação:", bg="black", fg="blue", font=('Calibri', 12), anchor = "w")
lblClassificacao.place(x = 50, y = 140, width=90, height = 25)

txtClassificacao = tk.Entry(tela, width = 35, font=('Calibri', 12))
txtClassificacao.place(x = 150, y = 140, width = 150, height = 25)


lblcelular = tk.Label(tela, text ="celular:", bg="black", fg="blue", font=('Calibri', 12), anchor = "w")
lblcelular.place(x = 50, y = 180, width=150, height = 25)

txtcelular = tk.Entry(tela, width = 40, font=('Calibri', 12))
txtcelular.place(x = 150, y = 180, width = 150, height = 25)



lblrecidencial = tk.Label(tela, text ="recidencial:", bg="black", fg="blue", font=('Calibri', 12), anchor = "w")
lblrecidencial.place(x = 50, y = 220, width=150, height = 25)

txtrecidencial = tk.Entry(tela, width = 40, font=('Calibri', 12))
txtrecidencial.place(x = 150, y = 220, width = 150, height = 25)


lblemail = tk.Label(tela, text ="Email:", bg="black", fg="blue", font=('Calibri', 12), anchor = "w")
lblemail.place(x = 50, y = 260, width=150, height = 25)

txtemail = tk.Entry(tela, width = 40, font=('Calibri', 12))
txtemail.place(x = 150, y = 260, width = 150, height = 25)


lblObservacao = tk.Label(tela, text ="Observação:", bg="black", fg="blue", font=('Calibri', 12), anchor = "w")
lblObservacao.place(x = 50, y = 300, width=150, height = 25)

txtObservacao = tk.Entry(tela, width = 40, font=('Calibri', 12))
txtObservacao.place(x = 150, y = 300, width = 350, height = 100)


btngravar = tk.Button(tela, text ="Gravar", 
                       bg ='black',foreground='white', font=('Calibri', 12, 'bold'))
btngravar.place(x = 150, y = 400, width = 65)














tela.mainloop()