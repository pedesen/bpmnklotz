# USAGE
# python detect-simple-bpmn-process.py --image images/simple.png
import cv2
import numpy as np
import argparse

outputImage = None

def read_image_from_commandline():
    arguments_parser = argparse.ArgumentParser()
    arguments_parser.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(arguments_parser.parse_args())
    image = cv2.imread(args["image"])
    print("Read picture from %s " % args["image"])
    return image


def normalize_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image


def detect_flows(image):
    flows = []
    blurred_image = 255 - cv2.medianBlur(image, 1)

    # Detect and draw lines
    lines = cv2.HoughLinesP(blurred_image, 1, np.pi/180, 200, minLineLength=30, maxLineGap=20)
    for line in lines:
        for x1, y1, x2, y2 in line:
            flows.append(("flow", x1, y1, x2, y2))
            cv2.line(outputImage, (x1, y1), (x2, y2), (0, 0, 255), 2)
    return flows

def detect_events(image):
    events = []
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT,
                               dp=1.8,
                               minDist=200,
                               param1=30, param2=75, minRadius=5,
                               maxRadius=100)
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        rounded_circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles

        for (x, y, r) in rounded_circles:
            events.append(("event", x, y))
            cv2.circle(outputImage, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(outputImage, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    return events

def detect_tasks(image):
    tasks = []
    thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 71, 9)

    # Fill rectangular contours
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        cv2.drawContours(thresh, [c], -1, (255, 255, 255), -1)

    # Morph open
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=4)

    # Draw rectangles
    cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(outputImage, (x, y), (x + w, y + h), (36, 255, 12), 3)
        tasks.append(("task", x, y, w, h))
    return tasks

def unique_elements(elements):
    unique_elements = []
    last_type = ""
    for el in elements:
        if el[0] == "flow" and last_type == "flow":
            print("Drop duplicate", el)
        else:
            unique_elements.append(el)
        last_type = el[0]
    return unique_elements

takenImage = read_image_from_commandline()
outputImage = takenImage.copy()

normalizedImage = normalize_image(takenImage)
flows = sorted(detect_flows(normalizedImage), key=lambda  t: t[1])
events = sorted(detect_events(normalizedImage), key=lambda t: t[1])
tasks = sorted(detect_tasks(normalizedImage), key=lambda t: t[1])
elements = unique_elements(sorted(events + flows + tasks, key=lambda t: t[1]))

print("Model: %s", elements)
#print("All events: %s" % events)
#print("Start (x,y) event, ", events[0])
#print("Flows (x1,y1,x2,y2): %s " % flows)
#print("Tasks (x,y,w,h) : %s" % tasks)
#print("End event (x,y) : ", events[-1])
cv2.imshow("output", np.hstack([takenImage, outputImage]))
cv2.waitKey(0)
cv2.destroyAllWindows()
