const ELEMENTS = {
  'StartEvent': {type: 'bpmn:StartEvent'},
  'MessageStartEvent': {type: 'bpmn:StartEvent', eventDefinitionType: 'bpmn:MessageEventDefinition'},
  "Task": {type: 'bpmn:Task'},
  "ServiceTask": {type: 'bpmn:ServiceTask'},
  "UserTask": {type: 'bpmn:UserTask'},
  "EndEvent": {type: 'bpmn:EndEvent'}
}
const WEBSOCKET_URL = 'localhost:5678'

let enabled = false;
let socket;
export default function BpmnKlotzService(eventBus, modeling, elementRegistry, canvas) {
  const model = (elements) => {
    // remove all elements
    const allElements = elementRegistry.getAll();
    modeling.removeElements(allElements.filter(element => element.type !== "bpmn:Process"));
    // add elements
    const parent = canvas.getRootElement();
    elements.forEach((element) => {
      const bpmnElement = ELEMENTS[element.type];
      // x/y coords of upper left corner
      const x = element.corners[0][0];
      const y = element.corners[0][1];
      modeling.createShape({...bpmnElement}, {x, y}, parent);
    }) 
  }

  eventBus.on('editorActions.init', function(event) {
    var editorActions = event.editorActions;

    editorActions.register('toggle-klotz-detection', function() {
      enabled = !enabled;
      
      const container = document.querySelector('.djs-container')
        if (enabled) {
          socket = new WebSocket(`ws://${WEBSOCKET_URL}`);
          socket.addEventListener('message', function (event) {
            console.log('event.data ', event.data);
            model(JSON.parse(event.data));
          });
          container.classList.add('klotz');
        } else {
          socket.close();
          container.classList.remove('klotz');
        }
    });
  });
}

BpmnKlotzService.$inject = [
  'eventBus',
  'modeling',
  'elementRegistry',
  'canvas',
];