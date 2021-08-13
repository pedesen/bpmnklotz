import cv2
import cv2.aruco as aruco
import id_to_elements
import aruco_detector
import asyncio

async def show_image_with_detections(camera):
    label_color = (0, 0, 0)
    label_font = cv2.FONT_HERSHEY_DUPLEX
    while(True):
        # Capture frame-by-frame
        _, frame = camera.read()
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
                cv2.putText(frame, element_type, (int(x), int(y)), label_font,
                            1.3, label_color, 2, cv2.LINE_AA)
        if len(corners_invert) > 0:
            aruco.drawDetectedMarkers(frame, corners_invert)
            for index, element_id in enumerate(ids_invert.flatten()):
                element_type = id_to_elements.id_to_elements(element_id)
                (x,y) = corners_invert[index][0].tolist()[0]
                cv2.putText(frame, element_type, (int(x), int(y)), label_font,
                            1.3, label_color, 2, cv2.LINE_AA)
        else:
            pass

        cv2.imshow('BPMNKlotz', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


camera = aruco_detector.find_camera()
asyncio.run(show_image_with_detections(camera))
camera.release()
cv2.destroyAllWindows()
