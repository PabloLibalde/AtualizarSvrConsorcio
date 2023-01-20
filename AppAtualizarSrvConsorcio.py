import os
import shutil
import time
from tkinter import * # type: ignore
from tkinter import filedialog

# ------------------------------LOG-------------------------------------

LOG = open("AtualizaSrvConsorcio_Log.txt", "w+")
ROOT_DIR =os.getcwd()
ROOT_DIR = ROOT_DIR.replace("\dist","")
print(f"Caminho Raiz: {ROOT_DIR}",file=LOG)

# ----------------------------VAR GLOBAL--------------------------------

exenovo = ""
lista_pastas = []

# -----------------------------FUNCOES------------------------------------

def selecao_exe():
    #Selecionar o novo exe
    global exenovo
    exenovo = filedialog.askopenfilename(title="Selecione o Novo Exe SrvConsorcio.", 
                                        filetypes=[("exe", "*.exe"),("Todos Arquivos", "*.*")])
    exenovo = exenovo.split('/')[-1]
    


def copiar_exe_pastas ():
#Coletar a lista de nome dos arquivos
    global lista_pastas, exenovo
    for pasta in os.listdir(f"{ROOT_DIR}\\"):
        d = os.path.join(pasta)
        print(os.path.isdir(d))
        if (os.path.isdir(d)) and (('Svr' in d) or ('Srv' in d)):
            shutil.copy(f"{ROOT_DIR}\\{exenovo}",f"{ROOT_DIR}\\"+d)
            print(f"{exenovo} copiado para {ROOT_DIR}\\{d}")
            lista_pastas.append(d)
            

def atualizar_exe ():
    #Atualizar o Exe
    for lista in lista_pastas:
        os.chdir(f"{ROOT_DIR}\\{lista}")
        print(f"Atualizar {lista}?")
        x= input("Digite S para Sim e N para Não:").upper()
        if x == "S":
            for exe in os.listdir():
                if ("Srv" in exe) and (".exe" in exe) and (f"{exenovo}" not in exe):
                    os.system('taskkill /IM "' + exe + '" /F')
                    print(f"Finalizou = {ROOT_DIR}\\{lista}\\{exe}", file=LOG)
                    print(f"Finalizou = {ROOT_DIR}\\{lista}\\{exe}")
                    time.sleep(2)
                    os.remove(exe)
                    print(f"Deletou = {ROOT_DIR}\\{lista}\\{exe}", file=LOG)
                    print(f"Deletou = {ROOT_DIR}\\{lista}\\{exe}")
                    os.rename(f"{exenovo}",f"{exe}")
                    print(f"Renomeou = {ROOT_DIR}\\{lista}\\{exenovo} para {exe}", file=LOG)
                    print(f"Renomeou = {ROOT_DIR}\\{lista}\\{exenovo} para {exe}")
                    os.startfile(exe)
                    print(f"Iniciou = {ROOT_DIR}\\{lista}\\{exe}", file=LOG)
                    print(f"Iniciou = {ROOT_DIR}\\{lista}\\{exe}")
                    time.sleep(5)
                    print("-----------------------------------------------",file=LOG)
                    print("-----------------------------------------------")
        else:
            os.remove(exenovo)
            print(f"Apagou o {exenovo} da {ROOT_DIR}\\{lista}",file=LOG)
            print(f"Apagou o {exenovo} da {ROOT_DIR}\\{lista}")                    


def atualizar_explorer():
    # Atualizar Explorer
    decisao = input("S = Sim | N = Não : ").upper()
    if decisao == "S":
        os.system("taskkill /IM explorer.exe /F")
        time.sleep(2)
        os.system("start explorer.exe")

# ----------------------------------------------------------------------

#Janela
janela = Tk()
#Dimensoes Janela
largura = 500
altura = 300
#Resolucao da Tela do PC
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()
#Posicao da Janela (Definida para o Centro da tela)
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
#Propriedades da Janela
janela.title("Atualizador de pastas SrvConsorcio")
janela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))

#-------Labels
texto_orientacao = Label(janela, text="Coloque este exe na pasta raiz das pastas do SrvConsorcio, junto com o SrvConsorcio.exe novo.")


#-------Buttons
btn_selecionar = Button(janela, text="Selecionar Novo exe", command=selecao_exe)
btn_copiar = Button(janela, text="Copiar exe selecionado para as Pastas", command=copiar_exe_pastas)


#-------Grid (column=0, row=1)
texto_orientacao.grid()
btn_selecionar.grid()
btn_copiar.grid()


janela.mainloop()
