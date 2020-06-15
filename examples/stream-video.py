# simple example demonstrating how to control a Tello using your keyboard.
# For a more fully featured example see manual-control-pygame.py
#
# Use W, A, S, D for moving, E, Q for rotating and R, F for going up and down.
# When starting the script the Tello will takeoff, pressing ESC makes it land
#  and the script exit.
import sys
from threading import Thread

sys.path.append('D:\Projects\Tello\DJITelloPy\TelloSDKPy')

from djitellopy.tello import Tello
import cv2, math, time

tello = Tello()

tello.connect()
tello.streamon()


def video_stream():
    frame_read = tello.get_frame_read()
    while True:
        img = frame_read.frame
        cv2.imshow("drone", img)
        key = cv2.waitKey(1) & 0xff
        if key == 27:  # ESC
            break
    return 0


stream = Thread(target=video_stream)
stream.start()

tello.land()

stream.join()
tello.streamoff()
