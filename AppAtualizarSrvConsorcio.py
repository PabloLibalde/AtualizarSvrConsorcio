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
selecao_pastas =[]
global label_selecao


# -----------------------------FUNCOES------------------------------------

def selecao_exe():
    #Selecionar o novo exe
    global exenovo
    exenovo = filedialog.askopenfilename(title="Selecione o Novo Exe SrvConsorcio.", 
                                        filetypes=[("exe", "*.exe"),("Todos Arquivos", "*.*")])
    exenovo = exenovo.split('/')[-1]
    
def selecao_dir():
    #Selecionar o novo exe
    global lista_pastas,ROOT_DIR,List_Srv
    List_Srv.delete(0,'end') #limpar lista
    lista_pastas.clear
    ROOT_DIR = filedialog.askdirectory(title="Selecione o diretorio Raiz da pastas dos Servidor Consorcio.")
    for pasta in os.listdir(ROOT_DIR):
        d = os.path.join(pasta)
        if (os.path.isdir(d)) and (('Svr' in d) or ('Srv' in d)):
            lista_pastas.append(d)
            List_Srv.insert(END,d)


def atualizar():
#Coletar a lista de nome dos arquivos
    global lista_pastas, exenovo,ROOT_DIR,selecao_pastas
    x=list(List_Srv.curselection())
    for d in x:
        selecao_pastas.append(lista_pastas[d])
    for d in selecao_pastas:
            shutil.copy(f"{ROOT_DIR}\\{exenovo}",f"{ROOT_DIR}\\"+d)
            print(f"{exenovo} copiado para {ROOT_DIR}\\{d}")
    
    for d in lista_pastas:
        os.chdir(f"{ROOT_DIR}\\{d}")
        for exe in os.listdir():
            if ("Srv" in exe) and (".exe" in exe) and (f"{exenovo}" not in exe):
                processos = os.popen('wmic process get description, processid').read()
                if exe in processos:
                    os.system('taskkill /IM "' + exe + '" /F')
                time.sleep(2)
                os.remove(exe)
                os.rename(f"{exenovo}",f"{exe}")
                os.startfile(exe)
                time.sleep(5)
                


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
texto_orientacao = Label(janela, text="Label1")
label_selecao = Label(janela, text='')


#-------Buttons
btn_selecionar = Button(janela, text="Selecionar Novo exe", command=selecao_exe)
btn_rootdir = Button(janela, text="Selecionar Diretorio Raiz", command=selecao_dir)
btn_copiar = Button(janela, text="Atualizar Pastas Selecionadas", command=atualizar)

#-------Listbox
List_Srv = Listbox(janela,selectmode=MULTIPLE)

#-------Grid (column=0, row=1)
texto_orientacao.grid()
btn_selecionar.grid()
btn_copiar.grid()
btn_rootdir.grid()
List_Srv.grid()
label_selecao.grid()

janela.mainloop()
