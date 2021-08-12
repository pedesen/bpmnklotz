# bpmnklotz

Model BPMN with building blocks (Bauklötzen)

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
