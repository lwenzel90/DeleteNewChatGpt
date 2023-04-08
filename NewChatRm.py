from time import sleep
import cv2
import numpy as np
import pyautogui

def find_image_on_screen(image_paths, threshold=0.9):
    for path in image_paths:        
        # Load the template image
        template = cv2.imread(path, cv2.IMREAD_UNCHANGED)

        # Take a screenshot and convert it to grayscale
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        # Perform template matching
        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

        # Find locations where the matching score is above the threshold
        loc = np.where(res >= threshold)

        print(zip(*loc[::-1]))
        coordinates = []
        # Iterate through the matching locations and print their coordinates
        for pt in zip(*loc[::-1]):
            print(f"Found image at: {pt}")
            coordinates.insert(0, pt)
            
        coordinates.reverse()
        for pt in coordinates:
            if pt == coordinates[0]:
                print("Moving mouse 5px down and 5px right")
                # move the mouse 5px down and 5px right, update tuple with new coordinates
                pt = (pt[0] + 0, pt[1] + 0)
                pyautogui.moveTo(pt)
                sleep(.5)
                # click the mouse
                pyautogui.click()
                sleep(.5)

if __name__ == "__main__":
    image_paths = [
        "./NewChat.png",
        "./TrashCan.png",
        "./CheckMark.png"
    ]
    # forever loop
    run = True
    if run:
        find_image_on_screen(image_paths)