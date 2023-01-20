import os
import shutil
import time
from tkinter import * # type: ignore


LOG = open("AtualizaSrvConsorcio_Log.txt", "w+")
ROOT_DIR =os.getcwd()
ROOT_DIR = ROOT_DIR.replace("\dist","")
print(f"Caminho Raiz: {ROOT_DIR}",file=LOG)

exenovo = "SrvConsorcioMunicipal.exe"

lista_pastas = []
def copiar_exe_pastas ():
#Coletar a lista de nome dos arquivos
    for pasta in os.listdir(f"{ROOT_DIR}\\"):
        d = os.path.join(pasta)
        if (os.path.isdir(d)) and ('Svr' in d) or ('Srv' in d):
            shutil.copy(f"{ROOT_DIR}\\{exenovo}",f"{ROOT_DIR}\\"+d)
            print(f"{exenovo} copiado para {ROOT_DIR}\\{d}", file=LOG)
            print(f"{exenovo} copiado para {ROOT_DIR}\\{d}")
            lista_pastas.append(d)
            
print("-----------------------------------------------")            


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

print("!!!!Atualização Concluida!!!!",file=LOG)
print("!!!!Atualização Concluida!!!!")
print("-----------------------------------------------")
print("Reiniciar o explorer.exe, afins de limpar de recarregar a bandeja dos icones?")

def atualizar_explorer():
    # Atualizar Explorer
    decisao = input("S = Sim | N = Não : ").upper()
    if decisao == "S":
        os.system("taskkill /IM explorer.exe /F")
        time.sleep(2)
        os.system("start explorer.exe")

"""
#Janela Interface
janela = Tk()
janela.title("Automacao Atualização SrvConsorcio")

texto_orientacao = Label(janela, text="Coloque este exe na pasta raiz das pastas do SrvConsorcio, junto com o SrvConsorcio.exe novo.")
texto_orientacao.grid(column=0, row=0)

botao = Button(janela, text="Copiar SrvConsorcio.exe para as Pastas", command=copiar_exe_pastas)
botao.grid(column=0, row=1)


janela.mainloop()
"""