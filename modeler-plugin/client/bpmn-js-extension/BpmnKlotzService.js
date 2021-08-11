/**
 * A bpmn-js service that provides the actual plug-in feature.
 *
 * Checkout the bpmn-js examples to learn about its capabilities
 * and the extension points it offers:
 *
 * https://github.com/bpmn-io/bpmn-js-examples
 */



const createStartEvent = (canvas, modeling) => {
  const parent = canvas.getRootElement();
  modeling.createShape({ type: "bpmn:Task" }, {x: 200, y: 100}, parent);
}

export default function BpmnKlotzService(modeling, canvas) {
  const arucoCoord = [[[[229., 409.],
    [251., 413.],
    [245., 437.],
    [222., 432.]]], [[[445., 321.],
    [467., 325.],
    [465., 346.],
    [443., 342.]]],[[[100., 291.],
    [122., 294.],
    [115., 315.],
    [ 93., 311.]]],]
    
  const arucoIds =  [1,2,0]

  // eventBus.on('diagram.init', function() {
  //   createStartEvent(canvas, elementFactory, modeling);
  // });

  document.addEventListener('keydown', (event) => {
      if (event.key === 'k') {
      createStartEvent(canvas, modeling);
    }
  })

}

BpmnKlotzService.$inject = [
  'modeling',
  'canvas',
];