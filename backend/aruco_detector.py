import cv2
import cv2.aruco as aruco
import id_to_elements
import sys


def find_camera():
    if len(sys.argv) > 1:
        camera_port = int(sys.argv[1])
        print("Use camera port %s" % camera_port)
        return cv2.VideoCapture(camera_port)
    else:
        print("No camera port given. Try to detect camera.")
        for camera_port in range(0, 10):
            try:
                camera = cv2.VideoCapture(camera_port)
                print("Use camera port %s" % camera_port)
                return camera
            except:
                pass
        print("No camera found.")

def capture(camera):
    # Capture frame-by-frame
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters_create()

    bpmn_snapshot = []
    corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    corners_invert, ids_invert, _ = aruco.detectMarkers( cv2.bitwise_not(gray), aruco_dict, parameters=parameters)
    if len(corners) > 0:
        for index, element_id in enumerate(ids.flatten()):
            element_type = id_to_elements.id_to_elements(element_id)
            current_element = {
                  "id": element_id,
                  "type": element_type,
                  "corners": corners[index][0].tolist()
            }
            bpmn_snapshot.append(current_element)
    if len(corners_invert) > 0:
        for index, element_id in enumerate(ids_invert.flatten()):
            element_type = id_to_elements.id_to_elements(element_id)
            current_element = {
                "id": element_id,
                "type": element_type,
                "corners": corners_invert[index][0].tolist()
            }
            bpmn_snapshot.append(current_element)
    else:
        pass
    return bpmn_snapshot

