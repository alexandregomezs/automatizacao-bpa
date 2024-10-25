import pyautogui
from time import sleep

class AutomationBpa:

    sleep(5)

    def dado1():
        pyautogui.hotkey('alt', 'tab')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.hotkey('alt', 'tab')
        pyautogui.hotkey('ctrl', 'v')

    def dado2():
        pyautogui.hotkey('alt', 'tab')
        pyautogui.press('right')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.hotkey('alt', 'tab')
        pyautogui.hotkey('ctrl', 'v')

    def dado3():
        pyautogui.hotkey('alt', 'tab')
        pyautogui.press('right')
        pyautogui.press('right')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.hotkey('alt', 'tab')
        pyautogui.hotkey('ctrl', 'v')

    def double_tab():
        pyautogui.press('tab')
        pyautogui.press('tab')
        
    quantidade_linhas = 1
        
    
    for i in range(1, quantidade_linhas+1):
        

        #linha 01
        dado1()
        double_tab()
        dado2()
        pyautogui.press('tab')
        pyautogui.press('f') #Atenção: definir "f" para feminino e "m" para masculino
        pyautogui.press('tab')

        #linha 02
        dado3()
        double_tab()
        pyautogui.press('3')
        pyautogui.press('tab')

        #linha 03
        dado2()
        double_tab()
        pyautogui.write('81')
        pyautogui.press('tab')

        #linha 04
        dado2()
        pyautogui.press('tab')
        dado2() 
        double_tab()


        #linha 05
        dado2()
        double_tab()
        pyautogui.press('tab')

        #linha 06
        dado2()
        pyautogui.press('tab')
        dado2()
        pyautogui.press('1')
        double_tab()
        pyautogui.press('tab')
        
        #linha 07      
        pyautogui.write('Z000')
        pyautogui.press('tab')
        pyautogui.press('1')
        
        #Adicionar na folha
        double_tab()
        pyautogui.press('enter')
        
        #Alocar para a próxima pessoa
        pyautogui.hotkey('alt', 'tab')
        pyautogui.press('down')                    
        pyautogui.press('home')
        
        
        #mudar para o BPA para iniciar novamente o processo
        pyautogui.hotkey('alt', 'tab')
        

AutomationBpa()