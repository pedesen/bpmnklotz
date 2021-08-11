import numpy as np
import cv2
import cv2.aruco as aruco

cap = cv2.VideoCapture(0)

ids_to_elements = {0: "StartEvent", 1: "ServiceTask", 2: "EndEvent"}

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters_create()

    bpmn_snapshort = []
    corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    if len(corners) > 0:
        gray = aruco.drawDetectedMarkers(frame, corners)
        for id in ids.flatten():
            current_element = {"id": id, "type": ids_to_elements[id], "corners": corners[0][0]};
            bpmn_snapshort.append(current_element)
            # draw also in image
            elm = current_element
            x = elm['corners'][0][0]
            y = elm['corners'][0][1]
            image = cv2.putText(frame, elm['type'], (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 0, 0), 2, cv2.LINE_AA)
        print(bpmn_snapshort)

    # Display the resulting frame
    cv2.imshow('BPMNKlotz', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
