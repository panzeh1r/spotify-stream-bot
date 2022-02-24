import pyautogui as gui
import time

counter = 1
talep = int(input("Kaç bot basılsın: "))

time.sleep(5)



with open("usernames.txt", "r") as f1, open("passwords.txt", "r") as f2:
    while counter <= talep:
        f1_contents = f1.readline()
        f2_contents = f2.readline()
        gui.click(296, 47, clicks=3, interval=0.25)
        gui.typewrite("https://accounts.spotify.com/tr/login/?continue=https%3A//open.spotify.com/__noul__%3Fl2l%3D1%26nd%3D1&_locale=tr-TR")
        gui.press("enter")
        time.sleep(3)
        gui.click(527, 543, clicks=3, interval=0.25)
        gui.typewrite(f1_contents)
        gui.click(527, 634)
        gui.typewrite(f2_contents)
        gui.press("enter")
        time.sleep(10)
        image = gui.locateOnScreen("ss.png")
        image

        if not image:
            gui.click(118, 253)
            time.sleep(5)
            gui.click(118, 253)
            time.sleep(3)
            gui.typewrite("raku kirmizi mavi")
            time.sleep(5)
            gui.click(660, 405)
            time.sleep(40)
            gui.click(1275, 131)
            time.sleep(2)
            gui.click(1197, 299)
            time.sleep(5)
            counter = counter + 1

        else:
            counter = counter + 1


       


