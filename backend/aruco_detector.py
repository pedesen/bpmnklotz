import cv2
import cv2.aruco as aruco
import id_to_elements

for camera_port in range(1, 10):
    try:
        cap = cv2.VideoCapture(camera_port)
        break
    except:
        pass

def capture():
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters_create()

    bpmn_snapshot = []
    corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    if len(corners) > 0:
        for index, element_id in enumerate(ids.flatten()):
            element_type = id_to_elements.id_to_elements(element_id)
            current_element = {
                  "id": element_id,
                  "type": element_type,
                  "corners": corners[index][0].tolist()
            }
            bpmn_snapshot.append(current_element)
    return bpmn_snapshot

