import cv2
import cv2.aruco as aruco
import id_to_elements

fixed_camera_port = None

def find_camera(fixed_camera_port):
    if fixed_camera_port:
        return cv2.VideoCapture(fixed_camera_port)
    else:
        for camera_port in range(0, 10):
            try:
                return cv2.VideoCapture(camera_port)
            except:
                pass

def capture(cap):
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

