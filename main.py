import cv2
import numpy as np
import pyautogui

ss = (1600,900)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 60.0, (ss))

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("screenshot", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
out.release()
cv2.destroyAllWindows()
