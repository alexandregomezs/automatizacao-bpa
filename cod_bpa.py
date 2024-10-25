import pyautogui
from time import sleep
import requests
import keyboard
import threading

# Variável de controle para parar a automação
parar_automacao = False

class RequestBpa:
    def enviarRequest(self):
        url = 'https://api.telegram.org/bot7476537425:AAGieqlloUcAu1ilu3JxmiVhdWywOC-cnag/sendMessage?chat_id=-4548620708&text="Alerta, Automação BPA terminou!!"'
        requests.get(url)
        print("Mensagem enviada")

class AutomationBpa:
    enviarMensagem = RequestBpa()

    # Adiciona uma verificação de parada em cada método de ação
    @staticmethod
    def verificar_parada():
        global parar_automacao
        if parar_automacao:
            print("Automação interrompida!")
            raise Exception("Parada solicitada pelo usuário.")

    @staticmethod
    def dado1():
        AutomationBpa.verificar_parada()
        pyautogui.hotkey("alt", "tab")
        sleep(0.2)
        pyautogui.hotkey("ctrl", "c")
        sleep(0.2)
        pyautogui.hotkey("alt", "tab")
        sleep(0.2)
        pyautogui.hotkey("ctrl", "v")
        sleep(0.2)

    @staticmethod
    def dado2():
        AutomationBpa.verificar_parada()
        pyautogui.hotkey("alt", "tab")
        sleep(0.2)
        pyautogui.press("right")
        sleep(0.2)
        pyautogui.hotkey("ctrl", "c")
        sleep(0.2)
        pyautogui.hotkey("alt", "tab")
        sleep(0.2)
        pyautogui.hotkey("ctrl", "v")
        sleep(0.2)

    @staticmethod
    def dado3():
        AutomationBpa.verificar_parada()
        pyautogui.hotkey("alt", "tab")
        sleep(0.3)
        pyautogui.press("right")
        sleep(0.3)
        pyautogui.press("right")
        sleep(0.3)
        pyautogui.hotkey("ctrl", "c")
        sleep(0.3)
        pyautogui.hotkey("alt", "tab")
        sleep(0.3)
        pyautogui.hotkey("ctrl", "v")
        sleep(0.3)

    @staticmethod
    def double_tab():
        AutomationBpa.verificar_parada()
        pyautogui.press("tab")
        sleep(0.3)
        pyautogui.press("tab")
        sleep(0.3)

# Função que monitora a tecla ESC para interromper
def monitorar_esc():
    global parar_automacao
    while True:
        if keyboard.is_pressed("esc"):
            parar_automacao = True
            print("Parada solicitada! Encerrando a automação.")
            break
        sleep(0.1)

# Função principal da automação
def executar_automacao():
    global parar_automacao
    print("Iniciando a automação do BPA")

    # Thread para monitorar ESC
    threading.Thread(target=monitorar_esc, daemon=True).start()

    while not parar_automacao:
        quant_linhas = str(input("Deseja digitar 10 linhas? (S/N/C) ")).upper()
        
        if quant_linhas == "N":
            quantidade_linhas = int(input("Digite a quantidade de linhas restantes: "))
        elif quant_linhas == "S":
            quantidade_linhas = 10
        elif quant_linhas == "C":
            print("Encerrando...")
            break
        else:
            print("Opção inválida! Tente novamente.")
            continue

        sexo_digitado = str(input("Qual sexo será digitado primeiro (F/M): ")).upper()
        iszi = str(input("É exame de ZIE ou ZI2? (S/N): ")).upper()

        exameIsZi = "003" if iszi == "N" else "009" if iszi == "S" else None
        if exameIsZi is None:
            print("Opção inválida para exame! Tente novamente.")
            continue

        try:
            for i in range(quantidade_linhas):
                if parar_automacao: break

                print('Iniciando contagem de 5 segundos...')
                sleep(5)
                if parar_automacao: break

                # linha 01
                AutomationBpa.dado1()
                AutomationBpa.double_tab()
                AutomationBpa.dado2()
                pyautogui.press("tab")
                pyautogui.press("backspace")
                pyautogui.press(sexo_digitado)
                pyautogui.press("tab")

                # linha 02
                AutomationBpa.dado3()
                AutomationBpa.double_tab()
                pyautogui.press("3")
                pyautogui.press("tab")

                # linha 03
                AutomationBpa.dado2()
                AutomationBpa.double_tab()
                pyautogui.write("81")
                pyautogui.press("tab")

                # linha 04
                AutomationBpa.dado2()
                pyautogui.press("tab")
                AutomationBpa.dado2()
                AutomationBpa.double_tab()

                # linha 05
                AutomationBpa.dado2()
                pyautogui.press("f7")

                # linha 06
                AutomationBpa.dado2()
                pyautogui.press("tab")
                AutomationBpa.dado2()
                pyautogui.press("1")
                pyautogui.press("tab")
                pyautogui.press("backspace")
                pyautogui.write("145")
                pyautogui.press("tab")
                pyautogui.press("backspace")
                pyautogui.write(exameIsZi)
                pyautogui.press("tab")

                # linha 07
                pyautogui.write("Z000")
                pyautogui.press("tab")
                pyautogui.press("1")

                # Adicionar na folha
                AutomationBpa.double_tab()
                pyautogui.press("enter")

                # Alocar para a próxima pessoa
                pyautogui.hotkey("alt", "tab")
                pyautogui.press("down")
                pyautogui.press("home")
                pyautogui.hotkey("alt", "tab")
                pyautogui.press("f6")
            
            if parar_automacao: break

            AutomationBpa.enviarMensagem.enviarRequest()

            opc = str(input("Deseja Continuar?")).upper()
            if opc == "N":
                print("Encerrando...")
                break

        except Exception as e:
            print(str(e))
            break

# Executa a automação
executar_automacao()