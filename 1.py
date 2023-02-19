
from pyfirmata import Arduino, util
board = Arduino('COM4')
pin4 = board.get_pin('d:11:p')
pin3 = board.get_pin('d:10:p')
pin = 2
red = 0
green = 0
blue = 0
redsize = 0
bluesize = 0
programlevel = 0
import numpy as np
import cv2
board.digital[pin].mode = SERVO
def rotateservo(pin,angle):
    board.digital[pin].write(180)

webcam = cv2.VideoCapture(0)

while (1):
    _, imageFrame = webcam.read()

    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)


    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)


    blue_lower = np.array([94, 80, 2], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)


    kernal = np.ones((5, 5), "uint8")

    # For red color
    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(imageFrame, imageFrame,
                              mask=red_mask)

    # For green color
    green_mask = cv2.dilate(green_mask, kernal)
    res_green = cv2.bitwise_and(imageFrame, imageFrame,
                                mask=green_mask)

    # For blue color
    blue_mask = cv2.dilate(blue_mask, kernal)
    res_blue = cv2.bitwise_and(imageFrame, imageFrame,
                               mask=blue_mask)

    contours, hierarchy = cv2.findContours(red_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (0, 0, 255), 2)

            cv2.putText(imageFrame, "Red Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))
            red += 1
            redsize  = w + x + h + y
            o += w



    contours, hierarchy = cv2.findContours(green_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (0, 255, 0), 2)

            cv2.putText(imageFrame, "Green Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (0, 255, 0))
            green += 1


    contours, hierarchy = cv2.findContours(blue_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (255, 0, 0), 2)

            cv2.putText(imageFrame, "Blue Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 0, 0))
            blue += 1
            bluesize == x + w + y + h


    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
    if red == 0:
        board.digital[12].write(1)
        pin3.write(0.3)
        board.digital[13].write(0)
        pin4.write(0.6)
    if red > 0:
        board.digital[12].write(0)
        pin3.write(0.5)
        board.digital[13].write(0)
        pin4.write(0.5)
        red = 0
    if redsize >= 420:
        board.digital[12].write(0)
        pin3.write(0)
        board.digital[13].write(0)
        pin4.write(0)
        rotateservo(pin, 180)
        programlevel += 1
    if programlevel += 1
        rotateservo(pin, 0)
        programlevel += 1
    if programlevel == 3 and blue == 0:
        board.digital[12].write(1)
        pin3.write(0.3)
        board.digital[13].write(0)
        pin4.write(0.6)
    if programlevel == 3 and blue > 0:
        board.digital[12].write(0)
        pin3.write(0.5)
        board.digital[13].write(0)
        pin4.write(0.5)
        blue = 0
        programlevel += 1
    if programlevel == 4 and bluesize < 50:
        rotateservo(pin, 180)
        programlevel += 1






