import numpy as np
import cv2
import cv2.aruco as aruco

ids_to_elements = {0: "StartEvent", 1: "ServiceTask", 2: "EndEvent"}

def id_to_elements(id):
    try:
        return ids_to_elements[id]
    except:
        return "Unknown element type"

for camera_port in range(1, 10):
    try:
        cap = cv2.VideoCapture(camera_port)
        break
    except:
        pass

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
        for index, element_id in enumerate(ids.flatten()):
            element_type = id_to_elements(element_id)
            current_element = {"id": id, "type": element_type, "corners": corners[index][0]}
            bpmn_snapshort.append(current_element)
            # draw also in image
            elm = current_element
            x = elm['corners'][index][0]
            y = elm['corners'][index][1]
            image = cv2.putText(frame, element_type, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 0, 0), 2, cv2.LINE_AA)
        print(bpmn_snapshort)

    # Display the resulting frame
    cv2.imshow('BPMNKlotz', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
