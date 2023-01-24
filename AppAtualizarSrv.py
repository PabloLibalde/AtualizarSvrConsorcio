from logging import CRITICAL,ERROR,WARNING,INFO,DEBUG
from logging import basicConfig
from logging import critical,error,warning,info,debug
from logging import FileHandler,StreamHandler
import os
import shutil
import time
from tkinter import * # type: ignore
from tkinter import filedialog, messagebox

# ------------------------------LOG-------------------------------------
basicConfig(
    level=DEBUG,
    filename='AppAtualizarSrv.log',
    filemode='a',
    format='%(levelname)s:%(asctime)s:%(message)s',
)


ROOT_DIR =os.getcwd()



# ----------------------------VAR GLOBAL--------------------------------

exenovo = ""
lista_pastas = []
selecao_pastas =[]

info("------------------- Inicio App -------------------")
# -----------------------------FUNCOES------------------------------------

def selecao_exe():
    #Selecionar o novo exe
    try:
        global exenovo
        exenovo = filedialog.askopenfilename(title="Selecione o Novo Exe SrvConsorcio.", 
                                            filetypes=[("exe", "*.exe")])
        exenovo = exenovo.split('/')[-1]
        messagebox.showinfo("Informação",f"Exe Selecionado {exenovo}")
    except Exception as erro:
        error(f"def selecao_exe : {erro}")
        messagebox.showerror("Erro","Erro ao Selecionar EXE")

    
def selecao_dir():
    try:
        #Selecionar o novo exe
        global lista_pastas,ROOT_DIR,List_Srv
        List_Srv.delete(0,'end') #limpar lista
        lista_pastas.clear
        ROOT_DIR = filedialog.askdirectory(title="Selecione o diretorio Raiz da pastas dos Servidor Consorcio.")
        os.chdir(ROOT_DIR)
        for pasta in os.listdir():
            if os.path.isdir(pasta):
                if ("Svr" in pasta) or ("Srv" in pasta):
                    lista_pastas.append(pasta)
                    List_Srv.insert(END,pasta)
        info(f"Pasta(s) {lista_pastas} Encontrada(s)")
        messagebox.showinfo("Informação",f"Selecione as pastas da Lista que deseja atualziar. Depois clique em 'Atualizar Pastas Selecionadas'")
    except Exception as erro:
        error(f"def selecao_dir: {erro}")
        messagebox.showerror("Erro","Erro ao Selecionar Diretorio Raiz")


def atualizar():
#Coletar a lista de nome dos arquivos
    try:
        global lista_pastas, exenovo,ROOT_DIR,selecao_pastas
        x=list(List_Srv.curselection())
            
        for d in x:
            selecao_pastas.append(lista_pastas[d])
        info(f"Pastas {selecao_pastas} Selecionadas")    
        
        for d in selecao_pastas:
                shutil.copy(f"{ROOT_DIR}\\{exenovo}",f"{ROOT_DIR}\\"+d)
                info(f"Copiado {ROOT_DIR}\\{exenovo} para {ROOT_DIR}\\{d}")


        for d in lista_pastas:
            os.chdir(f"{ROOT_DIR}\\{d}")
            
            for exe in os.listdir():
                if ("Srv" in exe) and (".exe" in exe) and (f"{exenovo}" not in exe):
                    processos = os.popen('wmic process get description, processid').read()
                    if exe in processos:
                        os.system('taskkill /IM "' + exe + '" /F')
                        info(f"Finalizado o processo {exe}.")
                    else:
                        info(f"O {exe} não estava em execução")
                    time.sleep(2)
                    os.remove(exe)
                    info(f"Removido {ROOT_DIR}\\{d}\\{exe}. ")
                    os.rename(f"{exenovo}",f"{exe}")
                    info(f"Renomeado {ROOT_DIR}\\{d}\\{exenovo} para {exe}. ")
                    os.startfile(exe)
                    info(f"Iniciado {ROOT_DIR}\\{d}\\{exe}. ")
                    time.sleep(5)
        messagebox.showinfo("Informação",f"O(s) .exe foram atualizados com Sucesso!")
    except Exception as erro:
        error(f"def atualizar: {erro}")
        messagebox.showerror("Erro","Erro ao Atualizar EXE")            


def atualizar_explorer():
    try:
    # Atualizar Explorer
        os.system("taskkill /IM explorer.exe /F")
        time.sleep(2)
        os.system("start explorer.exe")
        info(f"Reiniciado Explorer. ")
        messagebox.showinfo("Informação",f"Explorere Atualizado!")
    except Exception as erro:
        error(f"def atualizar_explorer: {erro}") 
        messagebox.showerror("Erro","Erro ao Atualizar Explorer")
# ----------------------------------------------------------------------

#Janela
janela = Tk()
#Dimensoes Janela
largura = 300
altura = 650
#Resolucao da Tela do PC
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()
#Posicao da Janela (Definida para o Centro da tela)
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2 - 20
#Propriedades da Janela
janela.title("RGSystem")
janela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))


#-------Labels

texto_orientacao = Label(janela,
                            text="Atualizador Srv\n(Consorcio/Saude)"
                            )

texto_orientacao_btn_atualizar = Label(janela,
                            text="Selecione a(s) pasta(s) clicando nela(s)."
                            )



#-------Buttons
btn_selecionar = Button(janela,
                        width=25,
                        text="Selecionar Novo exe", 
                        command=selecao_exe
                        )

btn_rootdir = Button(janela,
                        width=25,
                        text="Selecionar Diretorio Raiz", 
                        command=selecao_dir
                        )

btn_atualizar = Button(janela,
                        width=25,
                        text="Atualizar Pastas Selecionadas", 
                        command=atualizar
                        )

btn_atualizar_explorer = Button(janela,
                        width=25,
                        text="Atualizar Exeplorer", 
                        command=atualizar_explorer
                        )

#-------Listbox
List_Srv = Listbox(janela,
                    height=30,
                    width=30,
                    selectmode=MULTIPLE
                    )

#-------pack (column=0, row=1)

texto_orientacao.pack()
btn_selecionar.pack()
btn_rootdir.pack()
texto_orientacao_btn_atualizar.pack()
List_Srv.pack()
btn_atualizar.pack()
btn_atualizar_explorer.pack()

janela.mainloop()
