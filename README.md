# bpmnklotz

Model BPMN with building blocks.

This is a Camunda Summer Hack Days project from 2021. The goal was to create BPMN symbols as tangible building blocks, which can be used to model a digital version of the diagram.

## How does it work?

The project consists of a python backend running OpenCV, which recognizes Aruco markers (similar to QR Codes), and a Camunda Modeler plugin which creates BPMN elements on the canvas. The backend sends all recognized markers to the Camunda Modeler via a websockets connection. 

## Setup & Run Server

```
cd backend
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python server.py [camera port as integer]
```
## Test detection
```
cd backend
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python server.py [camera port as integer]
python show_detection.py [camera port as integer]
```
## Setup & Run Modeler Plugin
```
cp bpmnklotz-plugin <camunda-modeler-plugin-folder>
```

or

```
cd <camunda-modeler-plugin-folder>
ln -s <bpmnklotz-repo>/bpmnklotz-plugin
```

* Run Modeler
* Menu -> BPMN Klotz -> Enable Klotz Detection
