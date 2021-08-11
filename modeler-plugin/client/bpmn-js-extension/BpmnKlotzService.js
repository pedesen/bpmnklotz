const ELEMENTS = {
  0: 'bpmn:StartEvent',
  1: 'bpmn:Task',
  2: 'bpmn:EndEvent'
}

export default function BpmnKlotzService(modeling, elementRegistry, canvas) {
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

  document.addEventListener('keydown', (event) => {
    if (event.key === 'k') {
      // remove all elements
      const allElements = elementRegistry.getAll();
      modeling.removeElements(allElements.filter(element => element.type !== "bpmn:Process"));

      // add elements
      const parent = canvas.getRootElement();
      arucoCoord.forEach((element, index) => {
        const type = ELEMENTS[arucoIds[index]];
        // x/y coords of upper left corner
        const x = element[0][0];
        const y = element[0][1];
        modeling.createShape({ type }, {x, y}, parent);
      }) 
    }
  })
}

BpmnKlotzService.$inject = [
  'modeling',
  'elementRegistry',
  'canvas',
];