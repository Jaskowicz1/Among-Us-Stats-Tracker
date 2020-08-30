# Among-Us-Stats-Tracker
Reads text on screen to allow statistics about wins and losses. When the code sees "Victory" or "Defeat", it will write to either "wins.txt" or "lose.txt" and increase the number of wins or losses. This means this allows OBS/Streamlabs OBS to work with this.

Tested and programmed in Python 3.7.


---


# Requirements

- Python
- cv2 (pip install cv2)
- mss
- numpy
- pytesseract
- tesseract (https://github.com/UB-Mannheim/tesseract/wiki)

(chat and console messages can be the same but may cause conflict).


---


# Usage/Installation

When you have all the requirements installed, run the python script "Main.py". This should come up with a box that shows a new frame of part of you monitor every .75 seconds. This box is what determines whether you got a win or a loss.

It's advised to wait until the counter increases before hitting "Play Again" otherwise your stats may not change.


---


# Errors


You may get an error along the lines of `tesseract is not installed or it's not in your PATH. See README file for more information.`. This is either because you didn't install tesseract from the link, or the path `C:/Program Files/Tesseract-OCR/tesseract.exe` is incorrect. If you did install tesseract and you're still getting this error, change the path to the path of `tesseract.exe` on line 8.

---


# Licence


<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
