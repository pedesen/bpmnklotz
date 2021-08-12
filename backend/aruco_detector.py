import cv2
import cv2.aruco as aruco

camera_port = 0
cap = cv2.VideoCapture(camera_port)
ids_to_elements = {0: "StartEvent", 1: "ServiceTask", 2: "EndEvent"}

def capture():
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters_create()

    bpmn_snapshot = []
    corners, ids, _ = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    if len(corners) > 0:
        for element_id in ids.flatten():
            current_element = {
                  "id": element_id,
                  "type": ids_to_elements[element_id],
                  "corners": corners[0][0].tolist()
            }
            bpmn_snapshot.append(current_element)
    print(bpmn_snapshot)
    return bpmn_snapshot

