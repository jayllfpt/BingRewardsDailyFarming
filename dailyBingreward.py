import pyautogui as jay
from time import sleep
import random, string

def randomword(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

def edgeW(number):
        for i in range(35):
                sleep(0.5)
                print('Edge PC' + str(number) + ': search:' + str(i))

                with jay.hold('win'):
                        jay.press(number)
                sleep(1)
                with jay.hold('ctrl'):
                        jay.press('t')
                sleep(0.5)

                jay.write(randomword(random.randint(5, 10)))
                jay.press('enter')
                sleep(2)
                with jay.hold('alt'):
                        jay.press('f4')

def removeAd(number):
        with jay.hold('win'):
                jay.press(number)
        sleep(10)
        with jay.hold('alt'):
                jay.press('f4')
        

def edgeA(number):
        # open android browser
        with jay.hold('win'):
                jay.press(number)
        sleep(15)

        with jay.hold('ctrl'):
                jay.press('o')
        sleep(8)
        with jay.hold('alt'):
                jay.press('o')
        for i in range(25):
                sleep(2)
                print('Edge Mobile' + str(number) + ': search:' + str(i))
                with jay.hold('alt'):
                        jay.press('i')
                sleep(0.5)
                jay.press('backspace')
                jay.write(randomword(random.randint(1, 3)))
                jay.press('enter')
                
        with jay.hold('alt'):
                jay.press('f4')
        
edgeW('1')
edgeW('3')

edgeA('4')
edgeA('5')