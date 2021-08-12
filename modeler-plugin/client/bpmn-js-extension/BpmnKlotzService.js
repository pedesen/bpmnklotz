const ELEMENTS = {
  0: {type: 'bpmn:StartEvent', eventDefinitionType: 'bpmn:MessageEventDefinition'},
  1: {type: 'bpmn:UserTask', },
  2: {type: 'bpmn:EndEvent'}
}
const WEBSOCKET_URL = 'localhost:8765'

let enabled = false;
let socket;
export default function BpmnKlotzService(eventBus, modeling, elementRegistry, canvas) {
  const model = () => {
    // remove all elements
    const allElements = elementRegistry.getAll();
    modeling.removeElements(allElements.filter(element => element.type !== "bpmn:Process"));
    // add elements
    const parent = canvas.getRootElement();
    arucoCoord.forEach((element, index) => {
      const bpmnElement = ELEMENTS[arucoIds[index]];
      // x/y coords of upper left corner
      const x = element[0][0];
      const y = element[0][1];
      modeling.createShape({...bpmnElement}, {x, y}, parent);
    }) 
  }

  const arucoCoord = [
    [
        [229., 409.],
        [251., 413.],
        [245., 437.],
        [222., 432.]
    ], [
        [445., 321.],
        [467., 325.],
        [465., 346.],
        [443., 342.]
    ], [
        [100., 291.],
        [122., 294.],
        [115., 315.],
        [ 93., 311.]
    ]
  ]
  const arucoIds =  [1,2,0]

  eventBus.on('editorActions.init', function(event) {
    var editorActions = event.editorActions;

    editorActions.register('toggle-klotz-detection', function() {
      enabled = !enabled;
      
      const container = document.querySelector('.djs-container')
        if (enabled) {
          socket = new WebSocket(`ws://${WEBSOCKET_URL}`);
          socket.addEventListener('message', function (event) {
            console.log('Message from server ', event.data);
            model();
          });
          container.classList.add('klotz');
        } else {
          socket.close();
          container.classList.remove('klotz');
        }
    });
  });

 

  document.addEventListener('keydown', (event) => {
    if (event.key === 'k') { model() }
  })
}

BpmnKlotzService.$inject = [
  'eventBus',
  'modeling',
  'elementRegistry',
  'canvas',
];