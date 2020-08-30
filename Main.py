
# Imports
import time
import cv2
import mss
import numpy
import pytesseract

# Path for tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Variables
wins = 0
loses = 0
hasRead = False

# Load the data for wins.txt and lose.txt
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

# State how many wins and losses they have.
print("Win file has " + str(wins) + " wins")
print("Lose file has " + str(loses) + " loses")

# Get the position on the monitor
mon = {'top': 105, 'left': 575, 'width': 800, 'height': 250}

with mss.mss() as sct:
    while True:
        im = numpy.asarray(sct.grab(mon))

        text = pytesseract.image_to_string(im)

        # Using 'in' here because text likes to have a box in every string.
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

        # Wait .75 seconds.
        time.sleep(0.75)
