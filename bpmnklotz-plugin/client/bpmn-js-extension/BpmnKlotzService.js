const ELEMENTS = {
  'StartEvent': {type: 'bpmn:StartEvent'},
  'MessageStartEvent': {type: 'bpmn:StartEvent', eventDefinitionType: 'bpmn:MessageEventDefinition'},
  "Task": {type: 'bpmn:Task'},
  "ServiceTask": {type: 'bpmn:ServiceTask'},
  "UserTask": {type: 'bpmn:UserTask'},
  "EndEvent": {type: 'bpmn:EndEvent'}
}
const WEBSOCKET_URL = 'localhost:5678'

const isSequenceFlow = (element) => {
  return ['SequenceFlowShort', 'SequenceFlowLong'].includes(element.type);
}

let enabled = false;
let socket;
let klotzCanvas;
export default function BpmnKlotzService(eventBus, modeling, elementRegistry, canvas) {
  const model = (elements) => {
    // remove all elements
    const allElements = elementRegistry.filter(element => element.type !== "bpmn:Process");
    modeling.removeElements(allElements);
    // add elements
    const parent = canvas.getRootElement();
    elements.forEach((element) => {

      if (isSequenceFlow(element)) {
        return;
      }

      const bpmnElement = ELEMENTS[element.type];
      // x/y coords of upper left corner
      const x = element.corners[0][0];
      const y = element.corners[0][1];
      modeling.createShape({...bpmnElement}, {x, y}, parent);
    })

    const sortedElements = elementRegistry.filter(element => element.type !== "bpmn:Process");
    sortedElements.sort((elA, elB) => elA.x - elB.x);
    
    
    for (let i = 0; i < sortedElements.length; i++) {
      let next;
      try {
        next = sortedElements[i+1]
        modeling.connect(sortedElements[i], next);
      } catch {
        next = null;
      }
    }
  }

  eventBus.on('editorActions.init', function(event) {
    var editorActions = event.editorActions;

    editorActions.register('toggle-klotz-detection', function() {
      enabled = !enabled;
      
      const container = document.querySelector('.djs-container')
        if (enabled) {
          socket = new WebSocket(`ws://${WEBSOCKET_URL}`);
          socket.addEventListener('message', function (event) {
            const elements = JSON.parse(event.data);
            model(elements);
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