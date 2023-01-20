from tkinter import * #type: ignore

#Janela
menu_inicial = Tk()
#Dimensoes Janela
largura = 500
altura = 300
#Resolucao da Tela do PC
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()
#Posicao da Janela (Definida para o Centro da tela)
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
#Propriedades da Janela
menu_inicial.title("Atualizador de pastas SrvConsorcio")
menu_inicial.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))

#Botoes
btn_selecionar= Button(menu_inicial, text="Selecionar")
btn_selecionar.pack()


menu_inicial.mainloop()