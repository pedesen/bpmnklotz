import cv2
import cv2.aruco as aruco
import id_to_elements
import aruco_detector
import asyncio
import sys

async def show_image_with_detections(cap):
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
        parameters = aruco.DetectorParameters_create()

        corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        corners_invert, ids_invert, _ = aruco.detectMarkers( cv2.bitwise_not(gray), aruco_dict, parameters=parameters)
        if len(corners) > 0:
            aruco.drawDetectedMarkers(frame, corners)
            for index, element_id in enumerate(ids.flatten()):
                element_type = id_to_elements.id_to_elements(element_id)
                (x,y) = corners[index][0].tolist()[0]
                cv2.putText(frame, element_type, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 0, 0), 2, cv2.LINE_AA)
        if len(corners_invert) > 0:
            aruco.drawDetectedMarkers(frame, corners_invert)
            for index, element_id in enumerate(ids_invert.flatten()):
                element_type = id_to_elements.id_to_elements(element_id)
                (x,y) = corners_invert[index][0].tolist()[0]
                cv2.putText(frame, element_type, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 0, 0), 2, cv2.LINE_AA)
        else:
            pass

        cv2.imshow('BPMNKlotz', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if len(sys.argv) > 1:
    cap = aruco_detector.find_camera(int(sys.argv[1]))
else:
    cap = aruco_detector.find_camera(None)
asyncio.run(show_image_with_detections(cap))
cap.release()
cv2.destroyAllWindows()
