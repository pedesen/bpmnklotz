include <./lib/bpmn-coasters.scad>

gateway("parallel", "", aruco=[ // 42
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
]);