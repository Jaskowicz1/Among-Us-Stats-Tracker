import time

import cv2
import mss
import numpy
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

wins = 0
loses = 0

hasRead = False

with open("wins.txt", "r") as file:
    data = file.read().replace('\n', '')

    dataSplit = data.split(": ")
    if(len(dataSplit) > 1):
        wins = int(dataSplit[1])

with open("lose.txt", "r") as file:
    data = file.read().replace('\n', '')

    dataSplit = data.split(": ")
    if(len(dataSplit) > 1):
        loses = int(dataSplit[1])
    

print("Win file has " + str(wins) + " wins")
print("Lose file has " + str(loses) + " loses")

mon = {'top': 105, 'left': 575, 'width': 800, 'height': 200}

with mss.mss() as sct:
    while True:
        im = numpy.asarray(sct.grab(mon))
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        text = pytesseract.image_to_string(im)


        if "Victory" in text:
            if hasRead == False:
                wins += 1
                with open("wins.txt", 'w') as file:
                    file.write("Wins: " + str(wins))

                hasRead = True
        elif "Defeat" in text:
            if hasRead == False:
                loses += 1
                with open("lose.txt", 'w') as file:
                    file.write("Loses: " + str(loses))

                hasRead = True
        else:
            hasRead = False

        cv2.imshow('Image', im)

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        # One screenshot per second
        time.sleep(0.75)
