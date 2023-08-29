import pyautogui as pg
import time

print('Zapusk sdelan')


def sendmessage():
    time.sleep(3)

    for i in range(70):
        pg.typewrite('DEN DOBRIY')
        pg.press('enter')


sendmessage()
